class huesped:
    def _init_(self, cedula, nombre, habitacion):
        self.nombre = nombre
        self.cedula = cedula
        self.habitacion = habitacion
        self.siguiente = None
        
class habitacion:
    def _init_(self,numero):
        self.numero = numero
        self.ocupada = False
        self.siguiente = None
        
class hotel:
    def _init_(self):
        self.lista_de_huespedes = None
        self.lista_de_habitaciones = None
        
    def agregar_huesped(self, cedula, nombre, habitacion):
        nuevo_huesped = huesped(cedula, nombre, habitacion)
        nuevo_huesped.siguiente = self.lista_de_huespedes
        self.lista_de_huespedes = nuevo_huesped
        
    def registrar_habitacion_ocupada(self, numero_habitacion ):
        actual = self.lista_de_habitaciones
        while actual:
            if actual.numero == numero_habitacion:
                actual.ocupada = True
                break
            actual = actual.siguiente
            
    def consultar_indivudual(self,cedula):
        actual = self.lista_de_huespedes
        while actual:
            if actual.cedula == cedula:
                return f" Cedula: {actual.cedula}, Nombre: {actual.nombre}, habitacion: {actual.habitacion}"
            actual = actual.siguiente
        return "Huesped no encontrado"
    
    def consultar_huespedes_totales_cedula(self, cedula):
        resultados = []
        actual = self.lista_de_huespedes
        while actual:
            if actual.cedula == cedula:
                resultados.append(f" Cedula: {actual.cedula}, Nombre: {actual.nombre}, habitacion: {actual.habitacion}")
            actual = actual.siguiente
        return resultados
    
    def consultar_huespedes_totales_orden_llegada(self):
        resultados = []
        actual = self.lista_de_huespedes
        while actual:
            resultados.append(f" Cedula: {actual.cedula}, Nombre: {actual.nombre}, habitacion: {actual.habitacion}")
            actual = actual.siguiente
        return resultados
    
    def consultar_habitaciones_disponibles(self):
        disponibles = []
        actual = self.lista_de_habitaciones
        while actual:
            if not actual.ocupada:
                disponibles.append(actual.numero)
            actual = actual.siguiente
        return disponibles

    def consultar_habitaciones_ocupadas(self):
        ocupadas = []
        actual = self.lista_de_habitaciones
        while actual:
            if actual.ocupada:
                ocupadas.append(actual.numero)
            actual = actual.siguiente
        return ocupadas

hotel = hotel()
hotel.lista_de_habitaciones = habitacion(101)
hotel.lista_de_habitaciones.siguiente = habitacion(102)
hotel.lista_de_habitaciones.siguiente.siguiente = habitacion(103)

hotel.agregar_huesped("12345", "Sergio", 101)
hotel.agregar_huesped("98765", "Diego", 102)

print("Habitaciones Disponibles:", hotel.consultar_habitaciones_disponibles())
print("Habitaciones Ocupadas:", hotel.consultar_habitaciones_ocupadas())
print("Consulta Huesped Individual:", hotel.consultar_indivudual("12345"))
print("Consulta Huespedes Totales por Cédula:", hotel.consultar_huespedes_totales_cedula("12345"))
print("Consulta Huespedes Totales por Orden de Llegada:", hotel.consultar_huespedes_totales_orden_llegada())