# Definición de la clase CajeroAutomatico
class CajeroAutomatico1:
    def __init__(self, saldo_inicial):
        self.saldo = saldo_inicial

    def depositar(self, monto):
        self.saldo += monto
        return f"Depósito exitoso. Saldo actual: {self.saldo}"

    def retirar(self, monto):
        if self.saldo >= monto:
            self.saldo -= monto
            return f"Retiro exitoso. Saldo actual: {self.saldo}"
        else:
            return "Saldo insuficiente"

# Crear una instancia del CajeroAutomatico con saldo inicial de 1000
cajero = CajeroAutomatico1(1000)

# Ejemplos de operaciones
print(cajero.depositar(500))
print(cajero.retirar(200))