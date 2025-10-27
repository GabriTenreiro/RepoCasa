alumnos = [
    {"nombre": "Laura", "notas": [8, 7, 9]},
    {"nombre": "Gabriel", "notas": [5, 3, 8]}
]

def añadir(alumnos, nombre, notas):
    nuevo = {"nombre": nombre, "notas": notas}
    alumnos.append(nuevo)
    return alumnos

añadir(alumnos,'Javier',[2,3,4])
contador=1
for x in alumnos:
    print(f'Alumno {contador} : {x}')
    contador += 1

def mediaAlumno():    
    for x in alumnos:
        notas=x['notas']
        media=sum(notas)/len(notas)
        print(f'La media de  {x["nombre"]} es de {media:.2f}')

        
mediaAlumno()
