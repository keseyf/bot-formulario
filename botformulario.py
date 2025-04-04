import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from colorama import init, Fore, Style

init(autoreset=True)

def limpar_terminal():
    os.system("cls" if os.name == "nt" else "clear")

def solicitar_login():
    while True:
        limpar_terminal()
        print(Fore.CYAN + "Digite os dados de login no formato:")
        print(Fore.YELLOW + "email@example.com,senha\n")
        entrada = input("> ").strip().split(",")
        if len(entrada) == 2:
            return entrada[0], entrada[1].strip()
        else:
            print(Fore.RED + "Formato inválido! Pressione Enter para tentar novamente.")
            input()

def solicitar_dados():
    limpar_terminal()
    print(Fore.CYAN + "Digite os dados dos usuários no seguinte formato:")
    print(Fore.YELLOW + "nome,cpf,cnpj,razão_social,data_nasc,ano_nasc,email,cep,número,complemento; ...")
    print(Fore.LIGHTBLACK_EX + "(Separe os campos com vírgula e os usuários com ponto e vírgula)\n")
    entrada = input("> ").strip()
    usuarios = [u.strip().split(",") for u in entrada.split(";")]
    for u in usuarios:
        if len(u) != 10:
            raise ValueError("Um ou mais cadastros estão com dados incompletos.")
    return usuarios

def preencher_formulario(driver, dados):
    campos = [
        "name", "cpf", "q", "job_title", "birthday",
        "birth_year", "contact.email", "address.postal_code",
        "address.street_number", "address.additional_info"
    ]
    for i, campo in enumerate(campos):
        input_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, campo))
        )
        input_element.clear()
        input_element.send_keys(dados[i])
    input_element.send_keys(Keys.ENTER)

def main():
    email, senha = solicitar_login()
    usuarios = solicitar_dados()

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=chrome_options)

    try:
        driver.get("https://web.agendor.com.br/entrar/")
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "email"))).send_keys(email)
        driver.find_element(By.ID, "senha").send_keys(senha)
        driver.find_element(By.ID, "btnEnviar").click()
        WebDriverWait(driver, 15).until(EC.url_contains("beta.agendor.com.br"))

        for index, usuario in enumerate(usuarios, start=1):
            driver.get("https://beta.agendor.com.br/people/new")
            print(Fore.GREEN + f"\n[{index}] Preenchendo dados de: {usuario[0]}")
            preencher_formulario(driver, usuario)
            print(Fore.CYAN + "\nFormulário enviado.")
            input(Fore.YELLOW + "Pressione Enter para continuar para o próximo cadastro...")

        print(Fore.GREEN + "\nTodos os formulários foram enviados com sucesso!")
        driver.quit()

    except Exception as e:
        print(Fore.RED + f"\nErro: {e}")

if __name__ == "__main__":
    main()
  
