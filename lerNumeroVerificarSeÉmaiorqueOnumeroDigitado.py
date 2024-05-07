#Programador Gustavo Rodrigues
#data:26/09/2023

try:
    i=1
    num=int(input("Digite um número"))
except ValueError:
    print("DIGITA UM NÚMERO CABAÇO")
else:
    if num>1:
        for i in range(i,num+1,1):
            print(i)
    else:
        for i in range(num,i+1,1):
            print(i)
