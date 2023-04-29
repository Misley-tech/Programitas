class Calc:
    #Una clase es basicamente un conjunto de funciones. Las clases tienen:
    #1) metodos, es lo mismo que una funcion
    #2) atributos, son variables (por ejemplo numeros) 
    def __init__(self,a,b):
        """ 
        __init__ Este es el metodo constructor, sirve para inicializar ("arrancar") 
        las variables que van a usar las funciones que estan dentro de la clase
        """
        # un atributo es una variable definida dentro una clase
        self.a = a # atributo a
        self.b = b # atributo b
    
    def suma(self):
        # el metodo suma, es una funcion comun, que tiene acceso a atributos 
        # y otros metodos definidos dentro de la funcion 
        a = self.a # le asigno a la variable a el atributo self.a 
        b = self.b # le asigno a la variable b el atributo self.b
        return a+b
    
    def resta(self):
        a = self.a
        b = self.b
        return a-b

    def multiplicacion(self):
        a = self.a
        b = self.b
        return a*b

    def raiz(self):
        a = self.a
        b = self.b
        if a != 0:
            return a**(1/2)
        else:
            return b**(1/2)

calculadora = Calc(1,1)
print(calculadora.suma())
