import sys


def txt_importer(path_file):
    p = path_file

    if f'{p[len(p) - 3]}{p[len(p) - 2]}{p[len(p) - 1]}' != 'txt':
        sys.stderr.write('Formato inválido\n')

    try:
        with open(p, mode='r') as file:
            content = file.read()
            return content.split('\n')
    except FileNotFoundError:
        sys.stderr.write(f'Arquivo {p} não encontrado\n')
