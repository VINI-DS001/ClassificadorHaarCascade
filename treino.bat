@echo off
:: Caminho para o utilitário de treinamento do OpenCV (modifique se necessário)
set exe_path=C:/Users/vinid/Downloads/opencv/build/x64/vc15/bin/opencv_traincascade.exe

:: Criar diretório de saída, se não existir
set data_dir=cascade
if not exist %data_dir% mkdir %data_dir%

:: Parâmetros de treinamento
set vec_file=positives.vec  :: O arquivo .vec gerado
set bg_file=bg.txt          :: O arquivo bg.txt com as imagens negativas
set numPos=200             :: Número de amostras positivas
set numNeg=200              :: Número de amostras negativas
set numStages=10            :: Número de estágios do classificador
set width=119               :: Largura da amostra
set height=93               :: Altura da amostra
set mem=2048                :: Ajuste a memória (em MB) conforme sua máquina

:: Executa o treinamento
%exe_path% -data %data_dir% -vec %vec_file% -bg %bg_file% -numPos %numPos% -numNeg %numNeg% -numStages %numStages% -w %width% -h %height% -featureType HAAR -mem %mem%

echo Treinamento concluído!
pause
