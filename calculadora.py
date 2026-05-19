def calcular_tmb(peso:float, altura:float, edad:int, valor_genero:float) -> float:
    valor_genero = 0
    if valor_genero == 5:
       valor_genero = -161

    tmb=(10 * peso) + (6.25 * altura) - (5 * edad) + valor_genero
    return tmb
