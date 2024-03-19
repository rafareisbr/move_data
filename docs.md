# Sources

- Este projeto tem o objetivo de tentar criar extratores simples de dados para utilizar dentro do apache airflow
- Os extratores capturam o dado da origem e transformam em pandas e então em um arquivo de texto (json, parquet, csv)

## Tipos de sync que gostariamos de ter:
- Full Refresh - Overwrite
- Incremental Sync - Time Window

## Init package
hatch new "nome projeto"
hatch new --init # existing project

# Create env
hatch env create
hatch shell (ativa o ambiente)
pip show omni_move_data (confirma pacote instalado)
hatch run python -c "import sys;print(sys.executable)" # onde está o python do environment

# Test
hatch run test (roda os testes do pytest)

## Gerar build e instalar pacote
hatch build
pip install dist/pacote_gerado.whl

## Instalar pacote em modo editável
pip install -e .

## Se você subir o projeto nesta estrutura pode instalar pacote pelo link do github
pip install git+ssh://git@github.com:seu_usuario/seu_projeto.git
