l1 = input().split(" ")
l2 = input().split(" ")

qtd1, v1 = l1
qtd2, v2 = l2

total = (int(qtd1) * float(v1)) + (int(qtd2) * float(v2))

print("VALOR A PAGAR: R$ %0.2f" %total)