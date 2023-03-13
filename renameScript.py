from datetime import date
import os
# importa a biblioteca

src = 'img.jpg'
# nome do arquivo original (na mesma pasta deste script)

data_atual = date.today()
# buscar data atual

data_semespacos = str(data_atual).replace("-", "")
# remover espaços para renomear arquivo corretamente

continuar = 1
cont = 0

while True:
    cont += 1
    id_placa = input('Qual o número da placa? ')

    tipo_bicho = int(input('\nQual das opcoes corresponde a foto tirada? \n 1- Afídeo \n 2- Parasitoide \n'))

    if (tipo_bicho == 1):
        animal = 'afideo'
    elif (tipo_bicho == 2):
        animal = 'parasitoide'
    else:
        print('Erro! Opcao invalida!')
        continue

    dest = ' '

    dest = data_semespacos + '_' + id_placa + '_' + animal + '.jpg'
    # nome desejado para o arquivo

    os.rename(src, dest)
    # renomeação do arquivo

    print("Arquivo " + str(cont) + " renomeado!")

    while True:
        continuar = input('\nDeseja tirar mais fotos? \n 1- Sim \n 2- Nao \n')
        if (int(continuar) == 1 or int(continuar) == 2):
            break
        #sai do loop para verificar se deseja tirar mais fotos, ou não
        else:
            print('Valor invalido')

    if int(continuar) == 2:
        break
    #sai do loop principal

print ('\n\nPrograma encerrado com sucesso!')

            


