# Análise dos dados

- [Análise dos dados](#análise-dos-dados)
  - [Modelagem de tópicos](#modelagem-de-tópicos)
  - [Análise de sentimentos](#análise-de-sentimentos)

## Modelagem de tópicos

Os notebooks utilizados nessa etapa foram obtidos do repositório [derekgreene/topic-model-tutorial](https://github.com/derekgreene/topic-model-tutorial) e adaptados ao contexto deste trabalho:

1. Text Preprocessing
2. NMF Topic Models
3. Parameter Selection for NMF

## Análise de sentimentos

Para implementar esta fase foi utilizada ferramenta iFell 2.0 que pode ser encontrada no repositório [matheusaraujo/methodsjava](https://bitbucket.org/matheusaraujo/methodsjava/src/master/).

Para fins de organização, criamos dois diretórios para os arquivos: `inputs_txt`, onde devem ficar localizados os arquivos de entrada para o iFeel, e `outputs_csv`, onde serão armazenados os arquivos gerados pela ferramenta.

Exemplificando o uso do iFeel, vá até o diretório raiz do seu repositório e digite os seguintes comandos:

```shell
cd iFeel
java -jar iFeel.jar --resources ../resources/ --file inputs_text/exemplo.txt --output output_csv/exemplo.csv
```

Após a fase de implementação das análises de sentimento, o notebook `resultados.ipynb` faz a união de todos os arquivos presentes no diretório `outputs_csv` e computa os resultados por polaridade.
