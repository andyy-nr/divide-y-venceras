import os
from Clases import Usuario as Us

# Usuarios de prueba, unicamente se puede acceder con estos.
prueba1= Us("1234", "12345678", 876.5)
prueba2 = Us("5678", "98765432", 5683.75)
prueba3 = Us("8523", "11235813", 52.3)
listaUsuarios = [prueba1, prueba2, prueba3]


def validarTarjeta(cuenta, pin):
    ingresado = False
    for usuario in listaUsuarios:
        if usuario.NCuenta == cuenta:
            if len(pin) != 4:
                print("El pin que ingreso no es correcto.")
            else:
                if pin == usuario.Pin:
                    ingresado = usuario
                    return ingresado
                else:
                    print("El pin que ingreso no es correcto.")
    return ingresado


def insertarTarjeta():
    print("Bienvenido")
    nCuenta = input("Por favor, ingrese el numero en su tarjeta\n-> ")
    pin = input("Ingrese su pin (4 digitos)\n-> ")

    usuario = validarTarjeta(nCuenta, pin)
    if not usuario: # si devuelve False es porque la validación fallo
        insertarTarjeta()
    else:
        return usuario # en este caso la validacion fue correcta y usuario contiene los datos de la tarjeta ingresada


def menuPrincipal():
    print("1. Consultar saldo")
    print("2. Depositar")
    print("3. Retirar")
    print("4. Salir")
    opc = int(input("-> "))
    return opc


def consultarSaldo(usuario):
    print(f"Su saldo actual es de: {usuario.Saldo}")


def depositar(usuario):
    monto = int(input("Ingrese el monto a depositar: "))
    usuario.depositar(monto)


def retirar(usuario):
    monto = int(input("Ingrese el monto a retirar: "))
    usuario.retirar(monto)


def apagar():
    apagado = int(input("Presione 1 para apagar el cajero, cualquier otro numero para continuar\n->"))
    if apagado == 1:
        return True
    else:
        return False