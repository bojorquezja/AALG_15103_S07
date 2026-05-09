def AlgoritmoVoraz(monedas, vuelto): 
    for moneda in monedas: 
        cantidad = (vuelto + 0.000000001) // moneda
        if cantidad > 0:
            print(f"{cantidad} de S/{moneda} vuelto:{vuelto}")
            vuelto -= (moneda * cantidad)

TiposMonedas = [200, 100, 50, 20, 10, 5, 2, 1, 0.5, 0.2, 0.1, 0.05] 

monto = float(input("Monto a cambiar :"))
cambio = AlgoritmoVoraz(TiposMonedas, monto) 
