# Catalogo

libros = ['Cuentos completos 1; Isaac Asimov; 2009; Ficción', 'Cuentos completos 2; Isaac Asimov; 2009; Ficción', 'De Animales a Dioses; Yuval Noah Harari; 2015; Historia General', 'Homo Deus; Yuval Noah Harari; 2016; Historia General', 'Prohibido Nacer; Trevor Noah; 2017; Autobiografía', 'Somos Luces Abismales; Carolina Sanín; 2018; Ensayos Literarios', 'Muerte con Pingüino; Andrei Kurkov; 1996; Novela', 'Que Viva la Música!; Andrés Caicedo; 1977; Novela']


lis_ani_libros = []
lis_ani_lib_singen = []
sin_genero = []

#___________________________________________________________________________________

for libro in libros:
    lis_ani_libros.append(libro.split(';'))
     

for sin_genero in lis_ani_libros:
    sin_genero.pop()
    lis_ani_lib_singen.append(sin_genero)

prelib =[]

for libro in lis_ani_lib_singen:
    prelib.append("; ".join(libro))

libros = prelib

print(libros)

#___________________________________________________________________________________
# SIN COMANDO .POP

# for libro in libros:
#     lis_ani_libros.append("; ".join(libro.split(';')[0:-1]))

# print(lis_ani_libros)


