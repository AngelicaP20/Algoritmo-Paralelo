class Alumno:
    nombre=""
    apellido= ""

    def NombreCompleto(self):
        return self.nombre + "" + self.apellido


alu = Alumno()
nombre = input("Nombre..:")
apellido = input("Apellido..:")

print(alu.NombreCompleto())