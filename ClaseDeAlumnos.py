
class alumnos_aula_A():
    def __init__(self, nombre, apellido, DNI, merito, materia, nota,inasistencia,amonestacion, domicilio):
#atributos de los alumnos
        self.nombre = nombre
        self.apellido = apellido
        self.DNI = DNI
        self.merito = merito
        self.materia = materia
        self.nota = nota
        self.inasistencia = inasistencia
        self.amonestacion = amonestacion
        self.domicilio = domicilio

#metodos
    def datos(self):
        print (f"Datos de Alumno: nombre: {self.nombre}, apellido {self.apellido}, N° DNI: {self.DNI}, Orden de Merito: {self.merito}, Domilicio: {self.domicilio}")
    def notas (self):
        print (f"La nota de {self.nombre} {self.apellido}, en la materia {self.materia} es: {self.nota}!")
        if self.nota >= 6: 
            print (f"{self.nombre}, lo estas haciendo bien, segui asi!")
        else:
            print (f"{self.nombre}, necesitas esforzarte mas!")
    def inasistencias (self):
        if self.inasistencia >= 1:
            print (f"{self.nombre}, posee {self.inasistencia} inasistencias")
    def direccion (self):
        print (f"el Domicilio de {self.nombre}{self.apellido}, es {self.domicilio}")
    def amonestaciones(self):
        if self.amonestacion >= 1: 
            print (f"{self.nombre}{self.apellido}, tiene {self.amonestacion} amonestaciones, precisa mejorar su conducta")
        else: 
            print (f"{self.nombre}, no posee amonestaciones, segui asi!")
            
            
        
alumno1 = alumnos_aula_A ("Francisco", "Flores", 35194399, 8, "Programacion", 7,1,0,"Florida 1991, Salta")
alumno1.datos()
alumno1.notas()
alumno1.amonestaciones()

alumno2 = alumnos_aula_A ("Federico", "Rocha", 36456789, 8, "Programacion", 5, 2,1,"Avenida Cordoba 1295")
alumno2.datos()
alumno2.inasistencias()
alumno2.notas()

alumno3 = alumnos_aula_A ("Miguel ", "Rodriguez", 39654789, 8, "Analisis 1", 9, 0,3,"calle Buenos Aires 2455")
alumno3.datos()
alumno3.amonestaciones()
alumno3.direccion()
alumno3.inasistencias()
alumno3.notas()

class alumnos_aula_B(alumnos_aula_A):
    def __init__(self, nombre, apellido, DNI, merito, materia, nota,inasistencia,amonestacion, domicilio):
#atributos de los alumnos
        self.nombre = nombre
        self.apellido = apellido
        self.DNI = DNI
        self.merito = merito
        self.materia = materia
        self.nota = nota
        self.inasistencia = inasistencia
        self.amonestacion = amonestacion
        self.domicilio = domicilio
        
alumno6 = alumnos_aula_B ("Sebastian ", "Gonzalez", 34691258, 8, "Filosofia", 4, 1,6,"calle Alvarado 1597")
alumno6.datos()
alumno6.notas()