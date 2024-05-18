"""6 - Verificando Palíndromos 🔄
Descrição: Vamos testar se uma palavra é um palíndromo?! Uma dica é: Utilize conceitos de manipulação de strings para inverter a palavra e comparar com a original.

O que aprenderemos?

Manipulação de strings em Python, especialmente invertendo uma string.
Compreensão de como comparar a string original com sua versão invertida para determinar se é um palíndromo.
Introdução ao conceito de palíndromos e sua aplicação em problemas de programação."""

def eh_palindromo(palavra):
    
    palavra = palavra.lower()
    palavra_invertida = palavra[::-1]
    if palavra == palavra_invertida:
        return True
    else:
        return False
palavra = input("Digite uma palavra para verificar se é um palíndromo: ")

if eh_palindromo(palavra):
    print("A palavra", palavra, "é um palíndromo!")
else:
    print("A palavra", palavra, "não é um palíndromo.")
