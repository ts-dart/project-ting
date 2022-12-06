import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    list = txt_importer(path_file)
    repeated = False

    for data in instance.__str__():
        if data['nome_do_arquivo'] == path_file:
            repeated = True

    if not repeated:
        dict = {
            'nome_do_arquivo': path_file,
            'qtd_linhas': len(list),
            'linhas_do_arquivo': list
        }

        instance.enqueue(dict)
        print(str(dict))
        sys.stderr.write(str(dict))


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
