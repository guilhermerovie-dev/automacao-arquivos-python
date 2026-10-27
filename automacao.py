from pathlib import Path
import shutil

def exibir_menu():
    print("\n-------- AUTOMAÇÃO DE ARQUIVOS --------")
    print("1. Mudar o diretório")
    print("2. Renomear todos os arquivos")
    print("3. Renomear apenas uma extensão específica")
    print("4. Organizar/Mover arquivos por categorias")
    print("5. Sair do programa")

def obter_opcao():
    while True:
        opcao = input("\nEscolha uma opção (1-5): ").strip()
        if opcao in ["1", "2", "3", "4", "5"]:
            return opcao
        print("\n[Erro] Opção inválida! Escolha um número de 1 a 5.")

def pegar_diretorio():
    while True:
        print("\n-------- AUTOMAÇÃO DE ARQUIVOS --------")
        caminho_str = input(r"Cole o seu diretório aqui: ").strip().strip('"\'')
        caminho = Path(caminho_str)
        
        if caminho.is_dir():
            print(f"\n[Sucesso] Diretório encontrado: '{caminho.resolve()}'")
            arquivos = [f.name for f in caminho.iterdir() if f.is_file()]
            print(f"Arquivos na pasta ({len(arquivos)}): {arquivos[:5]}{'...' if len(arquivos) > 5 else ''}\n")
            return caminho
        else:
            print("\n[Erro] O diretório informado não existe ou não é válido. Tente novamente.")

def renomear(diretorio: Path):
    nome_base = input("Digite o novo nome base para os arquivos: ").strip()
    if not nome_base:
        print("[Erro] O nome não pode estar vazio.")
        return

    arquivos = [f for f in diretorio.iterdir() if f.is_file()]
    
    if not arquivos:
        print("\n[Aviso] A pasta está vazia.")
        return

    for i, arquivo in enumerate(arquivos, start=1):
        extensao = arquivo.suffix.lower()
        novo_nome = f"{nome_base}_{i}{extensao}"
        caminho_novo = diretorio / novo_nome
        
        arquivo.rename(caminho_novo)
    
    print(f"\n[Sucesso] {len(arquivos)} arquivos renomeados com sucesso!")

def renomear_extensao(diretorio: Path):
    extensoes = {
        "1": ".jpg", "2": ".jpeg", "3": ".png", "4": ".pdf",
        "5": ".flac", "6": ".docx", "7": ".xlsx", "8": ".txt",
        "9": ".mp3", "10": ".mp4", "11": ".mkv", "12": ".avi",
        "13": ".zip", "14": ".rar"
    }

    while True:
        print("\n--- Escolha a Extensão Alvo ---")
        for k, v in extensoes.items():
            print(f"{k}. {v.upper().replace('.', '')}")
        
        escolha = input("\nPara qual extensão deseja renomear? (ou 'v' para voltar): ").strip().lower()
        if escolha == 'v':
            return
        
        if escolha not in extensoes:
            print("[Erro] Opção inválida! Escolha um número da lista.")
            continue
            
        extensao_alvo = extensoes[escolha]
        
        # Filtra apenas arquivos que possuem a extensão alvo
        arquivos_alvo = [f for f in diretorio.iterdir() if f.is_file() and f.suffix.lower() == extensao_alvo]
        
        if not arquivos_alvo:
            print(f"\n[Aviso] Não existem arquivos com a extensão {extensao_alvo} nesta pasta.")
            continue
            
        novo_nome = input(f"\nDigite o novo nome para os arquivos {extensao_alvo}: ").strip()
        if not novo_nome:
            print("[Erro] O nome não pode estar vazio.")
            continue

        for i, arquivo in enumerate(arquivos_alvo, start=1):
            novo_nome_formatado = f"{novo_nome}_{i}{extensao_alvo}"
            caminho_novo = diretorio / novo_nome_formatado
            arquivo.rename(caminho_novo)

        print(f"\n[Sucesso] {len(arquivos_alvo)} arquivos do tipo {extensao_alvo} renomeados!")
        
        confirm = input("Deseja renomear outra extensão? (s/n): ").lower().strip()
        if confirm != 's':
            break

def mover_arquivos(diretorio: Path):
    gavetas = {
        "Imagens": [".jpg", ".jpeg", ".png", ".webp"],
        "Documentos": [".pdf", ".docx", ".xlsx", ".txt"],
        "Musicas": [".mp3", ".flac", ".wav"],
        "Videos": [".mp4", ".mkv", ".avi"]
    }

    movidos = 0
    for arquivo in diretorio.iterdir():
        if arquivo.is_dir():
            continue

        extensao = arquivo.suffix.lower()
        
        for nome_da_pasta, lista_de_extensoes in gavetas.items():
            if extensao in lista_de_extensoes:
                pasta_destino = diretorio / nome_da_pasta
                pasta_destino.mkdir(exist_ok=True)
                
                destino_final = pasta_destino / arquivo.name
                shutil.move(arquivo, destino_final)
                print(f"-> {arquivo.name} movido para {nome_da_pasta}/")
                movidos += 1
                break
                
    print(f"\n[Sucesso] Total de arquivos organizados: {movidos}")

def main():
    diretorio_atual = pegar_diretorio()
    
    while True:
        exibir_menu()
        escolha = obter_opcao()

        if escolha == "1":
            diretorio_atual = pegar_diretorio()
        elif escolha == "2":
            renomear(diretorio_atual)
        elif escolha == "3":
            renomear_extensao(diretorio_atual)
        elif escolha == "4":
            mover_arquivos(diretorio_atual)
        elif escolha == "5":
            print("\nPrograma finalizado. Até logo!")
            break

if __name__ == "__main__":
    main()
