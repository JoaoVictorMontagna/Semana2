#  Se achar necessario, faça import de outras bibliotecas





# Crie a função que será avaliada no exercício aqui

nmr1=input("Digite primeiro numero: ")
nmr2=input("Digite segundo numero: ")

def multiplas_operacoes(a,b):
    soma=float(a)+float(b)
    subtracao=float(a)-float(b)
    multiplicacao=float(a)*float(b)

    print("Seu primeiro numero é: " + str(a) )
    print("Seu segundo numero é: " + str(b) )
    print(str(a)+" + " + str(b) + " = " + str(soma))
    print(str(a)+" - " + str(b) + " = " + str(subtracao))
    print(str(a)+" * " + str(b) + " = " + str(multiplicacao))
    if float(b)==0 or float(a)==0:
        print("toda divisão por 0 = 0 ")
    else:
        divisao=float(a)/float(b)
        print(str(a)+" / " + str(b) + " = " + str(divisao))

print(multiplas_operacoes(nmr1,nmr2))




# Teste a sua função aqui (caso ache necessário)











