#Programadores: Aline Gonçalves e Gustavo Rodrigues
#data:30/09/2023
#Programa para calcular o preço a pagar pelo fornecimento de energia

end=False
#cores
color='\033[94m'
colorVerde='\033[92m'
colorWarning='\033[91m'
colorMain='\033[95m'
consumo=0
while(end!=True):
    try:
        print(f'''{color} 
,-----.       ,--.             ,--.           ,--.                                ,--.        ,--.         ,--.               
'  .--./,--,--.|  |,---.,--.,--.|  | ,--,--. ,-|  | ,---. ,--.--.,--,--.     ,---. |  |,---. ,-'  '-.,--.--.`--' ,---. ,--,--. 
|  |   ' ,-.  ||  | .--'|  ||  ||  |' ,-.  |' .-. || .-. ||  .--' ,-.  |    | .-. :|  | .-. :'-.  .-'|  .--',--.| .--'' ,-.  | 
'  '--'\ '-'  ||  \ `--.'  ''  '|  |\ '-'  |\ `-' |' '-' '|  |  \ '-'  |    \   --.|  \   --.  |  |  |  |   |  |\ `--.\ '-'  | 
 `-----'`--`--'`--'`---' `----' `--' `--`--' `---'  `---' `--'   `--`--'     `----'`--'`----'  `--'  `--'   `--' `---' `--`--' 
                                                                                                                               ''')
        #recebe a quantidade de kWh 
        kwh=float(input(f"{colorMain}Digite a quantidade de kWh: "))
        #recebe o tipo de instação, se é Residência, Indústria ou Comércio
        tipoInstalacao=input("Digite o tipo de instalação, R (Residência) I(Indútrias) C (Comércio): ")
        #verifica valor digitado pelo usuario
        if(tipoInstalacao=='R' or tipoInstalacao=='r' or tipoInstalacao=='I' or tipoInstalacao=='i' or tipoInstalacao=='C'or tipoInstalacao=='c'):
            #verifica se o usuário optou por Residência
            if(tipoInstalacao=='R' or tipoInstalacao == 'r'):
                
                if(kwh<=500):
                    consumo=kwh*0.40  
                    print(f"{colorVerde}O preço por kWh é de R$0,40 portanto o valor a pagar é de: {consumo} R$")
                else:
                    consumo=kwh*0.65
                    print(f"{colorWarning}O preço por kWh é de R$0,65 portanto o valor a pagar é de: {consumo}R$")
            #verficia se o usuário optou por Comércio
            elif(tipoInstalacao=='C' or tipoInstalacao == 'c'):
                if(kwh<=1000):
                    consumo=kwh*0.55
                    print(f"{colorVerde}O preço por kWh é de R$0,55 portanto o valor a pagar é de: {consumo}R$")
                else:
                    consumo=kwh*0.60
                    print(f"{colorWarning}O preço por kWh é de R$0,60 portanto o valor a pagar é de: {consumo}R$")
            #verifica se o usuário optou por Indústria
            elif(tipoInstalacao=='I' or tipoInstalacao == 'i'):
                if(kwh<=5000):
                    consumo=kwh*0.55
                    print(f"{colorVerde}O preço por kWh é de R$0,55 portanto o valor a pagar é de: {consumo}R$")
                else:
                    consumo=kwh*0.60  
                    print(f"{colorWarning}O preço por kWh é de R$0,60 portanto o valor a pagar é de: {consumo}R$")
        else:
            #informa ao usuário que o valor informado não é válido
            print("O valor informado não corresponde como Residência Indústria ou Comércio")
    except ValueError:
        print("O valor inserido não é invalido")
    except:
        print("Oops! Algo deu errado, tente novamente mais tarde!")
    else:
        #verifica se o usuario deseja continuar calculando
        res=input(f"{colorVerde}Deseja calcular novamente? SIM ou NAO")
        if(res=='s' or res=='S' or res=='SIM' or res=='sim'):
            end=end
        elif(res=='n' or res=='N' or res=='NAO' or res=='nao'):
            end=True
        else:
            break

