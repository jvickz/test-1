def leia(mensagem):
    return float(input(mensagem))


def calcular_resto_divisao():
    # Lê os dois números usando a função leia
    num1 = leia("Digite o primeiro número: ")
    num2 = leia("Digite o segundo número: ")

    # Calcula o resto da divisão
    resto = num1 % num2

    # Exibe o resultado
    print(f"O resto da divisão de {num1} por {num2} é: {resto}")


# Executa a função
calcular_resto_divisao()10
101
40
