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
