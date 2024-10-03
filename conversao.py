import os
from PIL import Image

# Diretório base contendo as pastas dos datasets
base_dir = 'Shoe vs Sandal vs Boot Dataset'
# Nomes das pastas dos datasets
datasets = ['Boot', 'Shoe', 'Sandal']

# Iterar sobre cada dataset
for dataset in datasets:
    # Diretório de entrada de cada dataset
    input_dir = os.path.join(base_dir, dataset)
    # Diretório de saída correspondente para cada dataset
    output_dir = os.path.join(base_dir, f'{dataset} BMP')

    # Cria o diretório de saída se não existir
    os.makedirs(output_dir, exist_ok=True)

    # Loop por todos os arquivos no diretório de entrada
    for filename in os.listdir(input_dir):
        if filename.endswith('.jpg') or filename.endswith('.jpeg'):
            # Caminho completo do arquivo
            jpg_path = os.path.join(input_dir, filename)
            # Abre a imagem JPG
            with Image.open(jpg_path) as img:
                # Converte para BMP
                bmp_path = os.path.join(output_dir, f"{os.path.splitext(filename)[0]}.bmp")
                img.save(bmp_path, 'BMP')

print("Conversão concluída para todos os datasets!")
