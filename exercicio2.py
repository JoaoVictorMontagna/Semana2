#  Se achar necessario, faça import de outras bibliotecas





# Crie a função que será avaliada no exercício aqui
lista=[1,2,3,4]

def cumulativa(lista : list):
    nova_lista = []
    for i in range(len(lista)):
        soma = 0
        for n in range(i+1):
            soma += lista[n]
        nova_lista.append(soma)
    return nova_lista

print(lista)
print(cumulativa(lista))







# Teste a sua função aqui (caso ache necessário)











