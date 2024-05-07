end=True
color='\033[93m'

while(end!=False):
    print(f'''
    {color}      
        
d888888P          dP                dP                   dP                                              dP                dP             
   88             88                88                   88                                              88                88             
   88    .d8888b. 88d888b. .d8888b. 88 .d8888b.    .d888b88 .d8888b.    dP   .dP .d8888b. 88d888b. .d888b88 .d8888b. .d888b88 .d8888b.    
   88    88'  `88 88'  `88 88ooood8 88 88'  `88    88'  `88 88'  `88    88   d8' 88ooood8 88'  `88 88'  `88 88'  `88 88'  `88 88ooood8    
   88    88.  .88 88.  .88 88.  ... 88 88.  .88    88.  .88 88.  .88    88 .88'  88.  ... 88       88.  .88 88.  .88 88.  .88 88.  ...    
   dP    `88888P8 88Y8888' `88888P' dP `88888P8    `88888P8 `88888P8    8888P'   `88888P' dP       `88888P8 `88888P8 `88888P8 `88888P'   
                                                                                                                                      Aline Technology Corporation
''')
    try:
        p=int(input("Insira o valor de P: "))
        if (p == 1 or p == 2 or p == 3 or p == 4 or p == 5 or p == 6 or p == 7 or p == 8 or p == 9 or p == 10):
           print("O valor inserido não é válido! tente novamente.")

        P = input("Digite 'F' para Falso ou 'V' para Verdadeiro para P: ").upper()
        Q = input("Digite 'F' para Falso ou 'V' para Verdadeiro para Q: ").upper()
        R = input("Digite 'F' para Falso ou 'V' para Verdadeiro para R: ").upper()

        #verificar se o usuario digitou o que foi pedido
        if P not in ('F', 'V') or Q not in ('F', 'V') or R not in ('F', 'V'):
            print("Entrada inválida. Tente digitar  'F' ou 'V' somente .")
        else:
            #agora a operação lógica que o usuario quer
            ope =  input("Qual operação logica você deseja fazer 'and' ou 'or': ").lower()


        #vamos verificar a consistencia das operções
        if ope not in ('and' or 'or'):
            print("operação invalida, escolha entre 'and' ou 'or': ")
    
    
        # Realiza a operação lógica
        if ope == 'and':
            resultado = (P == 'V') and (Q == 'V') and (R == 'V')
        else:
            resultado = (P == 'V') or (Q == 'V') or (R == 'V')

        # Exibe o resultado
        print(f"O resultado da operação {ope} entre P={P}, Q={Q} e R={R} é {resultado}.")

    except ValueError:
        print("O valor inserido não é válido! tente novamente.")
    except:
        print("Algo deu errado! tente novamente")
    else:
        res=input("Deseja Continuar ? Y OR N")
        if(res=='y' or res=='Y'):
            end=True
        elif(res=='n' or res=='N'):
            end=False


    