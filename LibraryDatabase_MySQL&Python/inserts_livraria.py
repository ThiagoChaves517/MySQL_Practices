from mysql.connector import MySQLConnection, Error
from config import read_config

def insert_author(cursor, nome, data_nasc, pais_nasc, nota_biografica):
    query = "INSERT INTO Autor(nome, data_nasc, pais_nasc, nota_biografica) " \
            "VALUES(%s,%s,%s,%s)"

    args = (nome, data_nasc, pais_nasc, nota_biografica)
    autor_id = None
    try:
        cursor.execute(query, args)
        autor_id =  cursor.lastrowid
    except Error as error:
        print(error)
    return autor_id

def insert_book(cursor, nome, lingua, ano):
    query = "INSERT INTO Livro(nome, lingua, ano) " \
            "VALUES(%s,%s,%s)"

    args = (nome, lingua, ano)
    book_id = None
    try:
        cursor.execute(query, args)
        book_id =  cursor.lastrowid
    except Error as error:
        print(error)
    return book_id

def insert_editor(cursor, nome, telefone, endereco):
    query = "INSERT INTO Editora(nome, telefone, endereco) " \
            "VALUES(%s,%s,%s)"

    args = (nome, telefone, endereco)
    editor_id = None
    try:
        cursor.execute(query, args)
        editor_id =  cursor.lastrowid
    except Error as error:
        print(error)
    return editor_id

def insert_edition(cursor, ISBN, preco, ano, num_paginas, id_livro, id_editora, quant_estoque):
    query = "INSERT INTO Edicao(ISBN, preco, ano, num_paginas, id_livro, id_editora, quant_estoque) " \
            "VALUES(%s,%s,%s,%s,%s,%s,%s)"

    args = (ISBN, preco, ano, num_paginas, id_livro, id_editora, quant_estoque)
    edition_id = None
    try:
        cursor.execute(query, args)
        edition_id =  cursor.lastrowid
    except Error as error:
        print(error)
    return edition_id

def insert_in_the_write_table(cursor, id_livro, id_autor):
    query = "INSERT INTO Escreve(id_livro, id_autor) " \
            "VALUES(%s,%s)"

    args = (id_livro, id_autor)
    write_id = None
    try:
        cursor.execute(query, args)
        write_id =  cursor.lastrowid
    except Error as error:
        print(error)
    return write_id