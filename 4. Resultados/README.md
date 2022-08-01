# 4. Resultados

- [4. Resultados](#4-resultados)
  - [Coleta e bases de dados](#coleta-e-bases-de-dados)
    - [Datas e horários das coletas](#datas-e-horários-das-coletas)
    - [Quantidade de tweets e tamanho das bases](#quantidade-de-tweets-e-tamanho-das-bases)
    - [Quantidade de tweets presentes nas sub-bases](#quantidade-de-tweets-presentes-nas-sub-bases)
  - [Modelagem de tópicos](#modelagem-de-tópicos)
  - [Análise de sentimentos](#análise-de-sentimentos)
  - [Polaridade dos tópicos por idioma](#polaridade-dos-tópicos-por-idioma)
    - [Português](#português)
    - [Espanhol](#espanhol)
    - [Inglês](#inglês)
  - [Polaridades por tópico comum aos idiomas](#polaridades-por-tópico-comum-aos-idiomas)
  - [Polaridades por tópico comum aos anos](#polaridades-por-tópico-comum-aos-anos)

## Coleta e bases de dados

### Datas e horários das coletas

| **Ano** | **Início**         | **Fim**            |
| ------- | ------------------ | ------------------ |
| 2020    | 07/03 21h00 UTC -3 | 09/03 17h00 UTC -3 |
| 2021    | 07/03 19h00 UTC -3 | 09/03 19h00 UTC -3 |

### Quantidade de tweets e tamanho das bases

- **2020**

| **Bases**  | **Quantidade** | **Tamanho (GB)** |
| ---------- | -------------- | ---------------- |
| Base 1     | 1.878.069      | 12,4             |
| Base 2     | 3.703.971      | 28,4             |
| Base 3     | 4.065.364      | 30,0             |
| Base geral | 5.558.171      | 37,1             |

- **2021**

| **Bases**  | **Quantidade** | **Tamanho (GB)** |
| ---------- | -------------- | ---------------- |
| Base 1     | 5.631.905      | 36,8             |
| Base 2     | 5.561.617      | 36.4             |
| Base geral | 5.360.203      | 39,1             |

### Quantidade de tweets presentes nas sub-bases

|           | 2020      | 2021      |
| --------- | --------- | --------- |
| Inglês    | 1.991.792 | 2.459.599 |
| Espanhol  | 1.898.572 | 1.441.175 |
| Português | 274.636   | 124.444   |

## Modelagem de tópicos

- **2020**

| **Idioma** | **Quant.** | **Descritores**                                                                                                                                       |
| ---------- | ---------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| Inglês     | 5          | Sororidade, Celebração da mulher, Características da mulher, Equidade, Política                                                                       |
| Espanhol   | 10         | Comemoração, Memória, Marco histórico, Desejos e anseios, Lutas diárias, Manifestações, Protestos, Violência de gênero, Sororidade, Papéis familiares |
| Português  | 5          | Marco histórico, Homenagens cotidianas, Sarcasmo, Sororidade, Prestar tributo                                                                         |

- **2021**

| Idioma    | Quant. | Descritores                                                                                                                                                                                 |
| --------- | ------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Inglês    | 10     | Empoderamento, Manifestações em redes sociais, Ativismo interseccional, Celebração, Inspiração, Música, Homenagem à profissionais de saúde, Mães solo, Desejos de mudança, Criação/educação |
| Espanhol  | 5      | Denuncia, Resistência, Tributo, Celebração, Violência                                                                                                                                       |
| Português | 5      | Felicitações, Política, Marco histórico, Campanhas, Lutas diárias                                                                                                                           |

## Análise de sentimentos

- **2020**

|           | **Neutro** | **Positivo** | **Negativo** | **Indefinido** |
| --------- | ---------- | ------------ | ------------ | -------------- |
| Português | 97,85%     | 1,22%        | 0,63%        | 0,30%          |
| Espanhol  | 97,51%     | 1,26%        | 0,75%        | 0,48%          |
| Inglês    | 62,73%     | 27,70%       | 5,93%        | 3,64%          |

- **2021**

|           | **Neutro** | **Positivo** | **Negativo** | **Indefinido** |
| --------- | ---------- | ------------ | ------------ | -------------- |
| Português | 94,22%     | 3,40%        | 1,01%        | 1,36%          |
| Espanhol  | 97,02%     | 1,69%        | 0,81%        | 0,49%          |
| Inglês    | 60,76%     | 29,67%       | 5,75%        | 3,82%          |

## Polaridade dos tópicos por idioma

### Português

- **2020**

| **Tópico**            | **Neutro** | **Positivo** | **Negativo** |
| --------------------- | ---------- | ------------ | ------------ |
| Marco histórico       | 99,5%      | 0,4%         | 0,1%         |
| Homenagens cotidianas | 98,8%      | 0,9%         | 0,3%         |
| Sarcasmo              | 99,2%      | 0,6%         | 0,2%         |
| Sororidade            | 98,4%      | 1,2%         | 0,4%         |
| Prestar tributo       | 99,9%      | 0,1%         | 0            |

- **2021**

| Tópico          | **Neutro** | **Positivo** | **Negativo** |
| --------------- | ---------- | ------------ | ------------ |
| Felicitações    | 99,5%      | 0,5%         | 0            |
| Política        | 99,3%      | 0,5%         | 0,2%         |
| Marco histórico | 99,7%      | 0,2%         | 0,1%         |
| Campanhas       | 99%        | 0,8%         | 0,2%         |
| Lutas diárias   | 89,2%      | 10,2%        | 0,6%         |

### Espanhol

- **2020**

| **Tópico**          | **Neutro** | **Positivo** | **Negativo** |
| ------------------- | ---------- | ------------ | ------------ |
| Comemoração         | 99,4%      | 0,4%         | 0,2%         |
| Memória             | 99,9%      | 0,1%         | 0            |
| Marco histórico     | 99,6%      | 0,3%         | 0,1%         |
| Desejos e anseios   | 99,7%      | 0,3%         | 0            |
| Lutas diárias       | 99,6%      | 0,4%         | 0            |
| Manifestações       | 99,4%      | 0,5%         | 0,1%         |
| Protestos           | 99%        | 0,8%         | 0,2%         |
| Violência de gênero | 98,6%      | 1,2%         | 0,2%         |
| Sororidade          | 98,5%      | 0,9%         | 0,6%         |
| Papéis familiares   | 99%        | 0,8%         | 0,2%         |

- **2021**

| **Tópico**  | **Neutro** | **Positivo** | **Negativo** |
| ----------- | ---------- | ------------ | ------------ |
| Denuncia    | 99,4%      | 0,5%         | 0,1%         |
| Resistência | 99,5%      | 0            | 0,5%         |
| Tributo     | 98,8%      | 0,9%         | 0,3%         |
| Celebração  | 99,8%      | 0,2%         | 0            |
| Violência   | 99,1%      | 0,6%         | 0,3%         |

### Inglês

- **2020**

| **Tópico**                | **Neutro** | **Positivo** | **Negativo** |
| ------------------------- | ---------- | ------------ | ------------ |
| Sororidade                | 0          | 100%         | 0            |
| Celebração da mulher      | 17,7%      | 82%          | 0,3%         |
| Características da mulher | 30,9%      | 68,6%        | 0,5%         |
| Equidade                  | 37,3%      | 61,8%        | 0,9%         |
| Política                  | 14,1%      | 82,5%        | 3,4%         |

- **2021**

| **Tópico**                         | **Neutro** | **Positivo** | **Negativo** |
| ---------------------------------- | ---------- | ------------ | ------------ |
| Empoderamento                      | 0          | 100%         | 0            |
| Manifestações em redes sociais     | 19,5%      | 80,5%        | 0            |
| Ativismo interseccional            | 32,8%      | 65,3%        | 1,9%         |
| Celebração                         | 20,9%      | 78,6%        | 0,5%         |
| Inspiração                         | 41,6%      | 57,5%        | 0,9%         |
| Música                             | 5,6%       | 94,3%        | 0,1%         |
| Homenagem à profissionais de saúde | 3,4%       | 96,6%        | 0            |
| Mães solo                          | 24,2%      | 75,3%        | 0,5%         |
| Desejos de mudança                 | 20,1%      | 73,7%        | 6,2%         |
| Criação/educação                   | 0,1%       | 99,9%        | 0            |

## Polaridades por tópico comum aos idiomas

- **Sororidade (2020)**

| **Idioma** | **Neutro** | **Positivo** | **Negativo** |
| ---------- | ---------- | ------------ | ------------ |
| Português  | 98,4%      | 1,2%         | 0,4%         |
| Espanhol   | 98,5%      | 0,9%         | 0,6%         |
| Inglês     | 0          | 100%         | 0            |

- **Marco histórico (2020)**

| **Idioma** | **Neutro** | **Positivo** | **Negativo** |
| ---------- | ---------- | ------------ | ------------ |
| Portguês   | 99,5%      | 0,4%         | 0,1%         |
| Espanhol   | 99,6%      | 0,3%         | 0,1%         |

- **Celebração (2021)**

| **Idioma** | **Neutro** | **Positivo** | **Negativo** |
| ---------- | ---------- | ------------ | ------------ |
| Espanhol   | 99,8%      | 0,2%         | 0            |
| Inglês     | 20,9%      | 78,6%        | 0,5%         |

## Polaridades por tópico comum aos anos

- **Lutas diárias**

| **Idioma-ano** | **Neutro** | **Positivo** | **Negativo** |
| -------------- | ---------- | ------------ | ------------ |
| Espanhol-2020  | 99,6%      | 0,4%         | 0            |
| Português-2021 | 89,2%      | 10,2%        | 0,6%         |

- **Marco histórico**

| **Idioma-ano** | **Neutro** | **Positivo** | **Negativo** |
| -------------- | ---------- | ------------ | ------------ |
| Espanhol-2020  | 99,6%      | 0,3%         | 0,1%         |
| Português-2021 | 99,7%      | 0,2%         | 0,1%         |

- **Política**

| **Idioma-ano** | **Neutro** | **Positivo** | **Negativo** |
| -------------- | ---------- | ------------ | ------------ |
| Inglês-2020    | 14,1%      | 82,5%        | 3,4%         |
| Português-2021 | 99,3%      | 0,5%         | 0,2%         |
