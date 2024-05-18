"""1 - Concatenando Dados 🐾
Descrição: Vamos receber dois dados diferentes do usuário e concatena-los em uma única string?!

O que aprenderemos?

Manipulação de Strings (string)
Concatenação
Entrada de dados
Utilização eficiente do Github Copilot
"""


def concatenar_strings():
    
    string1 = input("Digite a primeira string: ")
    string2 = input("Digite a segunda string: ")


    resultado = string1 + " " + string2


    return resultado

print(concatenar_strings())