import os
import zipfile

caminho = input("Cole aqui o caminho da pasta com os arquivos .ZIP (Atualmente somente .ZIP, outras versões de arquivos compactados não serão extraídos) e pressione Enter: ")

if not os.path.isdir(caminho):
    print(f"\nERRO: O caminho '{caminho}' não foi encontrado ou não é uma pasta válida.")
else:
    print(f"\nIniciando verificação na pasta: {caminho}")
    arquivos_encontrados = 0
    for item in os.listdir(caminho):
        if item.endswith('.zip'):
            arquivos_encontrados = arquivos_encontrados + 1
            caminho_arquivo_zip = os.path.join(caminho, item)
            nome_pasta_destino = os.path.splitext(caminho_arquivo_zip)[0]
            print(f"\nArquivo encontrado: '{item}'")
            os.makedirs(nome_pasta_destino, exist_ok=True)
            try:
                with zipfile.ZipFile(caminho_arquivo_zip, 'r') as arquivo_zip:
                    print(f" -> Extraindo...")
                    arquivo_zip.extractall(nome_pasta_destino)
                    print(f" -> Sucesso! Arquivos extraídos para a pasta '{os.path.basename(nome_pasta_destino)}'.")
            except zipfile.BadZipFile:
                print(f" -> ERRO: O arquivo '{item}' parece estar corrompido ou não é um .zip válido.")
            except Exception as e:
                print(f" -> ERRO inesperado: {e}")

    if arquivos_encontrados == 0:
        print("\nNenhum arquivo .zip foi encontrado na pasta informada.")

print("\n\nProcesso concluído!")
input("Pressione Enter para sair.")