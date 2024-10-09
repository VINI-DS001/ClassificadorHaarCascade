import os

# Caminho completo para o opencv_traincascade.exe
<<<<<<< HEAD
opencv_traincascade_path = r"haartraining.exe"
=======
opencv_traincascade_path = r"C:/Users/vinid/Downloads/opencv/build/x64/vc15/bin/opencv_traincascade.exe"
>>>>>>> 955bbf5c0e81c0f3b42c649c54705a89b14741ee

# Diretório onde o classificador será salvo
output_dir = 'cascade'
os.makedirs(output_dir, exist_ok=True)

# Parâmetros do treinamento
vec_file = 'positives.vec'  # Arquivo .vec gerado
bg_file = 'bg.txt'  # Arquivo bg.txt gerado
numPos = 600 # Número de imagens positivas
numNeg = 600  # Número de imagens negativas
numStages = 5  # Número de estágios do classificador
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
