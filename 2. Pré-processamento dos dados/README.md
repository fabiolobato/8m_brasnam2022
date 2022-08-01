# 2. Pré-processamento dos dados

- [2. Pré-processamento dos dados](#2-pré-processamento-dos-dados)
  - [2.1. Limpeza e arquivos csv](#21-limpeza-e-arquivos-csv)
  - [2.2. Dividir dados em arquivos de 1k linhas](#22-dividir-dados-em-arquivos-de-1k-linhas)

São os scripts responsáveis pela etapa de pré-processamento dos dados e criação dos arquivos a serem usado como entrada para a fase de implementação da análise dos dados.

Para essa etapa, optou-se pela utilização de python notebooks, que podem ser utilizados via Jupyter Notebook, Jupyter Lab ou mesmo pelo VSCode, entre outros.

Existem 2 diretórios aqui:

## 2.1. Limpeza e arquivos csv

Aqui ficam localizados os notebooks responsáveis pela limpeza dos dados e pela criação de arquivos csv e txt.

Cada arquivo possui três arquivos de saída:

1. Arquivo csv completo, com os tweets sem pré-processamento
2. Arquivo csv com os tweets já pré-processados
3. Arquivo txt contendo somente os textos dos tweets pré-processados

O arquivo txt será o utilizado como entrada da Modelagem de tópicos na eta posterior de análise dos dados.

## 2.2. Dividir dados em arquivos de 1k linhas

Aqui ficam os notebooks responsáveis por dividir os arquivos txt gerados na fase anterior em arquivos de 1.000 linhas para serem usados de entrada na fase de Análise de Sentimentos, feita via iFeel. Eles ficarão cada um localizado em um diretório referente ao seu idioma.
