class Factura:
    def __init__(self, cliente, nit, producto, precio, cantidad):
        self.cliente = cliente
        self.nit = nit
        self.producto = producto
        self.precio = float(precio)
        self.cantidad = int(cantidad)
        self.iva_porcentaje = 0.19 # IVA Colombia

    def calcular_subtotal(self):
        return self.precio * self.cantidad

    def calcular_iva(self):
        return self.calcular_subtotal() * self.iva_porcentaje

    def calcular_total(self):
        return self.calcular_subtotal() + self.calcular_iva()