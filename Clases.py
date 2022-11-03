class Usuario:
    def __init__(self, pin, numCuenta, saldo):
        self.Pin = pin
        self.NCuenta = numCuenta
        self.Saldo = saldo


    def __str__(self):
        return   f"Usuario" \
                 f"Numero de cuenta: {self.NCuenta}" \
                 f"Pin: {self.Pin}" \
                 f"Saldo disponible: {self.Saldo}"


    def depositar(self, deposito):
        if deposito % 100 == 0:
            self.Saldo = self.Saldo + deposito
            print("Transacción realizada exitosamente")
        else:
            print("Por favor, intente de nuevo. Recuerde ingresar un multiplo de 100")


    def retirar(self, retiro):
        if retiro % 100 == 0 and retiro < self.Saldo:
            self.Saldo = self.Saldo - retiro
            print("Transacción realizada exitosamente")
        else:
            print("Por favor, intente de nuevo. \nVerifique que el numero ingresado sea multiplo de 100"
                  " O que el monto a retirar es menor que su saldo actual")


    def validarPin(self, pin):
        if len(pin) != 4:
            print("El pin que ingreso no es correcto.")
            return False
        else:
            if pin == self.Pin:
                return True
            else:
                print("El pin que ingreso no es correcto.")
                return False