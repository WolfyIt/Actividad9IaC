tamaño = int(input("Ingrese el tamaño de la pirámide (mínimo 3 asteriscos): "))

if tamaño < 3:
  print("El tamaño debe ser mayor o igual a 3")
else:
  for i in range(1, tamaño + 1):
    print(" " * (tamaño - i) + "*" * (2 * i - 1))
