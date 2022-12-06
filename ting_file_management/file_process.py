import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    list = txt_importer(path_file)
    repeat = False

    for data in instance.__str__():
        if data['nome_do_arquivo'] == path_file:
            repeat = True

    if not repeat:
        dict = {
            'nome_do_arquivo': path_file,
            'qtd_linhas': len(list),
            'linhas_do_arquivo': list
        }

        instance.enqueue(dict)
        sys.stdout.write(str(dict))


def remove(instance):
    if len(instance.__str__()) <= 0:
        print('Não há elementos')
        return 0

    path_file = instance.dequeue()['nome_do_arquivo']
    print(f'Arquivo {path_file} removido com sucesso')


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
