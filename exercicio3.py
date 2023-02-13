#  Se achar necessario, faça import de outras bibliotecas





# Crie a função que será avaliada no exercício aqui
def soma_dos_aninhados(lista : list):
    nova_lista = []
    for sublista in lista:
        soma = 0
        for numero in sublista:
            soma += numero
        nova_lista.append(soma)
    return nova_lista



lista = [[11, 22], [33], [44, 55, 66]]
outra_lista = [[1, 2, 3, 4], [3, 3], [4, 6]]

resultado1=soma_dos_aninhados(lista)
resultado2=soma_dos_aninhados(outra_lista)
soma=0
soma2=0
for i in resultado1:
    soma=i+soma

for i2 in resultado2:
    soma2=i2+soma2


print(lista)
print(outra_lista)
print(soma)
print(soma2)








# Teste a sua função aqui (caso ache necessário)











