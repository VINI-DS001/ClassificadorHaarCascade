import os

# Defina o diretório onde os arquivos estão localizados
diretorio = 'BootBMP'

# Percorra todos os arquivos no diretório
for nome_arquivo in os.listdir(diretorio):
    # Verifique se o arquivo é um arquivo .bmp
    if nome_arquivo.endswith('.bmp'):
        # Crie o novo nome removendo espaços e parênteses
        novo_nome = nome_arquivo.replace(' ', '').replace('(', '').replace(')', '')
        
        # Construa o caminho completo para o arquivo original e o novo arquivo
        caminho_original = os.path.join(diretorio, nome_arquivo)
        caminho_novo = os.path.join(diretorio, novo_nome)
        
        # Renomeie o arquivo se o novo nome for diferente
        if caminho_original != caminho_novo:
            os.rename(caminho_original, caminho_novo)
            print(f'Renomeado: "{nome_arquivo}" para "{novo_nome}"')

print("Renomeação concluída.")
