# 1. Coleta e criação de base de dados

São os scripts responsáveis pelos processos de coleta, atualização e organização das bases de dados.

O script de coleta de dados, bem como mais informações a respeito do seu uso, pode ser obtido no seguinte repositório [gean-costa/stream-tweets](https://github.com/gean-costa/stream-tweets).

O script `atualizar_tweets.py` é o responsável pela atualização dos dados. Nele constam as configurações dos tokens de acesso à API do Twitter e da conexão com o MongoDB. Para sua utilização, é necessário editá-lo e usar o comando:

```python
python atualizar_tweets.py
```

Em nosso caso, o processo de coleta utilizou mais de um servidor, resultando em mais de uma base de dados bruta e usamos o script de atualização para deixar todos os dados concentrados em uma única base. Caso esse seja o seu caso, recomenda-se o uso do script `remover_duplicatas.py` para deletar os tweets repetidos (mesmo id):

```python
python remover_duplicatas.py
```

Para dividir a base em sub-bases segundo o idioma, utiliza-se o script `criar_subbase_idioma.py`. Deve-se editar o arquivo no que diz respeito as conexões com o MongoDB e com relação ao parâmetro de idioma (que segue o formato [ISO 639-1](https://pt.wikipedia.org/wiki/ISO_639)):

```python
python criar_subbase_idioma.py
```
