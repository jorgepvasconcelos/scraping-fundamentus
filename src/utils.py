import os


def create_dirs():
    if not os.path.exists('./json'):
        os.mkdir('json')

    if not os.path.exists('./excel'):
        os.mkdir('excel')
