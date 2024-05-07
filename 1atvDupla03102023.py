#Programadores: Aline Gonçalves e Gustavo Rodrigues
#data:30/09/2023
#Programa para aprovar um empréstimo bancário para comprar um imóvel

end= False
while(end != True):
    try: 
        #recebe o valor total do imóvel que o cliente deseja comprar
        valorImovel= float(input("Digite o valor do Imóvel que deseja comprar: (somente números) "))
        #recebe a quantidade de meses em que o cliente deseja pagar
        qntMeses= int(input("Digite em quantas parcelas deseja pagar: "))
        #recebe o salario total do cliente
        valorSalario= float(input("Digite o seu salário bruto: "))
        #calcula a porcentagem de 30% do salario
        prcntSalario= valorSalario * 0.3
        #calcula o valor de cada prestação
        valorPrest= valorImovel / qntMeses
        #verifica se a quantidade de meses que o usuario digitou está de acordo com o máximo de parcelas possíveis
        if(qntMeses > 240):
            print("O máximo de parcelas disponiveis é 240!")
            break
        else:
            #calcula a quantidade minima  de parcelas e o salario ideal, para quitar a compra
            if(valorPrest > prcntSalario):
              calcValorPorParcela =  valorImovel / qntMeses 
              valorSalarioIdeal = (calcValorPorParcela*100) / 30
              quantMinima = valorImovel / prcntSalario
              
              print(f"Para adiquirir o imóvel pagando em {qntMeses} parcelas, o valor mínimo de seu sálario bruto deve ser de {valorSalarioIdeal}.")
              print(f"Levando em consideração que somente 30% do salário pode ser comprometido na parcela do financiamento, com o sálario bruto de R$ {valorSalario} seriam necessárias {quantMinima} parcelas para quitar um imóvel de R${valorImovel}")
              #informa ao cliente qual é o imóvel sugerido a partida das condições obtidas
              if quantMinima > 240 :
                  imovelSug = prcntSalario * 240
                  print(f"Dessa forma não será possível financiar o imóvel indicado pois a quantidade máxima é de 240 parcelas. Sugerimos que escolha um imóvel de até R$ {imovelSug}")
              break
            else:
                #mostra ao cliente que o imprésimo foi liberado
                print("Seu empréstimo foi liberado!")
                print(f"O valor de cada parcela é:{valorPrest}")
                print(f"O número de vezes é: {qntMeses}")
    except ValueError:
        print("O valor informado é inválido! Tente novamente.")
    else:
        #verifica se o usuario deseja continuar com os cálculos para o impréstimo bancário
        goOn = input("O usuario deseja calcular novamente? ( S para sim, N para não)")
        if goOn == "S" or goOn == "s" or goOn == "SIM" or goOn == "sim": 
            end = False
        else:
            end = True