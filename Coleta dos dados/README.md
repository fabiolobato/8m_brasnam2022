# 1. Coleta dos dados

São os scripts responsáveis pelos processos de coleta e atualização dos dados.

O script de coleta de dados, bem como mais informações a respeito do seu uso, pode ser obtido no seguinte repositório [gean-costa/stream-tweets](https://github.com/gean-costa/stream-tweets).

O script `atualizar_tweets.py` é o responsável pela atualização dos dados. Nele constam as configurações dos tokens de acesso à API do Twitter e da conexão com o MongoDB. Para sua utilização, é necessário editá-lo e usar o comando:

```python
python atualizar_tweets.py
```
