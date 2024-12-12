#!/bin/bash

# Script de instalação para o Spotify Music Downloader

echo "Iniciando a instalação do Spotify Music Downloader..."

# Verificando se o Python está instalado
if ! command -v python &> /dev/null
then
    echo "Python não encontrado. Instalando..."
    pkg install python -y
else
    echo "Python já está instalado."
fi

# Instalando o FFmpeg
echo "Instalando o FFmpeg..."
pkg install ffmpeg -y

# Instalando o Rust (necessário para SpotDL)
echo "Instalando o Rust..."
pkg install rust -y

# Instalando o SpotDL
echo "Instalando SpotDL..."
pip install spotdl

# Verificação da instalação
echo "Verificando se SpotDL foi instalado corretamente..."
if command -v spotdl &> /dev/null
then
    echo "SpotDL foi instalado com sucesso!"
else
    echo "Houve um erro na instalação do SpotDL. Tente instalar novamente."
fi

echo "Instalação concluída!"
