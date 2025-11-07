CUOTA_FIJA = 6.0
CUOTA_MEDIA = 0.1
CUATO_ALTA = 0.3
try:
    consumo = int(input("Ingresa la cantidad de litros que consumiste este mes:"))
    if consumo < 50 :
        pago = CUOTA_FIJA
    elif 50<= consumo <= 200 :
        pago = (consumo * CUOTA_MEDIA + CUOTA_FIJA)
    else: # consumo > 200 :
        pago = (consumo * CUATO_ALTA + CUOTA_FIJA)

    print(f"Este mes debes pagar: {pago:.2f}€")
except:
    print("La has cagao bacalao")

# Adeemas guarda con el nombre del cliente, pide el nombre del cliente por teclado y agregalo al archivo XML
nombre_cliente = input("Ingresa el nombre del cliente:")
with open("factura.xml", "w") as archivo:
    archivo.write(f"<factura>\n")
    archivo.write(f"  <cliente>{nombre_cliente}</cliente>\n")
    archivo.write(f"  <consumo>{consumo}</consumo>\n")
    archivo.write(f"  <pago>{pago:.2f}</pago>\n")
    archivo.write(f"</factura>\n")

