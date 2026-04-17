import os
from flask import Flask, render_template, request, redirect, url_for, session
from dotenv import load_dotenv
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formataddr
import smtplib

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv(
    "SECRET_KEY", "secret_key_fallback"
)  # Defina uma chave secreta para as sessões


class ExpenseManager:
    @staticmethod
    def add_expense(description, amount):
        if "expenses" not in session:
            session["expenses"] = []
        session["expenses"].append({"description": description, "amount": amount})
        session.modified = True  # Garante que a sessão seja atualizada

    @staticmethod
    def show_expenses():
        return session.get("expenses", [])

    @staticmethod
    def calculate_total():
        return sum(expense["amount"] for expense in session.get("expenses", []))

    @staticmethod
    def delete_expense(index):
        """Remove o gasto pelo índice."""
        if "expenses" in session and 0 <= index < len(session["expenses"]):
            session["expenses"].pop(index)
            session.modified = True  # Atualiza a sessão após a remoção


# Filtro customizado para formatar números
@app.template_filter('format_number')
def format_number(value):
    try:
        return f"{value:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
    except (ValueError, TypeError):
        return value


# Página principal
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        description = request.form["description"]
        amount = float(request.form["amount"])
        ExpenseManager.add_expense(description, amount)
        return redirect(url_for("index"))

    expenses = ExpenseManager.show_expenses()
    total = ExpenseManager.calculate_total()
    return render_template("index.html", expenses=expenses, total=total)


# Remover gasto
@app.route("/delete/<int:index>", methods=["POST"])
def delete_expense(index):
    ExpenseManager.delete_expense(index)
    return redirect(url_for("index"))


# Enviar relatório por e-mail
@app.route("/send_email", methods=["POST"])
def email():
    to_email = request.form["to_email"]

    expenses = ExpenseManager.show_expenses()
    total = ExpenseManager.calculate_total()
    if expenses:
        expenses_text = "\n".join(
            [
                f"{index + 1}. {expense['description']}: R${expense['amount']:.2f}"
                for index, expense in enumerate(expenses)
            ]
        )
        expenses_rows_html = "".join(
            [
                (
                    "<tr>"
                    f"<td style='padding:8px;border:1px solid #ddd'>{index + 1}</td>"
                    f"<td style='padding:8px;border:1px solid #ddd'>{expense['description']}</td>"
                    f"<td style='padding:8px;border:1px solid #ddd;text-align:right'>R${expense['amount']:.2f}</td>"
                    "</tr>"
                )
                for index, expense in enumerate(expenses)
            ]
        )
    else:
        expenses_text = "Nenhum gasto registrado."
        expenses_rows_html = (
            "<tr><td colspan='3' style='padding:8px;border:1px solid #ddd;text-align:center'>"
            "Nenhum gasto registrado."
            "</td></tr>"
        )

    text_body = (
        "Olá!\n\n"
        "Segue seu relatório de gastos:\n\n"
        f"{expenses_text}\n\n"
        f"Total: R${total:.2f}\n\n"
        "Atenciosamente,\n"
        "DevCix - Relatório de Gastos"
    )

    html_body = f"""
    <div style="font-family:Arial,sans-serif;color:#1f2937;line-height:1.5">
      <h2 style="margin-bottom:8px">Relatório de Gastos</h2>
      <p style="margin-top:0">Olá! Segue abaixo o resumo dos seus gastos.</p>
      <table style="border-collapse:collapse;width:100%;max-width:640px;margin-top:16px">
        <thead>
          <tr style="background:#f3f4f6">
            <th style="padding:8px;border:1px solid #ddd;text-align:left">#</th>
            <th style="padding:8px;border:1px solid #ddd;text-align:left">Descrição</th>
            <th style="padding:8px;border:1px solid #ddd;text-align:right">Valor</th>
          </tr>
        </thead>
        <tbody>
          {expenses_rows_html}
        </tbody>
        <tfoot>
          <tr>
            <td colspan="2" style="padding:10px;border:1px solid #ddd;text-align:right"><strong>Total</strong></td>
            <td style="padding:10px;border:1px solid #ddd;text-align:right"><strong>R${total:.2f}</strong></td>
          </tr>
        </tfoot>
      </table>
      <p style="margin-top:16px">Atenciosamente,<br><strong>DevCix - Relatório de Gastos</strong></p>
    </div>
    """

    smtp_server = os.getenv("SMTP_SERVER")
    smtp_port = int(os.getenv("SMTP_PORT"))
    login = os.getenv("LOGIN")
    password = os.getenv("PASSWORD")
    from_email = formataddr(("DevCix - Relatório de Gastos", login))
    subject = "Relatório de Gastos"

    send_email(
        subject,
        text_body,
        html_body,
        to_email,
        from_email,
        smtp_server,
        smtp_port,
        login,
        password,
    )

    return redirect(url_for("index"))


def send_email(
    subject,
    text_body,
    html_body,
    to_email,
    from_email,
    smtp_server,
    smtp_port,
    login,
    password,
):
    msg = MIMEMultipart("alternative")
    msg["From"] = from_email
    msg["To"] = to_email
    msg["Subject"] = subject
    msg.attach(MIMEText(text_body, "plain", "utf-8"))
    msg.attach(MIMEText(html_body, "html", "utf-8"))

    try:
        # Conexão com o servidor SMTP usando STARTTLS
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Inicia a conexão segura
            server.login(login, password)  # Autenticação
            server.send_message(msg)
            print("Email enviado com sucesso!")
    except smtplib.SMTPException as e:
        print(f"Falha ao enviar o email: {e}")


# Executa o app
if __name__ == "__main__":
    app.run(debug=True)
