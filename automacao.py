import os
import os.path
import shutil
from pathlib import Path

diretorio = ""
programa = True

def exibir_menu():
    print("\n-------- AUTOMAÇÃO DE ARQUIVOS -------")
    print("1. Para mudar o diretorio.")
    print("2. Para renomear arquivos.")
    print("3. Para renomear somente uma extensão.")
    print("4. Mover Arquivos")
    print("5. Sair do programa.")    

def opcao():
    opcao = input("\nEscolha uma opção: ").strip()
    while opcao not in ["1", "2", "3", "4", "5"]:
        print("\nOpção Inválida")
        exibir_menu()
        opcao = input("\nEscolha uma opção: ").strip()
    return opcao

def pegar_diretorio():
    while True:
        print("\n-------- AUTOMAÇÃO DE ARQUIVOS -------")
        caminho = input(r"Cole o seu diretório aqui: ").strip()
        if os.path.isdir(caminho):
            print(f"O diretório: '{caminho}' existe.")
            os.chdir(caminho)
            print(f"\nArquivos dessa pasta: {os.listdir()}\n")
            return caminho
        else:
            print("\nDiretório não existe.")
            continue
        
def renomear():
    global diretorio
    nome = input("Digite o nome do seu arquivo: ")

    for i, filename in enumerate(os.listdir(diretorio)):
        caminho_antigo = os.path.join(diretorio, filename)
       
        if os.path.isfile(filename):
            extensao = Path(filename).suffix.lower()
            nome_formatado = f"{nome}_{i+1}{extensao}"
            caminho_novo = os.path.join(diretorio, nome_formatado)
            os.rename(caminho_antigo, caminho_novo)   
            
    print(f"Arquivos renomeados: {os.listdir(diretorio)}\n")

def renomear_extensao():
    global diretorio

    extensoes = {
    "1": ".jpg",
    "2": ".jpeg",
    "3": ".png",
    "4": ".pdf",
    "5": ".flac",
    "6": ".docx",
    "7": ".xlsx",
    "8": ".txt",
    "9": ".mp3",
    "10": ".mp4",
    "11": ".mkv",
    "12": ".avi",
    "13": ".zip",
    "14": ".rar"
    }

    extensao = True

    while extensao:
        print("\n1. JPG")
        print("2. JPEG")
        print("3. PNG")
        print("4. PDF")
        print("5. FLAC")
        print("6. DOCX")
        print("7. XLSX")
        print("8. TXT")
        print("9. MP3")
        print("10. MP4")
        print("11. MKV")
        print("12. AVI")
        print("13. ZIP")
        print("14. RAR")
        
        escolha = input("\nPara qual extensão deseja renomear?: ").strip()
        if escolha not in extensoes:
            print("Opção inválida! Escolha um número de 1 a 14.")
            continue
        extensao_alvo = extensoes[escolha]

        
        encontrou_arquivo = False
        for filename in os.listdir(diretorio):
            if Path(filename).suffix.lower() == extensao_alvo:
                encontrou_arquivo = True
                break
   
        if not encontrou_arquivo:
            print(f"\nNão existe arquivos com a extensão {extensao_alvo} nesta pasta.")   
        else:
            novo_nome = input(f"\nDigite o novo nome para os arquivos {extensao_alvo}: ")    
            for i, filename in enumerate(os.listdir(diretorio)):
                    tipo = Path(filename)
                    if tipo.suffix.lower() == extensao_alvo:
                        caminho_antigo = os.path.join(diretorio, filename)
                        nome_formatado = f"{novo_nome}_{i+1}{extensao_alvo}"
                        caminho_novo = os.path.join(diretorio, nome_formatado)
                        os.rename(caminho_antigo,caminho_novo)

            print(f"\nArquivos renomeados com sucesso!")
            print(f"Estado atual da pasta: {os.listdir(diretorio)}\n")
        
        confirm = input("Deseja renomear as extensões novamente?: (s/n): ").lower().strip()

        while confirm not in ["s", "n"]:
            print("Opção Inválida")
            confirm = input("Deseja renomear as extensões novamente?: (s/n): ").lower().strip()

        if confirm == "n":
            extensao = False
        

def mover_arquivos():
    global diretorio
    gavetas = {"Imagens": [".jpg", ".jpeg", ".png", ".webp"],
               "Documentos": [".pdf", ".docx", ".xlsx", ".txt"],
               "Musicas": [".mp3", ".flac", ".wav"],
               "Videos": [".mp4", ".mkv", ".avi"]}
    

    for filename in os.listdir(diretorio):
        caminho_arquivo = os.path.join(diretorio, filename)

        if os.path.isdir(caminho_arquivo):
            continue

        extensao = Path(filename).suffix.lower()

        for nome_da_pasta, lista_de_extensoes in gavetas.items():
            if extensao in lista_de_extensoes:
                pasta_destino = os.path.join(diretorio, nome_da_pasta)
                if not os.path.exists(pasta_destino):
                    os.makedirs(pasta_destino)


                shutil.move(caminho_arquivo, pasta_destino)
                print(f"-> {filename} movido para {nome_da_pasta}/")
                break

    
diretorio = pegar_diretorio() 
while programa:
    exibir_menu()  
    pegar_opcao = opcao()

    if pegar_opcao == "1":
        diretorio = pegar_diretorio() 
    elif pegar_opcao == "2":
        renomear()
    elif pegar_opcao == "3":
        renomear_extensao()
    elif pegar_opcao == "4":
        mover_arquivos()
    elif pegar_opcao == "5":
        programa = False
        print("Programa Finalizado.")
