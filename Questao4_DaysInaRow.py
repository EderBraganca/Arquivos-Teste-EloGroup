from collections import defaultdict

lista = [
    {'Date': '2020-12-06', 'account_id': 'A1', 'User_id': 'U1'},
    {'Date': '2021-01-15', 'account_id': 'A1', 'User_id': 'U2'},
    {'Date': '2021-01-06', 'account_id': 'A1', 'User_id': 'U3'},
    {'Date': '2021-01-02', 'account_id': 'A1', 'User_id': 'U1'},
    {'Date': '2020-12-24', 'account_id': 'A1', 'User_id': 'U2'},
    {'Date': '2020-12-08', 'account_id': 'A1', 'User_id': 'U1'},
    {'Date': '2020-12-09', 'account_id': 'A1', 'User_id': 'U1'},
    {'Date': '2021-01-10', 'account_id': 'A2', 'User_id': 'U4'},
    {'Date': '2021-01-11', 'account_id': 'A2', 'User_id': 'U4'},
    {'Date': '2021-01-12', 'account_id': 'A2', 'User_id': 'U4'},
    {'Date': '2021-01-15', 'account_id': 'A2', 'User_id': 'U5'},
    {'Date': '2020-12-17', 'account_id': 'A2', 'User_id': 'U4'},
    {'Date': '2020-12-25', 'account_id': 'A3', 'User_id': 'U6'},
    {'Date': '2020-12-25', 'account_id': 'A3', 'User_id': 'U6'},
    {'Date': '2020-12-25', 'account_id': 'A3', 'User_id': 'U6'},
    {'Date': '2021-01-01', 'account_id': 'A3', 'User_id': 'U7'},
    {'Date': '2020-12-06', 'account_id': 'A3', 'User_id': 'U6'},
    {'Date': '2021-01-14', 'account_id': 'A3', 'User_id': 'U6'},
    {'Date': '2020-02-07', 'account_id': 'A1', 'User_id': 'U1'},
    {'Date': '2020-02-10', 'account_id': 'A1', 'User_id': 'U2'},
    {'Date': '2020-02-01', 'account_id': 'A2', 'User_id': 'U4'},
    {'Date': '2020-02-01', 'account_id': 'A2', 'User_id': 'U5'}]

#Converter as datas pra ficar mais facil carregar e ordenar
#ordenar
#iterar sobre as datas, vendo se os usuarios persistem

def dataToInteger(data):
    data = data.split('-')
    return int(data[0] + data[1] + data[2])

listaOrdenada = sorted(lista, key=lambda item: dataToInteger(item['Date']))

def compararData(data1, data2):
    data1Separ = data1.split('-')
    data2Separ = data2.split('-')
    if(int(data2Separ[0]) == int(data1Separ[0])):
        if(int(data1Separ[1]) == int(data2Separ[1])):
            if(int(data1Separ[2]) == (int(data2Separ[2]) - 1)):
                return True
        elif(int(data1Separ[1]) == (int(data2Separ[1]) - 1)):
            if(int(data1Separ[2]) >= 30 and int(data2Separ[2]) == 1):
                return True
        elif(int(data1Separ[1]) == 12 and int(data2Separ[1]) == 1):
            if(int(data1Separ[2]) >= 30 and int(data2Separ[2]) == 1):
                return True
    #Seria implementado, com tempo, o caso de mudar o ano
    return False

usuarios_ativos_por_tres_dias = set()

for i in range(len(listaOrdenada) - 2):
    data1 = listaOrdenada[i]['Date']
    usuario1 = listaOrdenada[i]['User_id']

    data2 = listaOrdenada[i + 1]['Date']
    usuario2 = listaOrdenada[i + 1]['User_id']

    data3 = listaOrdenada[i + 2]['Date']
    usuario3 = listaOrdenada[i + 2]['User_id']

    if compararData(data1, data2):
        if compararData(data2, data3):
            if usuario1 == usuario2 and usuario2 == usuario3:
                usuarios_ativos_por_tres_dias.add(usuario1)

print(usuarios_ativos_por_tres_dias)
