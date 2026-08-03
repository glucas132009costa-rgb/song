import sqlite3
import os
import time
import random
from musica import Song, banco_de_dados, cursor
from app import novo_usuario, historico, Cursor

#inicio do aplicativo após entrar com uma conta
def Inicio():
    algoritmo1()
    algoritmo2()
    algoritmo3()
    algoritmo4()
    algoritmo5()
    os.system('cls')
    print(f'Bem vindo, {novo_usuario.nome}\n')
    print(f'1- {m1[1]} - {m1[2]}')
    print(f'2- {m2[1]} - {m2[2]}')
    print(f'3- {m3[1]} - {m3[2]}')
    print(f'4- {m4[1]} - {m4[2]}')
    print(f'5- {m5[1]} - {m5[2]}')
    print(f'6-pesquisar música')
    resposta = input(' ')
    if resposta == "1":
        salvar_musica(m1[1], m1[2], m1[3], m1[4], m1[5], m1[6])
        tocando()
    elif resposta == "2":
        salvar_musica(m2[1], m2[2], m2[3], m2[4], m2[5], m2[6])
        tocando()
    elif resposta == "3":
        salvar_musica(m3[1], m3[2], m3[3], m3[4], m3[5], m3[6])
        tocando()
    elif resposta == "4":
        salvar_musica(m4[1], m4[2], m4[3], m4[4], m4[5], m4[6])
        tocando()
    elif resposta == "5":
        salvar_musica(m5[1], m5[2], m5[3], m5[4], m5[5], m5[6])
        tocando()
    elif resposta == "6":
        buscar()

#opção de pesquisar uma música
def buscar():
    while True:
        os.system('cls')
        nome = input("Sua Música: ")
        cursor.execute(
            "SELECT * FROM musicas WHERE nome LIKE ?",
            (f"%{nome}%",)
        )
        resultados = cursor.fetchall()
        if resultados:
            print("\nResultados encontrados:\n")
            for i, musica in enumerate(resultados, start=1):
                print(f"{i} - {musica[1]} - {musica[2]}")
                print(f"{musica[4]}")
            escolha = int(input("\nEscolha uma música: "))
            musica_e = resultados[escolha - 1]
            salvar_musica(musica_e[1], musica_e[2], musica_e[3], musica_e[4], musica_e[5], musica_e[6])
            tocando()
            break
        else:
            print("Não há resultados.")
            time.sleep(2)
            Inicio()
            break

#registra a musica escutada no historico do usuário
def salvar_musica(nome, artista, album, duracao, genero, ano):
    Cursor.execute("""
    INSERT INTO musicas (nome, artista, album, duracao, genero, ano)
    VALUES (?, ?, ?, ?, ?, ?)
    """, (nome, artista, album, duracao, genero, ano))
    historico.commit()

#tela de quando a musica está tocando
def tocando():
    while True:
        os.system('cls')
        Cursor.execute(f"""
    SELECT * FROM musicas
    ORDER BY id DESC
    LIMIT 1
    """)
        musica_atual = Cursor.fetchone()
        print(f'Tocando:\n {musica_atual[1]} - {musica_atual[2]}\n{musica_atual[4]}')
        genero = musica_atual[5].lower()
        palavras = genero.split()
        r = input('')
        if r == "1":
            sql = "SELECT * FROM musicas WHERE "
            sql += " OR ".join(["LOWER(genero) LIKE ?" for _ in palavras])
            sql += " ORDER BY RANDOM()\nLIMIT 1"
            parametros = [f"%{palavra}%" for palavra in palavras]
            cursor.execute(sql, parametros)
            mp = cursor.fetchone()
            salvar_musica(mp[1], mp[2], mp[3], mp[4], mp[5], mp[6])
            tocando()
        else:
            Inicio()
            break

def algoritmo1():
            Cursor.execute(f"""
        SELECT * FROM musicas
        ORDER BY id DESC
        LIMIT 1
        """)
            musica = Cursor.fetchone()
            if musica is None:
                cursor.execute(f"""
                SELECT * FROM musicas
                ORDER BY RANDOM()
                LIMIT 1
                """)
                musica = cursor.fetchone()
            genero = musica[5].lower()
            palavras = genero.split()
            sql = "SELECT * FROM musicas WHERE "
            sql += " OR ".join(["LOWER(genero) LIKE ?" for _ in palavras])
            sql += " ORDER BY RANDOM()\nLIMIT 1"
            parametros = [f"%{palavra}%" for palavra in palavras]
            cursor.execute(sql, parametros)
            global m1
            m1 = cursor.fetchone()

def algoritmo2():
            Cursor.execute(f"""
        SELECT * FROM musicas
        ORDER BY id DESC
        LIMIT 1 OFFSET 1
        """)
            musica = Cursor.fetchone()
            if musica is None:
                            cursor.execute(f"""
                            SELECT * FROM musicas
                            ORDER BY RANDOM()
                            LIMIT 1
                            """)
                            musica = cursor.fetchone()
            genero = musica[5].lower()
            palavras = genero.split()
            sql = "SELECT * FROM musicas WHERE "
            sql += " OR ".join(["LOWER(genero) LIKE ?" for _ in palavras])
            sql += " ORDER BY RANDOM()\nLIMIT 1"
            parametros = [f"%{palavra}%" for palavra in palavras]
            cursor.execute(sql, parametros)
            global m2
            m2 = cursor.fetchone()

def algoritmo3():
            Cursor.execute(f"""
        SELECT * FROM musicas
        ORDER BY id DESC
        LIMIT 1 OFFSET 2
        """)
            musica = Cursor.fetchone()
            if musica is None:
                            cursor.execute(f"""
                            SELECT * FROM musicas
                            ORDER BY RANDOM()
                            LIMIT 1
                            """)
                            musica = cursor.fetchone()
            genero = musica[5].lower()
            palavras = genero.split()
            sql = "SELECT * FROM musicas WHERE "
            sql += " OR ".join(["LOWER(genero) LIKE ?" for _ in palavras])
            sql += " ORDER BY RANDOM()\nLIMIT 1"
            parametros = [f"%{palavra}%" for palavra in palavras]
            cursor.execute(sql, parametros)
            global m3
            m3 = cursor.fetchone()

def algoritmo4():
            Cursor.execute(f"""
        SELECT * FROM musicas
        ORDER BY id DESC
        LIMIT 1 OFFSET 3
        """)
            musica = Cursor.fetchone()
            if musica is None:
                            cursor.execute(f"""
                            SELECT * FROM musicas
                            ORDER BY RANDOM()
                            LIMIT 1
                            """)
                            musica = cursor.fetchone()
            genero = musica[5].lower()
            palavras = genero.split()
            sql = "SELECT * FROM musicas WHERE "
            sql += " OR ".join(["LOWER(genero) LIKE ?" for _ in palavras])
            sql += " ORDER BY RANDOM()\nLIMIT 1"
            parametros = [f"%{palavra}%" for palavra in palavras]
            cursor.execute(sql, parametros)
            global m4
            m4 = cursor.fetchone()

def algoritmo5():
            Cursor.execute(f"""
        SELECT * FROM musicas
        ORDER BY id DESC
        LIMIT 1 OFFSET 4
        """)
            musica = Cursor.fetchone()
            if musica is None:
                            cursor.execute(f"""
                            SELECT * FROM musicas
                            ORDER BY RANDOM()
                            LIMIT 1
                            """)
                            musica = cursor.fetchone()
            genero = musica[5].lower()
            palavras = genero.split()
            sql = "SELECT * FROM musicas WHERE "
            sql += " OR ".join(["LOWER(genero) LIKE ?" for _ in palavras])
            sql += " ORDER BY RANDOM()\nLIMIT 1"
            parametros = [f"%{palavra}%" for palavra in palavras]
            cursor.execute(sql, parametros)
            global m5
            m5 = cursor.fetchone()

Inicio()
<<<<<<< HEAD
#teste
=======
>>>>>>> d4b6c65d8353da75cbe727182275dbaffe01672e
