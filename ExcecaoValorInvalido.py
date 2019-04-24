

def input_float(msg):
    while True: # enquanto for verdadeiro o codgigo abaixo tem q ser executado
        try:
            return float(input(msg)) # convertendo o valor para float
        except ValueError: # caso o numero não seja valido ira chamar essa except
            print("Número invalido.")

num1 = input_float("Digite o primeiro numero .:")
num2 = input_float("Digite o Segundo numero .:")

try:
    print(num1/num2)
except ZeroDivisionError: #caso o numero tenha q ser dividido por zero
    print("Não é possivel dividir o número por zero.")
