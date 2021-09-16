# Programa criado para imprimir a Sequencia de Fibonacci:
def main():
   # Entrada do usuario
   fnumero = int(input("Quantos numeros? "))

   # Variaveis dos numeros:
   n1 = 0
   n2 = 1
   contagem = 0

   # Checa se o tipo primitivo esta correto:
   if fnumero <= 0:
      print("Por favor, insira um numero inteiro positivo! :)")

   # Se houver apenas um numero, retorna n1:
   elif fnumero == 1:
      print(f"Sequencia de Fibonacci ate: {fnumero}")
      print(n1)

   # Gera a Sequencia de Fibonacci:
   else:
      print("Sequencia de Fibonacci:")
      # Estrutura condicional que checa se a contagem eh menor ou igual ao numero inserido pelo usuario:
      while contagem <= fnumero:
         print(n1)
         nth = n1 + n2
         # Valores atualizados:
         n1 = n2
         n2 = nth
         contagem += 1

if __name__ == "__main__":
   main()
