num1= int(input("Entre com o primeiro numero: "))
num2= int(input("Entre com o segundo numero: "))

operacao = input("Escolha a operação (+, -, *, /): ")

if operacao == "+":
    print(num1 + num2)
elif operacao == "-":
    print(abs(num1 - num2))
elif operacao == "*":
    print(num1 * num2)
elif operacao == "/":
    if num2 != 0:
        print(num1 / num2)
    else:
        print("Não é possível dividir por zero!")
else:
    print("Operação inválida!")        


