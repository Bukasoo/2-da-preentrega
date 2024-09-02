class Cliente:
    def __init__(self, nombre, apellido, email, telefono):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.telefono = telefono

    def actualizar_email(self, nuevo_email):
        self.email = nuevo_email

    def actualizar_telefono(self, nuevo_telefono):
        self.telefono = nuevo_telefono

    def __str__(self):
        return f"Cliente: {self.nombre} {self.apellido}, Email: {self.email}, Teléfono: {self.telefono}"