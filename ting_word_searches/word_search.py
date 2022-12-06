def exists_word(word, instance):
    arr = list()

    for file in instance.__str__():
        arr.append({
            'palavra': word,
            'arquivo': file['nome_do_arquivo'],
            'ocorrencias': []
        })

        lines = file['linhas_do_arquivo']
        for n in range(len(lines)):
            if word.lower() in lines[n].lower():
                arr[0]['ocorrencias'].append({'linha': n+1})

    return arr if len(arr[0]['ocorrencias']) > 0 else []


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
