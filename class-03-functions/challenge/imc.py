def calc_imc(height, weight):
    imc = weight / (height * height)
    return imc


height = float(input("digite sua altura em metros: "))
weight = float(input("digite seu peso em kilogramas: "))


# print(calc_imc(1.80, 80))
print(f" seu imc é: {calc_imc(height, weight):.2f}!")