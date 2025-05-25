class Producto:
    def __init__(self, id, nombre, stock, categoria, precio, activo = True):
        self.id = id
        self.nombre = nombre
        self.stock = stock
        self.categoria = categoria
        self.precio = precio
        self.activo = activo