import os

# Diretório contendo as imagens negativas
negative_images_dir = 'ImagensNegativas'
# Arquivo bg.txt que será gerado
output_bg_file = 'bg.txt'

# Abrir o arquivo bg.txt para escrita
with open(output_bg_file, 'w') as f:
    # Iterar sobre as imagens no diretório negativo
    for filename in os.listdir(negative_images_dir):
        if filename.endswith('.bmp'):  # Certifique-se de que todas as imagens sejam .bmp
            # Caminho completo para a imagem
            image_path = os.path.join(negative_images_dir, filename)
            # Escrever o caminho da imagem no arquivo bg.txt
            f.write(f"{image_path}\n")

print(f"Arquivo {output_bg_file} gerado com sucesso!")
