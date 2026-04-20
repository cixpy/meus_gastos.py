# Meus Gastos 💰

Uma aplicação web para gerenciar e controlar seus gastos pessoais de forma simples e eficiente.

## 🚀 Recursos

- ✅ Adicionar novos gastos com descrição e valor
- ✅ Visualizar lista de todos os gastos
- ✅ Calcular total de gastos automaticamente
- ✅ Deletar gastos específicos
- ✅ Interface responsiva e amigável
- ✅ Armazenamento em sessão para dados temporários

## 🛠️ Tecnologias Utilizadas

- **Backend**: Python com Flask
- **Frontend**: HTML, CSS e JavaScript
- **Análise de Dados**: Pandas e NumPy
- **Exportação**: OpenPyXL (para gerar planilhas)
- **Email**: Flask-Mail
- **Deploy**: Vercel (serverless)
- **Ambiente**: Python-dotenv para variáveis de ambiente

## 📋 Requisitos

- Python 3.7+
- pip (gerenciador de pacotes Python)

## 🔧 Instalação

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/meus_gastos.py.git
cd meus_gastos.py
```

2. Crie um ambiente virtual:
```bash
python -m venv .venv

# Windows
.venv\Scripts\activate

# macOS/Linux
source .venv/bin/activate
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

4. Configure as variáveis de ambiente:
```bash
# Crie um arquivo .env na raiz do projeto
cp .env.example .env  # se existir
# ou crie manualmente com:
echo SECRET_KEY=sua_chave_secreta_aqui > .env
```

## 🏃 Como Executar

### Localmente (Desenvolvimento)
```bash
cd api
python app.py
```

Acesse a aplicação em `http://localhost:5000`

### Deploy no Vercel
A configuração para deploy automático no Vercel já está pronta no arquivo `vercel.json`. Basta fazer push para seu repositório conectado ao Vercel.

## 📁 Estrutura do Projeto

```
meus_gastos.py/
├── api/
│   ├── app.py              # Aplicação Flask principal
│   ├── static/
│   │   ├── script.js       # JavaScript frontend
│   │   └── style.css       # Estilos da aplicação
│   └── templates/
│       └── index.html      # Template HTML principal
├── requirements.txt        # Dependências do projeto
├── vercel.json            # Configuração para deploy Vercel
└── README.md              # Este arquivo
```

## 🎯 Como Usar

1. **Adicionar um Gasto**: Preencha a descrição e o valor do gasto, clique em "Adicionar"
2. **Visualizar Gastos**: A lista de gastos aparece automaticamente na tela
3. **Ver Total**: O total é calculado e exibido automaticamente
4. **Deletar Gasto**: Clique no botão de deletar ao lado do gasto que deseja remover

## 🔐 Segurança

- A aplicação usa a chave `SECRET_KEY` para proteger as sessões
- Configure uma chave forte no arquivo `.env` em produção
- Certifique-se de adicionar `.env` ao `.gitignore` para não expor dados sensíveis

## 📧 Variáveis de Ambiente

```
SECRET_KEY=sua_chave_secreta_muito_forte_aqui
MAIL_USERNAME=seu_email@gmail.com
MAIL_PASSWORD=sua_senha_de_app
```

## 🤝 Contribuindo

Contribuições são bem-vindas! Para contribuir:

1. Faça um Fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/MinhaFeature`)
3. Commit suas mudanças (`git commit -m 'Adiciona MinhaFeature'`)
4. Push para a branch (`git push origin feature/MinhaFeature`)
5. Abra um Pull Request

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

## 👨‍💻 Autor

Criado por [seu-nome](https://github.com/seu-usuario)

## 📞 Suporte

Se tiver dúvidas ou encontrar problemas, abra uma [Issue](https://github.com/seu-usuario/meus_gastos.py/issues) no GitHub.

---

