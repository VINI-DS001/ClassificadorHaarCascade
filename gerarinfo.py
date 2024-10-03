import os

# Nome da pasta do dataset que contém as imagens positivas
dataset = 'Boot BMP'
# Arquivo info.txt que será gerado
output_info_file = 'info.txt'

# Dimensões das imagens positivas (todas têm o mesmo tamanho)
image_width = 136  # A largura real das suas imagens
image_height = 102  # A altura real das suas imagens

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
                f.write(f"{image_path} 1 0 0 {image_width} {image_height}\n")

    print(f"Arquivo {output_info_file} gerado com sucesso!")
