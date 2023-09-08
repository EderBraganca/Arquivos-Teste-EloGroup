listaFuncionarios = [
    {'id': 1, 'salary': 100000},
    {'id': 2, 'salary': 80000},
    {'id': 4, 'salary': 500000},
    {'id': 5, 'salary': 500000},
    {'id': 6, 'salary': 200000},
    {'id': 7, 'salary': 75000},
    {'id': 8, 'salary': 90000}
]

listaCargos = [
    {'id': 1, 'cargo': 'gerente'},
    {'id': 2, 'cargo': 'executivo'},
    {'id': 8, 'cargo': 'executivo'},
    {'id': 5, 'cargo': 'gerente'},
    {'id': 4, 'cargo': 'gerenteAss'},
    {'id': 7, 'cargo': 'gerentePj'},
    {'id': 6, 'cargo': 'lider'},
]

# Crie um dicionário para mapear cada cargo para a soma dos salários dos funcionários
somaSalariosPorCargo = {}

for funcionario in listaFuncionarios:
    salario = funcionario['salary']
    for cargo in listaCargos:
        if cargo['id'] == funcionario['id']:
            nome_cargo = cargo['cargo']
            if nome_cargo not in somaSalariosPorCargo:
                somaSalariosPorCargo[nome_cargo] = 0
            somaSalariosPorCargo[nome_cargo] += salario

# Encontre os dois salários mais altos
salarios_unicos = list(set(somaSalariosPorCargo.values()))
salarios_unicos.sort(reverse=True)
salarios_mais_altos = salarios_unicos[:2]

# Encontre todos os cargos com os salários mais altos
cargos_com_salarios_mais_altos = [cargo for cargo, salario in somaSalariosPorCargo.items() if salario in salarios_mais_altos]

print(f'Os dois cargos com os salários mais altos são: {", ".join(cargos_com_salarios_mais_altos)} com um total de salários de {salarios_mais_altos[0]} e {salarios_mais_altos[1]}.')
