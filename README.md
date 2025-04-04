# 🤖 BOT PREENCHIMENTO DE FORMULÁRIO

Este projeto automatiza o preenchimento de formulários de cadastro no site [Agendor](https://beta.agendor.com.br/), utilizando Selenium e uma interface simples em terminal. Ideal para agilizar cadastros em massa com feedback visual usando `colorama`.

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
- `python botformulario.py`

## Utilizando o bot:
#### Ao iniciar o bot será pedido login e senha para acessar o site, e devera ser passado desta maneira:
`email@example.com` e `senha`  

#### Após deverá ser colado as informações dos usuários, cada campo de informação do usuário é separado por vírgula "," e cada usuario é separado por ";".

### Exemplo de como os dados devem ser passados:

`Nome, Cpf, Cnpj, Razão_social, Data_nascimento (DD/MM), Ano_nasc (YYYY), Email, Cep, Número, Complemento;`


⚠️ Avisos
Verifique se todos os 10 campos estão preenchidos para cada usuário.

A função de envio do formulário é **NÃO** foi adicionado, e é de **EXCLUSIVA** obrigatoriedade do cliente. Caso o formulario não tenha sido enviado antes de iniciar o preenchimento do próximo cliente, o anterior não será submetido.

Após cada preenchimento, o script irá aguardar uma confirmação no terminal para prosseguir, Que deve ser feita apertando  **ENTER**.

*quaiser dúvida contatar o programador.*
