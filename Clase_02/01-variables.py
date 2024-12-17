# Primer asinacion de Variables
nombre = "Miguelangel"
curso = "Python"
print('mi nombre es',nombre,'estoy en el curso de', curso)

# Lista de 3 cursos
cursos= ['Python','AWS', 'DevOps']
print("1- "+cursos[2])


# Modificamos DevOps por DataOps
cursos[2]='DataOps'
cursos.append("GCP")
print(cursos)


# Mismo pero con Tupla
clase = ('Python','AWS', 'DevOps')
print("3- "+clase[2])

clasesHoras={"Python":"160","AWS":"120","DevOps":"100"}
clasesHoras["Azure"]="40"

print("Las horas de Python son: "+clasesHoras["Azure"])
