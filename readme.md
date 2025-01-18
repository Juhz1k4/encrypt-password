# encrypt-password

Bem-vindo ao repositório **encrypt-password**, um projeto desenvolvido para demonstrar como unir o **Python** básico com tecnologias web, criando um gerador de senhas seguras e interativo. Este projeto combina conceitos de dois cursos distintos, elevando a experiência de aprendizado através da prática.

## 🚀 Sobre o Projeto

Este projeto foi criado com o objetivo de:

- Demonstrar a criação de um sistema simples e eficiente de geração de senhas seguras.
- Integrar **Python**, **HTML**, **CSS**, e **JavaScript** em uma aplicação funcional.
- Praticar conceitos básicos de programação e manipulação de dados.
- Fornecer uma interface interativa e moderna para os usuários.

## 🛠️ Funcionalidades

- **Criptografia Personalizada:**
  - Transforma senhas digitadas em versões mais seguras com substituições inteligentes.

- **Análise de Força da Senha:**
  - Classifica a senha como **fraca**, **média** ou **forte** com feedback visual intuitivo.

- **Interface Intuitiva:**
  - Um fundo com design inspirado na "Matrix" para maior imersão.

- **Tecnologias Combinadas:**
  - Backend com **Flask** para processar as requisições.
  - Frontend responsivo utilizando **HTML**, **CSS** e **JavaScript**.

## 🔧 Tecnologias Utilizadas

- **Python**
- **Flask** e **Flask-CORS**
- **HTML** e **CSS**
- **JavaScript**

## 🔍 Visão Geral do Projeto

### Backend
O backend foi desenvolvido com **Flask** e gerencia a lógica de geração de senhas e a análise de segurança. Ele está configurado para receber requisições e retornar respostas JSON contendo a senha criptografada e a classificação de segurança.

### Frontend
O frontend foi criado para oferecer uma experiência amigável ao usuário. Ele apresenta:

- Um campo de entrada para digitar a senha.
- Um botão para acionar a criptografia.
- Feedback visual dinâmico com mensagens e cores (vermelho, amarelo e verde).

## 🔄 Como Executar o Projeto

### Clonando o Repositório

1. Clone este repositório:
   ```bash
   git clone https://github.com/Juhz1k4/encrypt-password.git
   ```

2. Navegue até o diretório do projeto:
   ```bash
   cd encrypt-password
   ```

### Instalando Dependências

Certifique-se de que o **Python** está instalado em seu sistema. Em seguida, instale as dependências necessárias:

```bash
pip install flask flask-cors
```

### Executando o Backend

Inicie o servidor Flask:

```bash
python app.py
```

O backend será executado em:

```
http://127.0.0.1:5000
```

### Executando o Frontend

Abra o arquivo `index.html` diretamente no navegador ou utilize uma extensão como **Live Server** no VSCode para servir o frontend localmente.

## 🌐 Experimente o Projeto

1. Abra o frontend no navegador.
2. Digite uma senha no campo indicado.
3. Clique em "Criptografar" e veja o resultado.

- Você verá a senha criptografada e um feedback sobre a força dela.

## 🎨 Melhorias Futuras

- **Personalização de Criptografia:** Permitir que o usuário defina padrões de substituição.
- **Exportação de Senhas:** Adicionar opção para salvar ou copiar senhas.
- **Interface Animada:** Criar animações para o fundo em tempo real.
- **Suporte Multilíngue:** Disponibilizar a aplicação em diferentes idiomas.

## 📢 Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para enviar pull requests ou abrir issues com sugestões e melhorias.

PS: Este projeto foi desenvolvido enquanto ainda estou aprendendo as linguagens utilizadas, por isso pode haver oportunidades de melhorias. 😊

