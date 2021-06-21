def reajuste(salario):
    if salario <= 500:
        novo_salario = salario + (salario*(50/100))
    else:
        novo_salario = salario + (salario*(30/100))
    return novo_salario

def main():
    s = float(input('Informe o salário do funcionário: R$'))
    ns = reajuste(s)
    print(f'Após reajuste, o novo salário do funcionário será de R${ns:.2f}')

main()