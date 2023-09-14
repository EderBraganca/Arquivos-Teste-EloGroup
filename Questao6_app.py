#Desenvolva um código em python para comparar as 
#taxas de retenção em janeiro de 2023 com as de dezembro de 2022. 
#A taxa de retenção é definida como a porcentagem de colaboradores que uma empresa 
#retém durante um determinado período de tempo, baseando-se nos dados. 

from collections import defaultdict

lista = [
    {'Date': '2023-01-01','account_id': 'A1', 'User_id': 'U1'},
    {'Date': '2023-01-01','account_id': 'A1', 'User_id': 'U2'},
    {'Date': '2023-01-06','account_id': 'A1', 'User_id': 'U3'},
    {'Date': '2023-01-02','account_id': 'A1', 'User_id': 'U1'},
    {'Date': '2022-12-24','account_id': 'A1', 'User_id': 'U2'},
    {'Date': '2022-12-08','account_id': 'A1', 'User_id': 'U1'},
    {'Date': '2022-12-09','account_id': 'A1', 'User_id': 'U1'},
    {'Date': '2023-01-10','account_id': 'A2', 'User_id': 'U4'},
    {'Date': '2023-01-11','account_id': 'A2', 'User_id': 'U4'},
    {'Date': '2023-01-12','account_id': 'A2', 'User_id': 'U4'},
    {'Date': '2023-01-15','account_id': 'A2', 'User_id': 'U5'},
    {'Date': '2022-12-17','account_id': 'A2', 'User_id': 'U4'},
    {'Date': '2022-12-25','account_id': 'A3', 'User_id': 'U6'},
    {'Date': '2022-12-25','account_id': 'A3', 'User_id': 'U6'},
    {'Date': '2022-12-25','account_id': 'A3', 'User_id': 'U6'},
    {'Date': '2022-12-06','account_id': 'A3', 'User_id': 'U7'},
    {'Date': '2022-12-06','account_id': 'A3', 'User_id': 'U6'},
    {'Date': '2023-01-14','account_id': 'A4', 'User_id': 'U6'},
    {'Date': '2023-02-07','account_id': 'A1', 'User_id': 'U1'},
    {'Date': '2023-02-10','account_id': 'A1', 'User_id': 'U2'},
    {'Date': '2023-02-01','account_id': 'A4', 'User_id': 'U4'},
    {'Date': '2023-02-01','account_id': 'A2', 'User_id': 'U5'},
    {'Date': '2022-12-05','account_id': 'A2', 'User_id': 'U8'}]

colabDez = defaultdict(set)
colabJan = defaultdict(set)
 
for item in lista:
    data = item['Date']
    account_id = item['account_id']
    user_id = item['User_id']
    
    if data.startswith('2022-12'):
        colabDez[account_id].add(user_id)
    elif data.startswith('2023-01'):
        colabJan[account_id].add(user_id)

taxas_de_retencao = {}
for account_id in colabDez:  
    taxas_de_retencao[account_id] = len(colabJan[account_id]) / len(colabDez[account_id])

print(taxas_de_retencao)