x = 22
x %= 4   # Resto da divisão
print(x)    # 2

y = 8
y **= 2     # a = 8 ** 2
print(y,'\n')    # 64

saldo = 1000
saque = 200
limite = 100

print(saldo >= saque)   # True
print(saldo >= saque and saque <= limite)   # False
print(saldo < saque or saque >= limite, '\n')    # True

# AND = para ser True tudo tem que ser True
# OR= para ser Tre apenas 1 tem que ser True

print(not 1000 > 1500)  # True
lista = []
print(not lista)        # True     => lista vazia é falsa
print(not "tem texto")  # False    => tem texto, portanto a negação é falsa
print(not "", '\n')           # True     => sem espaços é vazio

print(True and True)    # True
print(True and False)   # False
print(True or True)     # True
print(True or False, '\n')    # True

curso = "Curso de Python"
nome_curso = curso
saldo, limite = 200, 200     # mesmo que: saldo = limite = 200
print(curso is not nome_curso)  # False
print (saldo is limite, '\n')   # True

curso = "Curso de Python"
frutas = ["laranja", "uva", "limão"]
saques = [1500, 100]
print("Python" in curso)        # True
print("maçã" not in frutas)     # True
print (200 in saques)           # False


