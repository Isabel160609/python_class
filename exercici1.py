# Definir una clase Alumno
class Alumno:
    # El método __init__ se ejecuta cuando creamos un nuevo alumno
    def __init__(self, nombre, edad, nota):
        # Estos son los atributos (características) del alumno
        self.nombre = nombre
        self.edad = edad
        self.nota = nota
    
    # Un método es una función que pertenece a la clase
    def presentarse(self):
        print(f"Hola, me llamo {self.nombre} y tengo {self.edad} años")
    
    # Otro método para mostrar la nota
    def mostrar_nota(self):
        print(f"Mi nota es: {self.nota}")
    
    # Método para verificar si aprobó (nota >= 5)
    def aprobo(self):
        if self.nota >= 5:
            print(f"{self.nombre} aprobó con {self.nota}")
        else:
            print(f"{self.nombre} no aprobó con {self.nota}")


# Crear objetos (instancias) de la clase Alumno
alumno1 = Alumno("Juan", 15, 7.5)
alumno2 = Alumno("María", 14, 4.2)

# Usar los métodos de la clase
alumno1.presentarse()
alumno1.mostrar_nota()
alumno1.aprobo()

print()

alumno2.presentarse()
alumno2.mostrar_nota()
alumno2.aprobo()
