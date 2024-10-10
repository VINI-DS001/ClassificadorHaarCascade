# Classificador Haar Cascade para Detecção de Imagens

Equipe: Felipe Leão, Luan Machado, Vinícius Souza

Este repositório contém os códigos e documentação do projeto de construção e treinamento de um **Classificador Haar Cascade** para detecção de objetos específicos em imagens. O projeto utiliza o OpenCV para criar o classificador e realizar a extração de características, bem como o treinamento usando imagens positivas e negativas.

## Índice
- [Descrição do Projeto](#descrição-do-projeto)
- [Timeline do Projeto](#timeline-do-projeto)
- [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [Timeline do Projeto](#timeline-do-projeto)
- [Instalação e Execução](#instalação-e-execução)
- [Treinamento e Geração dos Arquivos](#treinamento-e-geração-dos-arquivos)
    - [Geração do Arquivo .vec](#geração-do-arquivo-vec)
    - [Geração dos Arquivos info.txt e bg.txt](#geração-dos-arquivos-infotxt-e-bgtxt)
- [Conjunto de Dados](#conjunto-de-dados)
- [Conversão de Imagens](#conversão-de-imagens)

## Descrição do Projeto

Este projeto tem como objetivo treinar um classificador utilizando o método Haar Cascade para a detecção de objetos visuais a partir de imagens. O processo inclui a criação do arquivo de vetores `.vec`, a geração de arquivos de descrição (`info.txt` e `bg.txt`), e o treinamento do classificador Haar Cascade com as imagens positivas e negativas.

## Timeline do Projeto

Inicialmente foi realizada a tentativa de seguir o procedimento descrito pelo [documento da Universidade de Auckland](https://github.com/felipecbarelli/livro-visao-computacional/blob/master/tutoriais/creating-a-cascade-of-haar-like-classifiers.pdf), utilizando o dataset "Boot" obtido no site Kaggle, entretanto não foi possível gerar corretamente os arquivos .txt.

Através de uma pesquisa mais aprofundada descobrimos que era necessário utilizar a versão 3.4.x do OpenCV devido aos métodos de treinamento do Haar Cascade terem sido removidos em versões 4.x Uma nova tentativa foi realizada utilizando a versão 3.4.16 do OpenCV, sendo possível gerar o arquivo .xml para detectar os objetos.

Uma alternativa encontrada foi o treinamento realizado através da aplicação [Cascade Trainer GUI](https://amin-ahmadi.com/cascade-trainer-gui/), criada pelo desenvolvedor de software Amin Ahmadi, o que possibilitou realizar o treinamento de vários datasets, variando suas features de treino para testar sua eficiência. Para realizar o treinamento através dessa aplicação, deve-se criar um diretório contendo duas pastas, "p" e "n", que contém respectivamente as imagens positivas e negativas. Ao abrir a aplicação, deve-se selecionar o diretório e ajustar os parâmetros de nº de estágios, quantidade de imagens positivas e negativas a serem usadas e a memória a ser usada. Por fim, deve-se iniciar o treinamento e aguardar a criação do arquivo .xml.

## Tecnologias Utilizadas
- Python 3.x
- OpenCV 3.4.x
- PIL (Python Imaging Library)
- Bibliotecas: `numpy`, `opencv-python`, `Pillow`
- Git/GitHub para controle de versão e colaboração

## Timeline do Projeto

Inicialmente foi realizada a tentativa de seguir o procedimento descrito pelo [documento da Universidade de Auckland](https://github.com/felipecbarelli/livro-visao-computacional/blob/master/tutoriais/creating-a-cascade-of-haar-like-classifiers.pdf), utilizando o dataset "Boot" obtido no site Kaggle, entretanto não foi possível gerar corretamente os arquivos .txt.

Através de uma pesquisa mais aprofundada descobrimos que era necessário utilizar a versão 3.4.x do OpenCV devido aos métodos de treinamento do Haar Cascade terem sido removidos em versões 4.x Uma nova tentativa foi realizada utilizando a versão 3.4.16 do OpenCV, porém não foi possível gerar o arquivo .xml por conta de erros oriundos do arquivo do vetor.

Uma nova tentativa foi realizada através da aplicação [Cascade Trainer GUI](https://amin-ahmadi.com/cascade-trainer-gui/), criada pelo desenvolvedor de software Amin Ahmadi, o que possibilitou realizar o treinamento de vários datasets, variando suas features de treino para testar sua eficiência.

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

4. Gere os arquivos `info.txt` e `bg.txt` para o treinamento:
    ```bash
    python gerarinfo.py
    python gerarbg.py
    ```

5. Gere o arquivo `.vec` com as imagens positivas:
    ```bash
    python gerarvec.py
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
