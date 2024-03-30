


class Carrito:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carrito = self.session.get("carrito")
        if not carrito:
            self.session["carrito"] = {}
            self.carrito = self.session["carrito"]
        else:
            self.carrito = carrito

    def agregar(self, juego):
        if juego.juego_id not in self.carrito.keys():
            self.carrito[juego.juego_id]={
                "producto_id": juego.juego_id,
                "nombre": juego.nombre,
                "acumulado": juego.precio,
                "cantidad": 1,
                

            }
        else:
            self.carrito[juego.juego_id]["cantidad"] += 1
            self.carrito[juego.juego_id]["acumulado"] += juego.precio
        self.guardar_carrito()

    def guardar_carrito(self):
        self.session["carrito"] = self.carrito
        self.session.modified = True

    def eliminar(self, juego):
        
        if juego.juego_id in self.carrito:
            del self.carrito[juego.juego_id]
            self.guardar_carrito()

    def restar(self, juego):
        
        if juego.juego_id in self.carrito.keys():
            self.carrito[juego.juego_id]["cantidad"] -= 1
            self.carrito[juego.juego_id]["acumulado"] -= juego.precio
            if self.carrito[juego.juego_id]["cantidad"] <= 0: self.eliminar(juego)
            self.guardar_carrito()

    def limpiar(self):
        self.session["carrito"] = {}
        self.session.modified = True

    def calcular_total(self):
        total = 0
        for juego_id in self.carrito.values():
            total += juego_id['acumulado']
        return total
    