"""3 - Operações Matemáticas Simples 📐
Descrição: Vamos solicitar como entrada dois números e depois vamos realizar uma operação simples entre eles.

O que aprenderemos?

Operações Matemáticas Básicas
Entrada de dados
Utilização eficiente do Github Copilot"""


def operacao_mat():
    num1 = int(input("Digite um número inteiro para usar na operação: "))
    
    num2 = int(input("Digite mais um número inteiro para usar na operação: "))

    opcao = input("Digite a opção de operação: + , - , / , * : ")
    
    if opcao == "+":
        print(num1 + num2)
    elif opcao == "-":
        print(num1 - num2)
    elif opcao == "/":
        print(num1 / num2)
    elif opcao == "*":
        print(num1 * num2)
    else:
        print("Opção inválida!")
operacao_mat()