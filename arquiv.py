"""
O modulo arquiv.py providência funções auxiliares para o programa de Ordenação
Externa, realizando a manipulação dos arquivos externos, tais como: criar, ler e escrever.
"""

def input_generator(num_elements: int, output: str, name: str = 'input', minNum: int = 0, maxNum: int = 100):
    """
    Cria um arquivo de entrada com elementos aleatórios

    Example:
        input_generator(100, 'D:\\', maxNum=100)

        Arquivo de saida:
        5
        23
        42
        ...

    Args:
        num_elements: numero todal de registros a serem criados
        output: Caminho onde o arquivo sera criado
        name (optional): Nome do arquivo
        minNum (optional): Menor elemento (inclusivo)
        maxNum (optional): Maior elemento (inclusivo)
    """
    import random 

    filePath = f"{output}{name}.txt"
    arquivo = open(filePath, 'w')
    for x in range(num_elements):
        i = random.randint(minNum,maxNum)
        arquivo.write("%d\n" % i)
    arquivo.close()


def fita_generator(num_fitas: int, output: str, name: str = 'fita') -> list:
    """
    Cria arquivos auxiliares para a funcao de ordenacao externa

    Args:
        num_fitas: numero de arquivos a serem criados
        output: Caminho onde o arquivo sera criado
        name (optional): Nome do arquivo

    Returns:
        Uma lista de arquivos abertos
    """
    files = list()
    for n in range(num_fitas):
        filePath = f"{output}{name}{str(n + 1)}.txt"
        arquivo = open(filePath, 'w')
        files.append(arquivo)
    return files


def fita_closer(fitas: list):
    """
    Fecha todos os arquivos que estao armazenados em uma lista
    """
    try:
        for f in fitas:
            f.close()
    except AttributeError:
        print("ERROR: Um elemento da lista não é um arquivo.")
