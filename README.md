# Classificador Haar Cascade para Detecção de Imagens

Equipe: Felipe Leão, Luan Machado, Vinícius Souza

Este repositório contém os códigos e documentação do projeto de construção e treinamento de um **Classificador Haar Cascade** para detecção de objetos em imagens. O projeto utiliza o OpenCV para criar o classificador e realizar a extração de características, bem como o treinamento usando imagens positivas e negativas.

## Índice
- [Descrição do Projeto](#descrição-do-projeto)
- [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [Instalação e Execução](#instalação-e-execução)
- [Treinamento e Geração dos Arquivos](#treinamento-e-geraçao-dos-arquivos)
    - [Geração do Arquivo .vec](#geraçao-do-arquivo-vec)
    - [Geração dos Arquivos info.txt e bg.txt](#geraçao-dos-arquivos-infotxt-e-bgtxt)
- [Conjunto de Dados](#conjunto-de-dados)
- [Conversão de Imagens](#conversao-de-imagens)
- [Vídeos](#vídeos)

## Descrição do Projeto

Este projeto tem como objetivo construir um classificador utilizando o método Haar Cascade para a detecção de objetos visuais a partir de imagens. O processo inclui a conversão de imagens para o formato BMP, a criação do arquivo de vetores `.vec`, a geração de arquivos de descrição (`info.txt` e `bg.txt`), e o treinamento do classificador Haar Cascade com as imagens positivas e negativas.

## Tecnologias Utilizadas
- Python 3.x
- OpenCV
- PIL (Python Imaging Library)
- Bibliotecas: `numpy`, `opencv-python`, `Pillow`
- Git/GitHub para controle de versão e colaboração

## Instalação e Execução

Para rodar o projeto localmente:

1. Clone o repositório:
    ```bash
    git clone 
    ```

2. Instale as dependências:
    ```bash
    pip install numpy opencv-python Pillow
    ```

3. Execute o script de conversão de imagens de JPG para BMP:
    ```bash
    python conversao.py
    ```

4. Gere o arquivo `.vec` com as imagens positivas:
    ```bash
    python gerarvec.py
    ```

5. Gere os arquivos `info.txt` e `bg.txt` para o treinamento:
    ```bash
    python gerarinfo.py
    python gerarbg.py
    ```

6. Inicie o treinamento do classificador Haar Cascade:
    ```bash
    python treino.py
    ```

## Treinamento e Geração dos Arquivos

### Geração do Arquivo .vec

O arquivo `.vec` é criado utilizando imagens positivas para o treinamento. Essas imagens são convertidas em um formato binário adequado para o treinamento com o OpenCV.

### Geração dos Arquivos info.txt e bg.txt

- `info.txt`: Contém informações sobre as imagens positivas, como a localização e dimensão dos objetos nas imagens.
- `bg.txt`: Contém os caminhos das imagens negativas, que serão utilizadas para o treinamento.

## Conjunto de Dados

O conjunto de dados utilizado neste projeto inclui imagens de sapatos, botas e sandálias. As imagens foram extraídas de um dataset público e convertidas para o formato BMP para o treinamento do classificador Haar Cascade.

- [Dataset: Shoe vs Sandal vs Boot](https://www.kaggle.com/datasets/hasibalmuzdadid/shoe-vs-sandal-vs-boot-dataset-15k-images)

## Conversão de Imagens

O script `conversao.py` converte imagens dos formatos `.jpg` ou `.jpeg` para `.bmp`, o formato necessário para o treinamento do classificador Haar Cascade.

## Vídeos
 - [Apresentação do Projeto](https://drive.google.com/file/d/SEU-LINK)
 - [Execução do Classificador](https://drive.google.com/file/d/SEU-LINK)
