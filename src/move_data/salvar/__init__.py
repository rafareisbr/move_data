import csv
from abc import ABC, abstractmethod

import pandas


class Salvar(ABC):

    @abstractmethod
    def salvar(self):
        pass


class SalvarSqlAlquemy(Salvar):

    def __init__(
            self,
            df: pandas.DataFrame,
            engine,
            nome_tabela: str,
            method="multi",
            if_exists="replace",
            index=False
    ):
        self.df = df
        self.engine = engine
        self.nome_tabela = nome_tabela
        self.if_exists = if_exists
        self.method = method
        self.index = index

    def salvar(self):
        self.df.to_sql(
            name=self.nome_tabela,
            if_exists=self.if_exists,
            con=self.engine,
            method=self.method,
            index=self.index,
            # chunksize=2500
        )
        return f"SALVANDO PARA SQL_ALQUEMY"


class SalvarArquivos(Salvar):
    extensao_dos_arquivos = 'none'

    def __init__(self, df: pandas.DataFrame, caminho_arquivo: str, nome_arquivo: str):
        self.df = df
        self.caminho_arquivo = caminho_arquivo
        self.nome_arquivo = nome_arquivo
        self.caminho_completo = f'{caminho_arquivo}/{self.nome_arquivo}.{self.extensao_dos_arquivos}'

    @abstractmethod
    def salvar(self):
        pass


class SalvarJson(SalvarArquivos):
    extensao_dos_arquivos = 'json'

    def salvar(self, index=False, orient='records', date_format='iso'):
        self.df.to_json(
            self.caminho_completo,
            index=index,
            orient=orient,
            date_format=date_format
        )
        print(f"SALVANDO PARA {self.extensao_dos_arquivos}")


class SalvarCsv(SalvarArquivos):
    extensao_dos_arquivos = 'csv'

    def salvar(
            self,
            index=False,
            sep='~',
            # header=True,
            na_rep='null',
            encoding='utf-8',
            escapechar="\\",
            # doublequote=False,
            quoting=csv.QUOTE_NONNUMERIC
    ):
        self.df.to_csv(self.caminho_completo,
                       index=index,
                       sep=sep,
                       # header=header,
                       na_rep=na_rep,
                       encoding=encoding,
                       escapechar=escapechar,
                       # doublequote=doublequote,
                       quoting=quoting
                       )
        print(f"SALVANDO PARA {self.extensao_dos_arquivos}")


class SalvarParquet(SalvarArquivos):
    extensao_dos_arquivos = 'parquet'

    def salvar(self, index=False):
        self.df.to_parquet(
            self.caminho_completo,
            engine="pyarrow",
            index=index
        )
        print(f"SALVANDO PARA {self.extensao_dos_arquivos}")

