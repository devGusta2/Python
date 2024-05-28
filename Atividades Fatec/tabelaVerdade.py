end=True
color='\033[93m'
Fim = '\033[0m'

# Cores e Formatos
Verde = '\033[92m'
Amarelo = '\033[93m'
Vermelho = '\033[91m'
Azul = '\033[94m'
Bold='\033[1m'
Fim = '\033[0m'
rosa='\033[95m'

# Inicializando Variáveis
Var_Up=0.00
A=''
#

while(end!=False):
    print(f'''
    {rosa}      
        
d888888P          dP                dP                   dP                                              dP                dP             
   88             88                88                   88                                              88                88             
   88    .d8888b. 88d888b. .d8888b. 88 .d8888b.    .d888b88 .d8888b.    dP   .dP .d8888b. 88d888b. .d888b88 .d8888b. .d888b88 .d8888b.    
   88    88'  `88 88'  `88 88ooood8 88 88'  `88    88'  `88 88'  `88    88   d8' 88ooood8 88'  `88 88'  `88 88'  `88 88'  `88 88ooood8    
   88    88.  .88 88.  .88 88.  ... 88 88.  .88    88.  .88 88.  .88    88 .88'  88.  ... 88       88.  .88 88.  .88 88.  .88 88.  ...    
   dP    `88888P8 88Y8888' `88888P' dP `88888P8    `88888P8 `88888P8    8888P'   `88888P' dP       `88888P8 `88888P8 `88888P8 `88888P'   
                                                                                                                                      
''')
    try:

        P = input(f"{Vermelho}Digite 'F' para atribuir Falso ou 'V' para atribuir Verdadeiro ao elemento P: ").upper()
        Q = input("Digite 'F' para atribuir Falso ou 'V' para atribuir Verdadeiro ao elemento Q: ").upper()
        R = input("Digite 'F' para atribuir Falso ou 'V' para atribuir Verdadeiro ao elemento  R: ").upper()
        print("\n")
        #verificar se o usuario digitou o que foi pedido
        if P not in ('F', 'V') or Q not in ('F', 'V') or R not in ('F', 'V'):
            print("Entrada inválida. Tente digitar  'F' ou 'V' somente .")
            print("\n")
        else:
            #agora a operação lógica que o usuario quer
            op =  input(f"{Azul}Qual operação logica você deseja fazer 'and' ou 'or': ").lower()
            print("\n")


        #vamos verificar a consistencia das operções
        if op not in ('and' or 'or'):
            print("operação inválida, escolha entre 'and' ou 'or': ")
            print("\n")
    
    
        # Realiza a operação lógica
        if op == 'and':
            resultado = (P == 'V') and (Q == 'V') and (R == 'V')
            print("\n")
        else:
            resultado = (P == 'V') or (Q == 'V') or (R == 'V')
            print("\n")

        # Exibe o resultado
        print(f'{Verde}{A:-^32}')
        print(f"{Verde}| {Bold} {Verde}  P   and  Q  and R  = {resultado} {Fim}{Verde}|")
        print(f'{Verde}{A:-^32}')
        print("\n")
    except ValueError:
        print("O valor inserido não é válido! tente novamente.")
    except:
        print("Algo deu errado! tente novamente")
    else:
        res=input(f"{Amarelo}Deseja Continuar ? Y OR N")
        if(res=='y' or res=='Y: '):
            end=True
        elif(res=='n' or res=='N :'):
            end=False