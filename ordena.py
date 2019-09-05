"""
O modulo ordena.py possui as funções de ordenação ultilizadas no projeto, tanto a
Interna como a Externa.
"""

def insertion_sort(arr):
    """
    Ordena uma lista homogenea, utilizando Ordenação por Inserção

    Args:
        arr: Uma lista de dados homogeneos
    """
    # Percorre a lista
    for i in range(1, len(arr)):

        #key recebe valor da lista na posição 'i'
        key = arr[i]

        """
        Move os elementos de 'arr[0...i-1]' que são maiores que a 'key'
        para uma posição à frente de sua posição atual
        """
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
        

def f_way_sort(buffer_size: int, input_path: str, output_path: str):
    """
    Funcao de Ordenacao Externa, usando intercalacao de f-Caminhos.
    O algoritmo pega todas as entradas de arquivos e gera um arquivo
    de saida com todos os dados dos arquivos anteriores porem ordenados. 

    Os arquivos de entrada devem ter cada registro em uma linha,
    e o arquivo de saida possui uma única linha de registros com
    cada registro separado por uma ' , '.

    Example:
        Arquivo de Entrada:
        10
        52
        9
        4

        Arquivo de saida:
        4,9,10,52

    Args:
        buffer_size: Tamanho do buffer 
        input_path: Path do arquivo de entrada
        output_path: Path do arquivo de saída
    """
