import os
import subprocess

# Diretório base para downloads
BASE_DIR = "/sdcard/Arquivos-Download"

# Função para criar diretórios
def create_directory(path):
    if not os.path.exists(path):
        os.makedirs(path)

# Função para baixar músicas
def download_music(category, search_term):
    output_dir = os.path.join(BASE_DIR, category)
    create_directory(output_dir)

    print(f"\nBaixando para: {output_dir}")
    try:
        subprocess.run(["spotdl", "download", search_term, "--output", output_dir], check=True)
        print(f"\n✅ Download concluído! Arquivos salvos em: {output_dir}\n")
    except subprocess.CalledProcessError:
        print("\n❌ Erro ao baixar. Verifique o link ou sua instalação do SpotDL.")

# Função para exibir o menu principal
def display_menu():
    print("=" * 40)
    print("🎵 Bem-vindo ao Downloader de Músicas 🎵")
    print("=" * 40)
    print("1️⃣  Baixar uma Música")
    print("2️⃣  Baixar um Álbum")
    print("3️⃣  Baixar uma Playlist")
    print("4️⃣  Baixar músicas de um Artista (Top Músicas)")
    print("5️⃣  Baixar as Top 10 Músicas (Global)")
    print("0️⃣  Sair")
    print("=" * 40)

# Menu principal
def main():
    while True:
        display_menu()
        try:
            option = int(input("➡ Escolha uma opção (0-5): "))
        except ValueError:
            print("❌ Opção inválida! Por favor, insira um número de 0 a 5.")
            continue

        if option == 0:
            print("\n👋 Saindo... Até logo!")
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
            search_term = "ytsearch:top 10 popular songs"
            download_music("Top-10", search_term)
        else:
            print("❌ Opção inválida! Tente novamente.")

if __name__ == "__main__":
    # Criar o diretório base se não existir
    create_directory(BASE_DIR)

    # Verificar se o SpotDL está instalado
    try:
        subprocess.run(["spotdl", "--version"], check=True, stdout=subprocess.DEVNULL)
        main()
    except FileNotFoundError:
        print("❌ SpotDL não está instalado.")
        print("💡 Instale-o com: pip install spotdl")
