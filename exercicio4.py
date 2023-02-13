#  Se achar necessario, faça import de outras bibliotecas





# Crie a função que será avaliada no exercício aqui


palavras=[1,2,2,3,"oi","ola","ola"]

def tem_duplicados (lista:list):
    nr=[]
    for i in lista:
        if lista.count(i)>1:
            nr.append(i)

    novalista=set(nr)
    tamanhoDaLista=len(novalista)

    print(str(tamanhoDaLista) + " valores repetidos encontrados: " + str(novalista))

print(tem_duplicados (palavras))



# Teste a sua função aqui (caso ache necessário)











