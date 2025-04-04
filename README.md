# 🤖 BOT PREENCHIMENTO DE FORMULÁRIO

Este projeto automatiza o preenchimento de formulários de cadastro no site [Agendor](https://beta.agendor.com.br/people/new), utilizando Selenium e uma interface simples em terminal. Ideal para agilizar cadastros em massa com feedback visual usando `colorama`.

---

## 🚀 Funcionalidades

- Login automático com verificação em loop  
- Suporte a múltiplos cadastros por entrada no terminal  
- Uso de `colorama` para uma experiência visual melhor no terminal  
- Preenchimento completo dos campos do formulário com envio automático  
- Limpeza de terminal entre etapas para melhor legibilidade  

---

## 🧰 Tecnologias usadas

- Python 🐍  
- Selenium  
- Colorama  
- WebDriver (Chrome)  

---

## ⚙️ Como usar

1. **Clone o repositório:**

   ```bash
   git clone https://github.com/keseyf/bot-formulario
   cd bot-formulario

2. **Instale as dependências:**

- Instale o python
- pip install selenium colorama
- Baixe o ChromeDriver compatível com a sua versão do Chrome e adicione-o ao seu PATH.

3. **Execute o script:**
- python botformulario.py

## Utilizando o bot:
#### Ao iniciar o bot será pedido login e senha para acessar o site, e devera ser passado desta maneira:
`email@example.com` e `senha`  

#### Após deverá ser colado as informações dos usuários, cada campo de informação do usuário é separado por vírgula "," e cada usuario é separado por ";".
⚠️ Avisos
Verifique se todos os 10 campos estão preenchidos para cada usuário.

O botão de envio do formulário é acionado via tecla ENTER (não possui id ou name).

Após cada envio, o script aguarda uma confirmação no terminal para prosseguir.
