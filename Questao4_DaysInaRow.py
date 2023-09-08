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
    {'Date': '2020-02-01', 'account_id': 'A2', 'User_id': 'U5'}
]

# Função para converter uma data no formato 'YYYY-MM-DD' para um número inteiro (YYYYMMDD)
def data_para_inteiro(data):
    partes = data.split('-')
    return int(partes[0] + partes[1] + partes[2])

# Ordenar a lista por datas (usando a função de conversão)
listaOrdenada = sorted(lista, key=lambda item: data_para_inteiro(item['Date']))

# Inicializar um dicionário para rastrear os usuários ativos por data
usuarios_ativos_por_data = defaultdict(set)

# Encontrar usuários ativos por três dias consecutivos
usuarios_ativos_por_tres_dias = set()

for item in listaOrdenada:
    data = item['Date']
    usuario = item['User_id']
    
    # Adicionar o usuário à lista de usuários ativos para a data atual
    usuarios_ativos_por_data[data].add(usuario)
    
    # Verificar se os usuários estão ativos em três datas consecutivas
    if len(usuarios_ativos_por_data[data]) == 1:
        data_anterior = data
    elif len(usuarios_ativos_por_data[data]) == 2:
        if data_para_inteiro(data) - data_para_inteiro(data_anterior) == 1:
            usuarios_ativos_por_tres_dias.update(usuarios_ativos_por_data[data])

print("Usuários ativos por três dias consecutivos:")
print(usuarios_ativos_por_tres_dias)
