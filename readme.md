# Move Data

# Motivação
Facilitar o processo de Extracao e Carga de dados num processo que use orquestrador de fluxos de dados
Essa biblioteca expõe dois tipos de comportamentos: Extratores e Salvadores (de dados)
Todos os extratores retornam um iter de dataframes, do pandas
Todos os salvadores esperam um dataframe do pandas
No momento, é possível extrair de bancos de dados suportados pelo SqlAlchemy e Arquivos Suportados pelo Pandas

# Como instalar
pip install git+ssh://git@github.com/rafareisbr/move_data.git

# Exemplo de uso
```python
import sqlalchemy
from move_data.extrair import ExtrairSqlAlquemy
from move_data.salvar import SalvarSqlAlquemy

# todos os extratores do sql alquemy recebem uma engine do sql alquemy como entrada
engine = sqlalchemy.create_engine(
    'postgresql+psycopg2://admin:mysecretpassword@localhost:5432/test'
)

# obtem uma lista virtual de todos os dados em paginas de tamanho 10000, relativas a query de entrada.
dataset = ExtrairSqlAlquemy(
            engine=engine, 
            chunk_size=10000, 
            query="select * from usuarios"
          ).extrair()

for data in dataset:
    SalvarSqlAlquemy(
        df=data,
        engine=engine,
        nome_tabela='tabela_destino',
        if_exists='append'
    ).salvar()
```