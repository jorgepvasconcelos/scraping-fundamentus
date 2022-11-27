from src.collect import acoes_table, fiis_table, todos_os_codigos, acoes_rendimentos
from src.utils import create_dirs


def main():
    create_dirs()

    acoes_table_data = acoes_table()
    fiis_table_data = fiis_table()
    codigos = todos_os_codigos(acoes_table_data, fiis_table_data)
    return print('ddddddddddd')
    acoes_rendimentos_date = acoes_rendimentos(codigos)


if __name__ == '__main__':
    main()
