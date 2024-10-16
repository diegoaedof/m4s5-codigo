# class A:
#     def imprimir(self):
#         print("Imprimiendo A")
    
#     def foo(self):
#         print("metodo clase A")

# class B(A):
#     def __init__(self,b):
#         self.b = b

#     def imprimir(self):
#         print("Imprimiendo B")
#         super().imprimir()


# class C(B,A):
#     def __init__(self, b, c):
#         super().__init__(b)
#         self.c = c

#     def imprimir(self):
#         print("Imprimiendo C")
#         super().imprimir()
    
#     def foo(self):
#         print("metodo clase C")

class A:
    def imprimir(self):
        print("Imprimiendo A")
    
    def foo(self):
        print("metodo clase A")

class B(A):
    def __init__(self,b):
        self.b = b

    def imprimir(self):
        print("Imprimiendo B")
        super().imprimir()


class C(A):
    def __init__(self, c=3):
        self.c = c

    def imprimir(self):
        print("Imprimiendo C")
        #super().imprimir()

class D(B,C):
    def __post_init__(self,c):
        super().__init__(c)

    def imprimir(self):
        print("Imprimiendo D")
        super().imprimir()

obj = B("b")
obj2 = A()
obj3 = C("c")
obj4 = D("b")

print(D.__mro__)
#obj4.imprimir()

print(isinstance(obj3,tuple(A.__subclasses__())))

#obj3.imprimir()

#obj3.imprimir()
#obj.imprimir()
#obj3.foo()

#print(B.__bases__)
#obj2.imprimir()
print(A.__subclasses__())
print(D.__bases__)

print(repr(obj3))