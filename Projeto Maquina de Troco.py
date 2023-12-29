valorProduto = float(input("Informe o valor do produto: R$ "))
valorPago = float(input("Informe o valor pago: R$ "))
valorTroco = (valorPago - valorProduto)
cedulas = [200, 100, 50, 20, 10, 5, 2, 1]
centavos = [0.50, 0.25, 0.10, 0.05, 0.01]


if valorPago == 0 or valorProduto ==0:
    print('Não é possível informar valores zerados. Favor informar um valor válido.')
elif (valorPago < valorProduto):
    print(f"Ainda faltam R$ {valorProduto-valorPago:.2f} para completar o valor do produto.")
elif valorPago==valorProduto:
    print(f"O valor do produto foi integralmente pago. Não é necessário retornar troco.")
else:
    print(f"O valor do troco é de R$ {valorTroco:.2f}.")
    print('         ')
    print("Calculando troco para retornar...")
    for nota in cedulas:
        totalNota = int(int(valorTroco) // nota)
        if totalNota > 0:
            print(f"{totalNota} nota(s) de R$ {nota:.2f}.")
            valorTroco -= totalNota * nota
    for moeda in centavos:
        totalMoeda = int(valorTroco / moeda)
        if totalMoeda > 0:
            print(f"{totalMoeda} moeda(s) de R$ {moeda:.2f}.")
            valorTroco -= totalMoeda * moeda