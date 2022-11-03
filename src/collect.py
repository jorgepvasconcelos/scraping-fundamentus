from __future__ import annotations

from src.scrapers.rendimentos_acoes import scrape_rendimentos_acoes
from src.scrapers.tables import scrape_acoes_table, scrape_fiis_table
from src.transform import transform_values
from src.utils import create_json, create_excel


def todos_os_codigos(acoes, fiis) -> list[str]:
    file_name = 'todos_os_codigos'

    list_of_data = []
    list_of_data.extend(acoes)
    list_of_data.extend(fiis)

    codigos = [v['CODIGO'] for v in list_of_data]
    create_json(data=codigos, file_name=file_name)
    return codigos


def acoes_table() -> list:
    file_name = 'acoes_table'

    # Extractc
    data = scrape_acoes_table()

    # Transform
    data = transform_values(data_list=data)

    # Load
    create_json(data=data, file_name=file_name)
    create_excel(data=data, file_name=file_name)

    return data


def fiis_table() -> list:
    file_name = 'fiis_table'

    # Extractc
    data = scrape_fiis_table()

    # Transform
    data = transform_values(data_list=data)

    # Load
    create_json(data=data, file_name=file_name)
    create_excel(data=data, file_name=file_name)

    return data


def acoes_rendimentos(codigos : list) -> list:
    file_name = 'acoes_rendimentos'

    # Extractc
    data = scrape_rendimentos_acoes(codigos=codigos)

    # # Transform
    # data = transform_values(data_list=data)
    #
    # # Load
    # create_json(data=data, file_name=file_name)
    # create_excel(data=data, file_name=file_name)

    return data
