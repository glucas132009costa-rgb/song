import time
import os
import sqlite3

banco_de_dados = sqlite3.connect("musicas.db")
cursor = banco_de_dados.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS musicas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    artista TEXT NOT NULL,
    album TEXT NOT NULL,
    duracao TEXT NOT NULL,
    genero TEXT NOT NULL,
    ano INTEGER NOT NULL
)
""")
banco_de_dados.commit()


class Song:
    def __init__(self, nome, artista, album, duracao, genero, ano):
        self.nome = nome
        self.artista = artista
        self.album = album
        self.duracao = duracao
        self.genero = genero
        self.ano = ano

def salvar_musica(nome, artista, album, duracao, genero, ano):
    cursor.execute("""
    INSERT INTO musicas (nome, artista, album, duracao, genero, ano)
    VALUES (?, ?, ?, ?, ?, ?)
    """, (nome, artista, album, duracao, genero, ano))

    banco_de_dados.commit()

def registrar_musica():
        while True:
            os.system('cls')
            nome = input('Música: ')
            artista = input('Artista: ')
            album = input('album: ')
            duracao = input('Duração: ')
            genero = input('Gênero: ')
            ano = input('Ano de lançamento: ')
            nova_musica = Song(nome, artista, album, duracao, genero, ano)
            salvar_musica(
                nova_musica.nome,
                nova_musica.artista,
                nova_musica.album,
                nova_musica.duracao,
                nova_musica.genero,
                nova_musica.ano
            )
            print("Música registrada com sucesso!")
            time.sleep(1)
            continue

def app():
     pass
