from abc import ABC, abstractmethod


class GeradorNomeArquivo(ABC):

    @abstractmethod
    def get_nome(self):
        pass


class GeradorNomeArquivoPorIndice(GeradorNomeArquivo):

    def __init__(self, nome: str, indice: int):
        self.nome = nome
        self.indice = indice

    def get_nome(self):
        return f'{self.nome}_{str(self.indice).zfill(5)}'

