##Ejercicio 1: Crear un microcatálogo bibliográfico

""" libros = ["La Casa de los espíritus; Isabel Allende; 1982; novela", 
         "Las Cosas que perdimos en el fuego; Mariana Enríquez; 2016; cuentos", 
         "El Complot de los románticos; Carmen Boullosa; 2009; novela", 
         "La Nave de los locos; Cristina Peri; 1984; ficción", 
         "El País de las mujeres; Gioconda Belli; 2010; novela", 
         "La Muerte de Artemio Cruz; Carlos Fuentes; 1962; novela ", 
         "Los Días hábiles; Sergio Gutiérrez; 2020; novela", 
         "Huasipungo; Jorge Icaza; 1934; novela indigenista", 
         "Justo antes del final; Emiliano Monge; 2022; novela", 
         "Un mundo huérfano; Giuseppe Caputo; 2016; novela"]
print(libros) """

libros = ["La Casa de los espíritus; Isabel Allende; 1982; novela", "Las Cosas que perdimos en el fuego; Mariana Enríquez; 2016; cuentos", "El Complot de los románticos; Carmen Boullosa; 2009; novela", "La Nave de los locos; Cristina Peri; 1984; ficción", "El País de las mujeres; Gioconda Belli; 2010; novela", "La Muerte de Artemio Cruz; Carlos Fuentes; 1962; novela ", "Los Días hábiles; Sergio Gutiérrez; 2020; novela", "Huasipungo; Jorge Icaza; 1934; novela indigenista", "Justo antes del final; Emiliano Monge; 2022; novela", "Un mundo huérfano; Giuseppe Caputo; 2016; novela"]

titulos = []
autores = []
anios = []
generos = []

for libro in libros:
    titulos.append(libro.split(';')[0])
    autores.append(libro.split(';')[1])
    anios.append(libro.split(';')[-2])
    generos.append(libro.split(';')[-1])

print(titulos, autores, anios, generos)

    