import sqlite3
from datetime import datetime
from contextlib import contextmanager

@contextmanager
def get_db_connection():
    conn = sqlite3.connect('cinema.db')
    conn.row_factory = sqlite3.Row
    try:
        yield conn
    finally:
        conn.close()

def init_db():
    with get_db_connection() as conn:
        cursor = conn.cursor()

        # Create tables
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS clientes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT NOT NULL,
            telefone TEXT NOT NULL,
            historico_compras TEXT
        )
        ''')

        cursor.execute('''
        CREATE TABLE IF NOT EXISTS filmes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            duracao INTEGER NOT NULL,
            genero TEXT NOT NULL,
            classificacao_etaria TEXT NOT NULL,
            sinopse TEXT
        )
        ''')

        cursor.execute('''
        CREATE TABLE IF NOT EXISTS salas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            numero INTEGER NOT NULL,
            tipo TEXT NOT NULL,
            capacidade INTEGER NOT NULL
        )
        ''')

        cursor.execute('''
        CREATE TABLE IF NOT EXISTS assentos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            sala_id INTEGER NOT NULL,
            fileira TEXT NOT NULL,
            numero INTEGER NOT NULL,
            ocupado INTEGER DEFAULT 0,
            FOREIGN KEY(sala_id) REFERENCES salas(id)
        )
        ''')

        cursor.execute('''
        CREATE TABLE IF NOT EXISTS sessoes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            filme_id INTEGER NOT NULL,
            sala_id INTEGER NOT NULL,
            horario TEXT NOT NULL,
            data TEXT NOT NULL,
            ingressos_disponiveis INTEGER NOT NULL,
            FOREIGN KEY(filme_id) REFERENCES filmes(id),
            FOREIGN KEY(sala_id) REFERENCES salas(id)
        )
        ''')

        cursor.execute('''
        CREATE TABLE IF NOT EXISTS ingressos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            sessao_id INTEGER NOT NULL,
            assento_id INTEGER NOT NULL,
            preco REAL NOT NULL,
            status TEXT DEFAULT 'disponivel',
            FOREIGN KEY(sessao_id) REFERENCES sessoes(id),
            FOREIGN KEY(assento_id) REFERENCES assentos(id)
        )
        ''')

        cursor.execute('''
        CREATE TABLE IF NOT EXISTS vendas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            cliente_id INTEGER NOT NULL,
            ingresso_id INTEGER NOT NULL,
            data TEXT NOT NULL,
            metodo_pagamento TEXT NOT NULL,
            total REAL NOT NULL,
            FOREIGN KEY(cliente_id) REFERENCES clientes(id),
            FOREIGN KEY(ingresso_id) REFERENCES ingressos(id)
        )
        ''')

        conn.commit() 