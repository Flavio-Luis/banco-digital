from os import system # modulo importado para criar uma function de limpar o terminal

login = '1' # valor padrão
password_default = "b" # valor padrão
balance = 0 # valor padrão
        
def validation_login(input_user_login): # function responsavel por validar o login do usuário

    while input_user_login != login: # loop para validar se as senhas batem, caso não bater, fica no loop até acertar !
        print("Invalid login!❌")
        input_user_login = input("Enter your login again:")
        continue
    print("Login Correct!✔️\n")
    result = 1 # retorno de um valor para a próxima function, com o intuito de evitar bugs(LEIA A DOCUMENTAÇÃO)
    return result

def validation_password(validation_login): # function responsavel por validar a senha do usuário

    if validation_login == 1: # validação do valor retornado da function validation_login, para saber se realmente está correto o login e prosseguir!
        input_user_password = input("Type your password:")
        while input_user_password != password_default: # loop para verificar se a senha digitada é a mesma armazenada
            print("Password Incorreto!❌")
            input_user_password = input("Enter your password again:")
            continue
    result = "Password Correct!✔️\n"
    return result

def validation_option(value_insert=0): # function responsavel por validar somente digitos válidos no MENU de funções do programa
    
    while True: # loop que verifica se os dígitos do usuário será aceito no programa
        try:
            choice_user_option = (input("\nPlease enter the option you want:"))
            choice_user_option_trat = int(choice_user_option) # atribuição do dado digitado pelo usuário a uma variavel com o intuito de validar
            if choice_user_option_trat < 1 or choice_user_option_trat > 4: # verificação se está digitando no intervalo correto
                    clear() # limpar terminal
                    print(f"\nThe digit '{choice_user_option_trat}' is not accepted!⚠️\n")
                    display_option(option)
                    continue
            break
        except ValueError:
            clear()
            print(f"\nDigit '{choice_user_option}' Invalid entered!⚠️\n")
            display_option(option)
            continue    

    return choice_user_option_trat

def validation_restart(value_restart=0): # function responsável por validar se o cliente deseja continuar ou não
    
    while True: # loop da verificação, para analisar se está digitando os valores corretos
        try:
            restart = input("\nEnter the option you want: ")
            restart_trat = int(restart)
            if restart_trat < 1 or restart_trat > 2:
                clear()
                print(f"The digit {restart_trat} is not accepted!⚠️\n")
                display_option(finally_program) # function que exibe as opções da dict finally_program no terminal
                continue
            break
        except ValueError:
            clear()
            print(f"\nDigit {restart} invalid!⚠️\n")
            display_option(finally_program)
            continue

    return restart_trat    

def display_option(option): # function responsavel por exibir as opções de dict na tela
    print("           OPTIONS           \n")
    for key,value in option.items(): # loop que exibe cada chave valor da dict no terminal
        print(f"{key} : {value}")

def banking_movement(choice_user_option): # function responsável por realizar as movimentações bancárias
    match choice_user_option:
        case 1:
            result_movement_banking = balance
        case 2:
            input_money_balance = float(input("What is the Deposit Amount: R$"))
            result_movement_banking = balance + input_money_balance
        case 3:
            while True:
                input_remove_money = float(input("What will be the withdrawal amount: R$"))
                result_movement_banking = balance - input_remove_money
                if result_movement_banking < 0 :
                    print("\n❌!Withdrawal amount is greater than the balance amount!❌")
                    print("\nAnswer with 'y' for yes or 'n' for no")
                    input_balance_error = input("Do you want to type again?").lower().startswith("s")
                
                    if input_balance_error is True:
                        print()
                        continue
                    else:
                        result_movement_banking = balance
                        break
                break
        case 4:
            result_movement_banking = input("Inté my brother!🤟")

    return result_movement_banking

def clear(): # function responsável por limpar o terminal
    system("cls")

option = { # dict com opções que o banco te possibilita
    1 : "EXTRACT",
    2 : "DEPÓSIT",
    3 : "WITHDRAW",
    4 : "CLOSE"

}

finally_program = { # dict com opções de encerrar o programa ou recomeçar
    1 : "RETURN TO MENU",
    2 : "END THE PROGRAM"
}

print("Welcome to your digital bankl📲\n") # começo do programa

input_user_login = input("Enter your login:")
result_validation_login = validation_login(input_user_login)

result_validation_password = validation_password(result_validation_login)
print(result_validation_password)

clear()
print("Access allowed!✔️\n")

while True: # loop que permite continuar com o programa

    display_option(option) # function que exibe as opções da dict option na tela

    option_trat = validation_option()

    result_finally = banking_movement(option_trat)
    balance = result_finally # armazenamento do valor de saldo na variavel "balance"

    clear()
    print(f"\nYour balance is R${result_finally:.2f}\n")
    
    display_option(finally_program)

    validation_restart_trat = validation_restart()

    if validation_restart_trat == 1: # verificação se deseja continuar com o programa ou encerrar
        clear()
        continue
    elif validation_restart_trat == 2:
        print("Inté my brother!🤟")
        break
    else:
        print("Unknown parameter")