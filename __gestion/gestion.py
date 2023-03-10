import pandas as pd
import os

excel = pd.read_excel(os.path.join('__conf/lista_clase.xlsx'), sheet_name='Resumen de lista de clase')

estudiantes = excel.loc[14:24, ['Información de curso']]

os.makedirs('estudiantes', exist_ok=True)
os.mkdir(os.path.join('estudiantes', 'Ejemplo'))
with open(os.path.join('estudiantes', 'Ejemplo', 'README.md'), 'w') as readme:
    readme.write('# Ejemplo')

for estudiante in estudiantes['Información de curso']:
    estudiante = estudiante.title()
    estudiante = estudiante.split(',')
    estudiante = estudiante[1].strip() + ' ' + estudiante[0].strip()
    estudiante = estudiante.replace('ñ', 'n')

    try:
        os.mkdir(os.path.join('estudiantes', estudiante))
        with open(os.path.join('estudiantes', estudiante, 'README.md'), 'w') as readme:
            readme.write(f'# {estudiante}')
    except FileExistsError:
        print('El directorio ya fue creado')
