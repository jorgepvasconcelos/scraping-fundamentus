import json

import pandas

from src.fundamentus_scraping import get_acoes, get_fiis
from src.transform import transform_values
from src.utils import create_dirs


def acoes():
    data = get_acoes()
    data = transform_values(data_list=data)

    with open('json/acoes.json', 'w') as file:
        json.dump(data, file, indent=2)

    df = pandas.DataFrame(data)
    df.to_excel('excel/acoes.xlsx', index=False)


def fiis():
    data = get_fiis()
    data = transform_values(data_list=data)

    with open('json/fiis.json', 'w') as file:
        json.dump(data, file, indent=2)

    df = pandas.DataFrame(data)
    df.to_excel('excel/fiis.xlsx', index=False)


if __name__ == '__main__':
    create_dirs()

    fiis()
    acoes()
