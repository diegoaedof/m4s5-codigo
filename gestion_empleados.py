from decoradores import registrar_calculo

class Empleado:
    def __init__(self, nombre, salario):
        self.__nombre = nombre
        self.__salario = salario

    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, valor):
        self.__nombre = valor

    @property
    def salario(self):
        return self.__salario
    
    @salario.setter
    def salario(self,valor):
        self.__salario = valor
    
    @registrar_calculo
    def salario_anual(self):
        return self.__salario * 12
    
    @staticmethod
    def validar_nombre(nombre):
        return nombre.isalpha()
    
    @classmethod
    def desde_cadena(cls,cadena): # "Diego-100" -> "Diego" "100"
        nombre, salario = cadena.split("-")
        return cls(nombre,float(salario))
    
    # def __repr__(self):
    #     return f"Empleado(nombre={self.__nombre}, salario={self.__salario})"


class Gerente(Empleado):

    @registrar_calculo
    def salario_anual(self):
        return self.salario * 12 * 1.1
    


    # def __repr__(self):
    #     return f"Gerente(nombre={self.nombre}, salario={self.salario})"


class EmpleadoRegular(Empleado):

    def __repr__(self):
        return f"EmpleadoRegular(nombre={self.nombre}, salario={self.salario})"


print(Empleado.__subclasses__())
print(Gerente.__bases__)
print(EmpleadoRegular.__bases__)

gerente1 = Gerente("Rodrigo",200)
emp_reg1 = EmpleadoRegular("Fernando",150)

print(gerente1.salario_anual())
print(emp_reg1.salario_anual())

gerente2 = Gerente.desde_cadena("Rodrigo-200")

print(gerente2)
print(gerente1)

# print(Empleado.validar_nombre("Diego3"))
# print(Empleado.validar_nombre("Diego"))
print(gerente1 == gerente2)
