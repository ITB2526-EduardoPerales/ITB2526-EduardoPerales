PWD = "asdasd"
clave = input("Dime la clave:")
intento = 0

while clave != PWD and intento < 2:
    print("Clave incorrecta!!!")
    intento = intento + 1
    clave = input("Dime la clave:")
print("Programa terminado")
#Nuevo commit