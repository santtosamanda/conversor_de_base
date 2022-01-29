def binario():
    print(f"\nO numero {numero} em base BINÁRIA é: {bin(numero)[2:]}")


def octal():
    print(f"\nO numero {numero} em base OCTAL é: {oct(numero)[2:]}")


def hexadecimal():
    print(f"\nO numero {numero} em base HEXADECIMAL é: {hex(numero)[2:]}")


def default():
    print("Alternativa inválida")


def opcao(argumento):
    alternativas = {
        1: binario,
        2: octal,
        3: hexadecimal,
    }
    return alternativas.get(argumento, "\nAlternativa inválida")


numero = int(input("Digite o número que deseja fazer a conversão: "))
base = int(input("""\nDeseja converter para qual base númerica?
[1] para binário
[2] para octal
[3] hexadecimal\n\nInforme sua opção: """))

if base in [1, 2, 3]:
    chamar_funcao = opcao(base)
    chamar_funcao()
else:
    print("\nAlternativa inválida")
