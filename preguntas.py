"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""
import csv
from collections import Counter
from itertools import count
datos=[]
with open('data.csv') as file:
    lector = csv.reader(file, delimiter='\t')
    for fila in lector:
        datos.append(fila)


def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    con=0
    for fila in datos:
        con=con+int(fila[1])
    return con


def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]

    """
    r=[]
    le=['A','B','C','D','E']
    for i in le:
        cont=0
        for row in datos:
            if row[0]==i:
                cont=cont+1
        r.append((i,cont))


    return (r)

def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]

    """
    r=[]
    le=['A','B','C','D','E']
    for i in le:
        cont=0
        for row in datos:
            if row[0]==i:
                cont=cont+int(row[1])
        r.append((i,cont))


    return (r)

def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """
    meses=[]
    for i in datos:
        fecha=i[2]
        meses.append(str(fecha[5:7]))
    res=[]
    lmes=["01","02","03","04","05","06","07","08","09","10","11","12"]
    for i in lmes:
        res.append((i,meses.count(i)))
    return res

def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """
    res=[]
    let=['A','B','C','D','E']
    for i in let:
        nums=[]
        for j in datos:
            if i==j[0]:
                nums.append(int(j[1]))
        res.append((i,max(nums),min(nums)))
    return(res)

def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """
    valores=[]
    for row in datos:
        spl = row[4].split(",")
        for j in spl:
            valores.append(j)    
    res=[]
    combis=['aaa','bbb','ccc','ddd','eee','fff','ggg','hhh','iii','jjj']
    for i in combis:
        vals=[]
        for j in valores:
            if(i==j[:3]):
                vals.append(int(j[4:]))
        res.append((i,min(vals),max(vals)))
    return (res)


def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """
    let=['A','B','C','D','E']
    nums=['0','1','2','3','4','5','6','7','8','9']
    respuesta=[]
    for n in nums:
        letasociadas=[]
        for row in datos:
            if row[1]==n:
                letasociadas.append(row[0])
        respuesta.append((int(n),letasociadas))
    return (respuesta)

def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """
    let=['A','B','C','D','E']
    nums=['0','1','2','3','4','5','6','7','8','9']
    respuesta=[]
    for n in nums:
        letasociadas=[]
        for row in datos:
            if ((row[1]==n) and row[0] not in letasociadas):
                letasociadas.append(row[0])
        respuesta.append((int(n),sorted(letasociadas)))
    return (respuesta)

def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """
    valores=[]
    for row in datos:
        spl = row[4].split(",")
        for j in spl:
            valores.append(j)    
    
    tripletas=['aaa','bbb','ccc','ddd','eee','fff','ggg','hhh','iii','jjj']
    res={}
    for d in tripletas:
        cont=0 
        for l in valores:
            if(d==l[:3]):
                cont=cont+1
        res.update({d:cont})
    return res

def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]

    """
    res=[]
    for row in datos:
        let=row[0]
        lc4=len(row[3].split(","))
        lc5=len(row[4].split(","))
        res.append((let,lc4,lc5))
    return res

def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }


    """
    lets= ['a','b','c','d','e','f','g']
    nuevo=[]
    for row in datos:
        nuevo.append((row[1],row[3].split(",")))
    
    res={}
    for l in lets:
        cont = 0
        for n in nuevo:
            if(l in n[1]):
                cont += int(n[0])
        res.update({l:cont})
    return res


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """
    res={}
    letras= ['A','B','C','D','E']
    for l in letras:
        tripletas =[]
        contar = 0
        for row in datos:
            if(row[0]==l):
                lista = row[4].split(",")
                for val in lista: 
                    s= val.split(":")
                    contar+=int(s[1])
        res.update({l:contar})
    return res
