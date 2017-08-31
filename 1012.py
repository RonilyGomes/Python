valor = input().split(" ")

a, b, c = valor
pi = 3.14159

triangulo = (float(a) * float(c))/2
circulo = pi * (float(c)* float(c))
trapezio = float(c) *(float(a) + float(b)) / 2
quadrado = float(b) * float(b)
retangulo = float(a) * float(b)


print("TRIANGULO: %.3f\nCIRCULO: %.3f\nTRAPEZIO: %.3f\nQUADRADO: %.3f\nRETANGULO: %.3f" % (triangulo, circulo, trapezio, quadrado, retangulo))
