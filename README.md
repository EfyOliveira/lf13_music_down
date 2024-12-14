# lf13 Music Downloader

Script em Python para baixar músicas, álbuns, playlists e até mesmo os Top 10 de músicas do Autor. Ele realizar os downloads e organiza os arquivos em pastas de acordo com a categoria escolhida.


---

Requisitos

Antes de usar o script, você precisará instalar alguns pacotes e ferramentas:

Dependências

Python 3

SpotDL - Ferramenta para baixar músicas do Spotify

FFmpeg (para o tratamento de arquivos de mídia)


Instalação

1. Instale o Python 3 e outras dependências necessárias:

Termux:

* `pkg install python ffmpeg`

Linux/macOS/Windows: Baixe o Python aqui e instale o FFmpeg a partir do repositório oficial.



2. Instale o SpotDL:

Com o Python e FFmpeg configurados, instale o SpotDL usando pip:

* `pip install spotdl`

Observação: Se você encontrar problemas relacionados ao Rust, como mostrado na instalação do SpotDL, instale o compilador Rust executando:

* `pkg install rust`


3. Baixe este repositório:

Clone o repositório para sua máquina:

* `git clone https://github.com/EfyOliveira/lf13_music_down.git`

* `cd lf13_music_down`

* `bash install.sh`



---

Uso

1. Execute o script:

No diretório onde o script foi baixado, execute:

* `python main.py`


2. Escolha uma opção:

O script exibirá um menu interativo com as opções abaixo:

1: Baixar uma música

2: Baixar um álbum

3: Baixar uma playlist

4: Baixar as músicas de um artista (Top Músicas)

5: Baixar as Top 10 músicas globais

0: Sair do programa



3. Informe o link:

Dependendo da opção escolhida, você precisará fornecer o link (música, álbum, playlist, etc.) ou o nome do artista.


4. Arquivos de Download:

Os arquivos serão baixados para a pasta /sdcard/Arquivos-Download (para Termux) ou para o diretório padrão configurado no script. As músicas serão organizadas em pastas de acordo com a categoria escolhida (Artista, Álbum, Playlist, etc.).




---

Exemplo de Execução

Ao executar o script, você verá algo como:

```bash 🎵 Bem-vindo ao Downloader de Músicas 🎵
1️⃣  Baixar uma Música
2️⃣  Baixar um Álbum
3️⃣  Baixar uma Playlist
4️⃣  Baixar músicas de um Artista (Top Músicas)
5️⃣  Baixar as Top 10 Músicas (Global)
0️⃣  Sair
➡ Escolha uma opção (0-5): 1
🔗 Insira o link da música: https://open.xxxxx.com/track/0vW68x9Vlv7ZJYSF7yDjD8?si=ayDVq8VkQtaknHio4LDggQ
Baixando a música...
Baixando para: /sdcard/Arquivos-Download/Música
✅ Download concluído! Arquivos salvos em: /sdcard/Arquivos-Download/Música
```


---

Contribuições

Sinta-se à vontade para contribuir para este projeto. Se você encontrou um erro ou tem sugestões de melhorias, abra um issue ou envie um pull request.


---

Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo LICENSE para mais detalhes.


---
