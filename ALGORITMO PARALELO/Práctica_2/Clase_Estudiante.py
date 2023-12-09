class Estudiante:

    def Nom_Estudiante(self, nombre, apellidos, edad, sexo, direccion, carrera, email, telefono):
        return self.nombre + " " + self.apellidos + " , " + self.edad + " , " + self.sexo + " , " + self.direccion + " , " + self.carrera + " , " + self.email + " , " + self.telefono


Estuden = Estudiante()
nombre = input("Nombre..:")
apellidos = input("Apellidos..:")
edad = input("Edad..:")
sexo = input("Sexo..:")
direccion = input("Dirección..:")
carrera = input("Carrera..:")
email = input("Email..:")
telefono = input("Teléfono..:")


print(Estuden.Nom_Estudiante(nombre, apellidos, edad, sexo, direccion, carrera, email, telefono))




    