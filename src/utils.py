from __future__ import annotations

import os
import json
from pathlib import Path

import pandas


def create_dirs():
    dir_name = ['excel', 'json']
    for name in dir_name:
        destine_path = f'../{name}'
        if not os.path.exists(destine_path):
            Path(destine_path).mkdir(exist_ok=True)


def create_excel(data: dict | list, file_name: str):
    df = pandas.DataFrame(data)
    path = f'../excel/{file_name}.xlsx'
    df.to_excel(path, index=False)


def create_json(data: dict | list, file_name: str):
    path = f'../json/{file_name}.json'
    with open(path, 'w') as file:
        json.dump(data, file, indent=2)


def somente_acoes(codigos: list):
    codigos_validos = []
    for codigo in codigos:
        if codigo[-1].isnumeric():
            codigos_validos.append(codigo)
    return codigos_validos
