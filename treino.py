import os

# Caminho completo para o opencv_traincascade.exe
opencv_traincascade_path = r"C:/Users/vinicius.d.souza/Downloads/opencv/build/x64/vc15/bin/opencv_traincascade.exe"

# Diretório onde o classificador será salvo
output_dir = 'cascade'
os.makedirs(output_dir, exist_ok=True)

# Parâmetros do treinamento
vec_file = 'positives.vec'  # Arquivo .vec gerado
bg_file = 'bg.txt'  # Arquivo bg.txt gerado
numPos = 200  # Número de imagens positivas
numNeg = 200  # Número de imagens negativas
numStages = 10  # Número de estágios do classificador
w, h = 24, 24  # Dimensão da janela de detecção
feature_type = 'HAAR'  # Tipo de característica (HAAR)

# Montar o comando para treinamento
traincascade_cmd = (
    f"{opencv_traincascade_path} -data {output_dir} -vec {vec_file} -bg {bg_file} "
    f"-numPos {numPos} -numNeg {numNeg} -numStages {numStages} "
    f"-w {w} -h {h} -featureType {feature_type}"
)

# Executar o comando
os.system(traincascade_cmd)

print("Treinamento iniciado...")
