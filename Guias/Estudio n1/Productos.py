class Producto:
    def __init__(self, nombre, precio, cantidad, codigoBarra):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
        self.codigoBarra = codigoBarra
        self.historial_stock = [] 


    def actualizar_stock(self, cambio): #El cambio puede ser positivo o negativo
        self.cantidad += cambio
        self.historial_stock.append(cambio)

    def total(self):
        return self.precio * self.cantidad

    def __str__(self): #Regresa el estado del producto
        return (f"Producto: {self.nombre} | Código: {self.codigo} | "
                f"Precio: ${self.precio:.2f} | Cantidad: {self.cantidad} | "
                f"Valor Total: ${self.valor_total():.2f}")


class Inventario:
    def __init__(self):
        self.productos = {}
        
    def agregar(self, producto):
        
        if producto.codigo in self.productos:
            print(f"⚠️ El producto con código {producto.codigo} ya existe.")
        else:
            self.productos[producto.codigo] = producto
            print(f"Producto '{producto.nombre}' agregado al inventario.")



    def actualizar(self, codigo, cambio):

        if codigo in self.productos:
            self.productos[codigo].actualizar_stock(cambio)
            print(f"Stock actualizado para {self.productos[codigo].nombre}.")
        else:
            print(f"El código |{codigo}| no pertenece a ningun producto.")

    def mostrar(self):
        if not self.productos:
            print("inventario vacío.")
        else:
            for producto in self.productos.values():
                print(producto)

    def total_inventario(self):
        return sum(p.valor_total() for p in self.productos.values())