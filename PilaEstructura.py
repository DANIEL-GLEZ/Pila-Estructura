class Pila:
    def __init__(self, max_tam=8):
        self.max_tam = max_tam
        self.elementos = []
        self.tope = 0  

    def mostrar_pila(self):
        print("\nEstado actual de la pila:")
        for i in range(self.max_tam, 0, -1):
            if i <= self.tope:
                print(f"[ {self.elementos[i - 1]} ]")
            else:
                print("[     ]") 
        print(f"Tope de la pila -> {self.tope}\n")

    def agregar(self, item):
        if self.tope < self.max_tam:
            self.elementos.append(item)
            self.tope += 1
            print(f"Agregado {item}: Estado actual -> {self.elementos}, Tope -> {self.tope}")
            self.mostrar_pila()
        else:
            print(f"Error: No se puede agregar (Desbordamiento){item}. La pila alcanzó su límite máximo.")

    def quitar(self):
        if self.tope > 0:  
            item = self.elementos.pop()
            self.tope -= 1
            print(f"Quitado {item}: Estado actual -> {self.elementos}, Tope -> {self.tope}")
            self.mostrar_pila()
        else:
            print("Error: La pila está vacía (Hay Subdesbordamiento), no hay elementos para quitar.")

mi_pila = Pila()

mi_pila.agregar("X")  # a
mi_pila.agregar("Y")  # b
mi_pila.quitar()      # c
mi_pila.quitar()      # d
mi_pila.quitar()      # e
mi_pila.agregar("V")  # f
mi_pila.agregar("W")  # g
mi_pila.quitar()      # h
mi_pila.agregar("R")  # i


