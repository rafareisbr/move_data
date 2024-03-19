import glob
from abc import ABC, abstractmethod

import pandas
import sqlalchemy


class Extrair(ABC):

    @abstractmethod
    def extrair(self):
        pass


class ExtrairSqlAlquemy(Extrair):

    def __init__(self, engine: sqlalchemy.engine.Engine, query: str, chunk_size: int) -> None:
        self.engine = engine
        self.query = query
        self.chunk_size = chunk_size

    def extrair(self):
        return pandas.read_sql(
            sql=self.query,
            con=self.engine,
            chunksize=int(self.chunk_size)
        )


class ExtrairArquivos(Extrair, ABC):
    extensao_dos_arquivos = 'none'

    def __init__(self, caminho_ate_arquivo: str, prefixo_nome_arquivo: str):
        self.caminhos = glob.glob(
            f"{caminho_ate_arquivo}/{prefixo_nome_arquivo}_" + "*" + f".{self.extensao_dos_arquivos}")


class ExtrairCsv(ExtrairArquivos):
    extensao_dos_arquivos = 'csv'

    def __init__(self,
                 caminho_ate_arquivo: str,
                 prefixo_nome_arquivo: str,
                 separator="~",
                 encoding='utf-8',
                 escapechar='\\',
                 header=True,
                 doublequote=False
                 ):
        super().__init__(caminho_ate_arquivo, prefixo_nome_arquivo)
        self.separator = separator
        self.encoding = encoding
        self.escapechar = escapechar
        self.header: bool = header
        self.doublequote: bool = doublequote

    def extrair(self):
        for caminho in self.caminhos:
            yield pandas.read_csv(
                caminho,
                sep=self.separator
            )


class ExtrairJson(ExtrairArquivos):
    extensao_dos_arquivos = 'json'

    def __init__(self,
                 caminho_ate_arquivo: str,
                 prefixo_nome_arquivo: str,
                 orient='records',
                 date_format='iso',
                 encoding='utf-8',
                 convert_dates=True
                 ):
        super().__init__(caminho_ate_arquivo, prefixo_nome_arquivo)
        self.orient = orient
        self.date_format = date_format
        self.encoding = encoding
        self.convert_dates = convert_dates

    def extrair(self):
        for caminho in self.caminhos:
            yield pandas.read_json(
                caminho,
                orient=self.orient,
                encoding=self.encoding,
                convert_dates=self.convert_dates
            )


class ExtrairParquet(ExtrairArquivos):
    extensao_dos_arquivos = 'parquet'

    def extrair(self):
        for caminho in self.caminhos:
            yield pandas.read_parquet(
                caminho,
                engine="pyarrow"
            )
