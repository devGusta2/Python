#Programador Gustavo Rodrigues
#data:26/09/2023
#programa para mostrar o intervalo do numero digitado



try:
    i=0
    num=int(input("Digite um número maior que 1"))

except  ValueError:
    
        print("O usua50rio não digitou um número! CABAÇO")
else:
    if(num>=1):
        for i in range(i,num+1,1):
            print(i)
