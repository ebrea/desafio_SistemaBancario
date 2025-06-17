#------------------  Eliminando espaços em branco --------------
# curso= "   Python     "
# print(curso.strip())        # "Python"
# print(curso.lstrip())       # "Python     "
# print(curso.rstrip())       # "   Python"

#------------------  Junções e Centralizações --------------
# curso= "Python"
# print(curso.center(12, "#"))    ###Python###
# print(".".join(curso))          # P.y.t.h.o.n

#------------------  Interpolaçãode variáveis --------------
# forma não recomendada       %s = string    %d = int     %f = float
# nome= 'Ruben'; idade= 25; materia= "História"; nota= 8.5
#
# print("Nome: %s / Idade: %d anos / Disciplina: %s / Nota: %f" % (nome, idade, materia, nota))
#
# print('Nome: {} / idade: {} anos / Disciplina: {} / Nota: {}'.format(nome, idade, materia, nota))
#
# print('Nome: {1} / idade: {0} anos / Disciplina: {3} / Nota: {2}'.format(idade, nome, nota, materia))
#
# print('Posso repetir dados. Ex: Nome = {0} / Disciplina = {2} ou Matéria = {2}'.format(nome, idade, materia, nota))
#
# print('Nome: {n} / idade: {i} anos / Disciplina: {m} / Nota: {x}'.format(n=nome, i=idade, m=materia, x=nota))
#
# print('Nome: {n} / idade: {i} anos / Disciplina: {m} / Nota: {x}'.format(n=nome, i=idade, m=materia, x=nota))
#
# dados = {'nome':'Maria', 'idade': 19}
# print('Nome: {nome} / idade: {idade} anos'.format(**dados))
#
# print(f'Nome={nome} / Idade={idade} / Disciplina={materia} / Nota={nota:8.3f}')
#                                                        # :8.3f = total de 8 carcteres com 3 casas após a vírgula
#                                                        # :.2f = apenas 2 casas após a vírgula

#------------------  Fatiamento --------------
print()
       # 012345678901234567890123456
frase = 'Confie_no_Senhor_e_anima-te'
print(len(frase))       # 27   => de 0 a 26
print(frase[0])         # C
print(frase[:9])        # Confie_no  => 9 primeiras (até a poisção 8)
print(frase[10:])       # Senhor_e_anima-te  => inicia na posição 10
print(frase[10:16])     # Senhor   ( da posição 10 a 15)
print(frase[10:16:2])   # Sno      (pula de 2 em 2)
print(frase[:])         # Confie_no_Senhor_e_anima-te   => a frase toda
print(frase[::-1])      # et-amina_e_rohneS_on_eifnoC   => ao contrário
print(frase[19:-3])     # anima   => da posição 13 até a -3 (não conta esta)
print(frase[10:-11])    # Senhor

s = "abcdef"
s = s[:3] + "XYZ" + s[4:]
print(s)