print("Esto es una herramienta para clacular la suma de números pares\n ")
print("Ingrese el número inicial: ")
i= int(input())
print("Ingrese el número final")
f= int(input())
suma=0
print( "Los números pares del rango")
while i <=f :
    if i%2 ==0:
        print(i)
        suma= i + suma
    i+=1 
print("La suma de tus números pares en el rango indicado es : ", suma)


