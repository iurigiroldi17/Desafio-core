num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

print("Escolha a operação:")
print("1 - Adição")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

opcao = input("Digite a opção: ")

if opcao == "1":
    resultado = num1 + num2
elif opcao == "2":
    resultado = num1 - num2
elif opcao == "3":
    resultado = num1 * num2
elif opcao == "4":
    if num2 != 0:
        resultado = num1 / num2
    else:
        resultado = "Erro: divisão por zero!"
else:
    resultado = "Opção inválida!"

print("Resultado:", resultado)