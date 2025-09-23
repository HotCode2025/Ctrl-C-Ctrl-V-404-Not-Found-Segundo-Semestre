def calcular_pago_total(pago_sin_impuesto, impuesto):

    return pago_sin_impuesto + (pago_sin_impuesto * impuesto / 100)

pago_sin_impuesto = 1000
impuesto = 21
pago_total = calcular_pago_total(pago_sin_impuesto, impuesto)
print(f"Pago con impuesto: {pago_total:.2f}")