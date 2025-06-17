
# idade = int(input("Qual a sua idade? : "))
#
# print(f" Você tem {idade} anos, portanto você é", end=" ")
# if idade < 12:
#     print('criança')
#
# elif idade >= 12 and idade < 18:
#         print("um adolescente")
#
# elif idade >= 18 and idade < 30:
#     print("jovem")
#
# elif idade >= 30 and idade < 60:
#     print("adulto")
#
# else:
#     print('idoso')
#
# print(40 * '=') # ===========================================================
#
# texto= input("Informe um texto: ")
# VOGAIS = "AEIOU"
#
# for letra in texto:
#     if letra.upper() in VOGAIS:
#         print(letra, end='-')
# else:
#     print('\nEste "else" é inútil')

#------------------ IF ternário ------------------------------
c1 = ''
c2= 'Condição 2'
print('Imprime isso se satisfazer a Condição 1, ou seja, c1 estar vazio' if not c1 else c2)
#------------------------------------------------------------

n = list(range(6))      # [0, 1, 2, 3]
print(n)

#------------------------------------------------------------

# for i in range(1, 12):
#     if i % 2 == 0:
#         continue  # pula os números pares
#     print(i, end='  ')           # 1 3 5 7 9 11
# print()
#------------------------------------------------------------

# opcao= -1
# while opcao != 0 :
#     opcao = int(input("[1] Sacar \n[2] Extrato\n[0] Sair \n> "))
#
#     if opcao==1:
#         print("Sacando...")
#
#     elif opcao==2:
#         print("Exibindo o extrato...")
#
#     else:
#         print("Opção inexistente")
#
#
# else:
#     print("Obrigado por usar nosso sistema bancário, até logo!")