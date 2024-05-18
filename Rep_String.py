"""2 - Repetindo Textos ✏️
Descrição: Agora vamos solicitar uma string e um número inteiro como entrada. Depois teremos que retornar a string repetida o número de vezes informado.

O que aprenderemos?

Manipulação de Strings (string)
Números Inteiros (int)
Múltiplas repetições
Entrada de dados
Aproveitar as sugestões do Github Copilot"""

def repetir_string():
    
    string = input("Digite uma string: ")
    
    num_repeticoes = int(input("Digite um número inteiro para repetir a string: "))
    resultado1 = string * num_repeticoes
    resultado2 = ""

    for _ in range(num_repeticoes):
        resultado2 += string+" "

    opcao = int(input("Digite a opção de repetição: 1 - concatenado, 2 - espaçado "))

    if opcao == 1:
        print(resultado1)
    elif opcao == 2:
        print(resultado2)
    else:
        print("Opção inválida!")

repetir_string()
