from __future__ import annotations

import os
import json

import pandas


def create_dirs():
    dir_name = ['excel', 'json']
    for name in dir_name:
        if not os.path.exists(f'./{name}'):
            os.mkdir(f'{name}')


def create_excel(data: dict | list, file_name: str):
    df = pandas.DataFrame(data)
    df.to_excel(f'excel/{file_name}.xlsx', index=False)


def create_json(data: dict | list, file_name: str):
    with open(f'json/{file_name}.json', 'w') as file:
        json.dump(data, file, indent=2)


def somente_acoes(codigos: list):
    codigos_validos = []
    for codigo in codigos:
        if codigo[-1].isnumeric():
            codigos_validos.append(codigo)
    return codigos_validos
