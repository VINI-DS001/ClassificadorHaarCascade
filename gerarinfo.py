import os

# Nome da pasta do dataset que contém as imagens positivas
dataset = 'BootBMP'
# Arquivo info.txt que será gerado
output_info_file = 'info.txt'

# Coordenadas e dimensões do recorte para as imagens positivas
x = 8  # Coordenada x do canto superior esquerdo do objeto
y = 5  # Coordenada y do canto superior esquerdo do objeto
object_width = 119  # Largura do objeto
object_height = 93  # Altura do objeto

# Verificar se a pasta Boot BMP existe
if not os.path.exists(dataset):
    print(f"Diretório {dataset} não encontrado!")
else:
    # Abrir o arquivo info.txt para escrita
    with open(output_info_file, 'w') as f:
        # Iterar sobre as imagens no diretório Boot BMP
        for filename in os.listdir(dataset):
            if filename.endswith('.bmp'):  # Certifique-se de que o formato está correto
                # Caminho completo para a imagem
                image_path = os.path.join(dataset, filename)
                # Escrever a linha no formato esperado
                f.write(f"{image_path} 1 {x} {y} {object_width} {object_height}\n")

    print(f"Arquivo {output_info_file} gerado com sucesso!")
