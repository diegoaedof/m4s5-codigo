def registrar_calculo(func):
    def wrapper(*args,**kwargs):
        print(f"Calculando salario para {args[0].nombre}")
        return func(*args,**kwargs)
    return wrapper