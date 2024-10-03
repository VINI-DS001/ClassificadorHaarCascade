import struct
import cv2
import os

def write_vec_file(images, output_file, width, height, num_images_to_use):
    # Garantir que não haja mais imagens do que o necessário
    num_images = min(len(images), num_images_to_use)

    # Abrir o arquivo de saída para escrita em binário
    with open(output_file, 'wb') as f:
        # Escrever o cabeçalho do arquivo .vec
        # Número de amostras, largura e altura
        f.write(struct.pack('<i', num_images))  # Número de amostras que vamos usar
        f.write(struct.pack('<i', width))
        f.write(struct.pack('<i', height))

        # Para cada imagem até o limite de num_images_to_use
        for img_path in images[:num_images]:
            # Carregar a imagem em escala de cinza
            img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
            if img is None:
                print(f"Erro ao carregar a imagem {img_path}")
                continue

            # Redimensionar a imagem para o tamanho desejado (24x24)
            img = cv2.resize(img, (width, height))

            # Converter a imagem em um array linear (uma linha de pixels)
            img_array = img.flatten()

            # Escrever o número de retângulos (sempre 1 no nosso caso)
            f.write(struct.pack('<i', 1))  # 1 objeto por imagem

            # Coordenadas do retângulo: x, y, largura, altura
            f.write(struct.pack('<i', 0))  # x
            f.write(struct.pack('<i', 0))  # y
            f.write(struct.pack('<i', width))  # largura
            f.write(struct.pack('<i', height))  # altura

            # Escrever a imagem como um array de bytes
            f.write(struct.pack(f'<{len(img_array)}B', *img_array))

    print(f"Arquivo .vec gerado com sucesso: {output_file} com {num_images} imagens.")

# Diretório onde estão as imagens positivas (Boot BMP)
dataset_dir = 'Boot BMP'
positive_images = []

# Carregar todas as imagens da pasta Boot BMP
for filename in os.listdir(dataset_dir):
    if filename.endswith('.bmp'):
        img_path = os.path.join(dataset_dir, filename)
        positive_images.append(img_path)

# Definir o número de imagens que queremos usar para o arquivo .vec
num_images_to_use = 200  # Por exemplo, 400 imagens positivas

# Gerar o arquivo .vec com imagens redimensionadas para 24x24
output_vec_file = 'positives.vec'
width, height = 24, 24  # Redimensionar para 24x24 pixels
write_vec_file(positive_images, output_vec_file, width, height, num_images_to_use)
