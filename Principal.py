import Funciones as fx


def main():
    apagado = fx.apagar()
    if apagado:
        return

    usuario = fx.insertarTarjeta()
    op2 = 0
    while op2 != 4:
        op2 = fx.menuPrincipal()
        if op2 == 1:
            fx.consultarSaldo(usuario)
        elif op2 == 2:
            fx.depositar(usuario)
        elif op2 == 3:
            fx.retirar(usuario)
        elif op2 == 4:
            print("Por favor, retire su tarjeta")
            main()
        else:
            print("La opción que ingresó no es válida")

main()
