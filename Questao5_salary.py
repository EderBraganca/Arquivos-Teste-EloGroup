listaFuncionarios = [
    {'id': 1, 'salary': 100000},
    {'id': 2, 'salary': 80000},
    {'id': 4, 'salary': 500000},
    {'id': 5, 'salary': 500000},
    {'id': 6, 'salary': 200000},
    {'id': 7, 'salary': 75000},
    {'id': 8, 'salary': 90000}]

listaCargos = [
    {'id': 1, 'cargo': 'gerente'},
    {'id': 2, 'cargo': 'executivo'},
    {'id': 8, 'cargo': 'executivo'},
    {'id': 5, 'cargo': 'gerente'},
    {'id': 4, 'cargo': 'gerenteAss'},
    {'id': 7, 'cargo': 'gerentePj'},
    {'id': 6, 'cargo': 'lider'}]

somaSalarios = {}

for funcionario in listaFuncionarios:
    salario = funcionario['salary']
    for cargo in listaCargos:
        if cargo['id'] == funcionario['id']:
            nome = cargo['cargo']
            if nome not in somaSalarios:
                somaSalarios[nome] = 0
            somaSalarios[nome] += salario

somaSalarios = dict(sorted(somaSalarios.items(), key=lambda item: item[1], reverse= True))
print(somaSalarios)

