""""
print ("holaaaaa");

numero = -8

if numero > 9:
    print("El número es positivo")
elif numero < 0:
    print("El número es negativo")
else:
    print("El número es cero")

numeros = [1, 2, 3, 4, 5]
for numero in numeros:
    print(numero)
print("--------------------------")
for numero in range(1, 7):
    print(numero)
print("--------------------------")
numero = 5
while numero >= 1:
    print(numero)
    numero -= 1
print("--------------------------")

x = 1
def clasificar_numero(x):
    opciones = {
        1: "El número es uno",
        2: "El número es dos",
        3: "El número es tres",
        4: "El número es cuatro",
    }
    resultado = opciones.get(x, "El número no está en la lista")
    return resultado

print (clasificar_numero(x))
print("--------------------------")

def es_numero(cadena):
    try:
        float(cadena)
        return True
    except ValueError:
        return False

valor1 = int(input("Ingrese valor a sumar : "))
valor2 = int(input("Ingrese  un segundo valor a sumar : "))

def suma(a, b):
    resultado = a + b
    return resultado

print(suma(valor1, valor2))


def ingresar_numero(mensaje):
    while True:
        valor = input(mensaje)
        if es_numero(valor):
            return float(valor)
        else:
            print("Error: el valor ingresado no es un número válido.")

primer_numero = ingresar_numero("Ingrese el primer número: ")
segundo_numero = ingresar_numero("Ingrese el segundo número: ")
suma = primer_numero + segundo_numero
print("La suma de los dos números es:", suma)

print("--------------------------")

with open("C:\\aqui\\aaaa.txt", "r") as archivo:
    contenido = archivo.read()
    print(contenido)
"""
#ruta_archivo = "C:\\Windows\\notepad.exe" # Ruta del archivo ejecutable del Bloc de notas
#subprocess.Popen(ruta_archivo)


#chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe %s" # Ruta del archivo ejecutable de Chrome

#webbrowser.get(chrome_path).open("https://www.google.com")

#while True:
    #pass

    #driver.save_screenshot("C:\\aqui\\screenshot"+fecha+".png")
    #driver.quit()