import os
import subprocess
from datetime import datetime

# Diretório base para downloads
BASE_DIR = "/sdcard/Arquivos-Download"

# Função para criar diretórios
def create_directory(path):
    if not os.path.exists(path):
        os.makedirs(path)

# Função para registrar erros
def log_error(error_message):
    with open("errors.log", "a") as error_file:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        error_file.write(f"[{timestamp}] {error_message}\n")

# Função para baixar músicas
def download_music(category, search_term):
    output_dir = os.path.join(BASE_DIR, category)
    create_directory(output_dir)

    print(f"\n\033[94m📂 Baixando para: {output_dir}\033[0m")
    try:
        subprocess.run(["spotdl", "download", search_term, "--output", output_dir], check=True)
        print(f"\n\033[92m✅ Download concluído! Arquivos salvos em: {output_dir}\033[0m\n")
    except subprocess.CalledProcessError as e:
        print("\n\033[91m❌ Erro ao baixar. Verifique o link ou sua instalação do SpotDL.\033[0m")
        log_error(str(e))

# Função para exibir o menu principal
def display_menu():
    print("\n" + "=" * 50)
    print("\033[96m🎵 Bem-vindo ao Downloader de Músicas 🎵\033[0m")
    print("=" * 50)
    print("\033[93m1️⃣  Baixar uma Música")
    print("2️⃣  Baixar um Álbum")
    print("3️⃣  Baixar uma Playlist")
    print("4️⃣  Baixar músicas de um Artista (Top Músicas)")
    print("5️⃣  Baixar as Top Músicas (Global)")
    print("0️⃣  Sair\033[0m")
    print("=" * 50)

# Menu principal
def main():
    while True:
        display_menu()
        try:
            option = int(input("\033[92m➡ Escolha uma opção (0-5): \033[0m"))
        except ValueError:
            print("\033[91m❌ Opção inválida! Por favor, insira um número de 0 a 5.\033[0m")
            continue

        if option == 0:
            print("\n\033[93m👋 Saindo... Até logo!\033[0m")
            break
        elif option == 1:
            url = input("\n🔗 Insira o link da música: ")
            download_music("Música", url)
        elif option == 2:
            url = input("\n🔗 Insira o link do álbum: ")
            download_music("Álbum", url)
        elif option == 3:
            url = input("\n🔗 Insira o link da playlist: ")
            download_music("Playlist", url)
        elif option == 4:
            artist = input("\n🎤 Insira o nome do artista: ")
            search_term = f"ytsearch:top tracks of {artist}"
            download_music(f"Artista/{artist}", search_term)
        elif option == 5:
            try:
                num_songs = int(input("\n🔢 Quantas músicas deseja baixar? (Padrão: 10): ") or 10)
                search_term = f"ytsearch:top {num_songs} popular songs"
                download_music("Top-Músicas", search_term)
            except ValueError:
                print("\033[91m❌ Entrada inválida! Usando valor padrão (10 músicas).\033[0m")
                search_term = "ytsearch:top 10 popular songs"
                download_music("Top-Músicas", search_term)
        else:
            print("\033[91m❌ Opção inválida! Tente novamente.\033[0m")

if __name__ == "__main__":
    # Criar o diretório base se não existir
    create_directory(BASE_DIR)

    # Verificar se o SpotDL está instalado
    try:
        subprocess.run(["spotdl", "--version"], check=True, stdout=subprocess.DEVNULL)
        main()
    except FileNotFoundError:
        print("\033[91m❌ SpotDL não está instalado.\033[0m")
        print("\033[93m💡 Instale-o com: pip install spotdl\033[0m")