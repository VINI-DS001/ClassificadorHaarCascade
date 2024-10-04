import struct
import cv2
import os

def write_vec_file(info_file, output_file, width, height):
    # Ler o arquivo info.txt
    with open(info_file, 'r') as f:
        lines = f.readlines()

    num_images = len(lines)

    # Abrir o arquivo de saída para escrita em binário
    with open(output_file, 'wb') as f_out:
        # Escrever o cabeçalho do arquivo .vec
        f_out.write(struct.pack('<i', num_images))
        f_out.write(struct.pack('<i', width))
        f_out.write(struct.pack('<i', height))

        # Processar cada linha do arquivo info.txt
        for line in lines:
            # Separar o caminho do arquivo e os números
            parts = line.strip().split(' ')
            
            # O caminho da imagem pode conter espaços, então devemos reconstruí-lo
            img_path = ' '.join(parts[:-5])  # Juntar tudo até os últimos 5 elementos
            num_rects = int(parts[-5])       # O número de retângulos é o quinto item a partir do final
            x, y, w, h = map(int, parts[-4:])  # Os últimos 4 elementos são as coordenadas

            # Carregar a imagem em escala de cinza
            img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
            if img is None:
                print(f"Erro ao carregar a imagem {img_path}")
                continue

            # Redimensionar a área do retângulo para 24x24
            roi = img[y:y+h, x:x+w]  # Recortar a imagem com base nas coordenadas
            roi_resized = cv2.resize(roi, (width, height))  # Redimensionar para 24x24 pixels

            # Converter a imagem em um array linear (uma linha de pixels)
            img_array = roi_resized.flatten()

            # Escrever o número de retângulos (sempre 1)
            f_out.write(struct.pack('<i', num_rects))

            # Escrever as coordenadas do retângulo (ajustadas para a nova resolução)
            f_out.write(struct.pack('<i', 0))  # x
            f_out.write(struct.pack('<i', 0))  # y
            f_out.write(struct.pack('<i', width))  # largura
            f_out.write(struct.pack('<i', height))  # altura

            # Escrever a imagem como um array de bytes
            f_out.write(struct.pack(f'<{len(img_array)}B', *img_array))

    print(f"Arquivo .vec gerado com sucesso: {output_file} com {num_images} imagens.")

# Caminho para o arquivo info.txt
info_file = 'info.txt'

# Gerar o arquivo .vec com imagens redimensionadas para 24x24
output_vec_file = 'positives.vec'
width, height = 24, 24  # Redimensionar para 24x24 pixels
write_vec_file(info_file, output_vec_file, width, height)
