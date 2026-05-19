def calcular_tmb(peso:float, altura:float, edad:int, valor_genero:float) -> float:
    valor_genero = 0
    if valor_genero == 5:
       valor_genero = -161

    tmb=(10 * peso) + (6.25 * altura) - (5 * edad) + valor_genero
    return tmb

def CalcularIMC (peso:float, altura:float):
    IMC = peso /(altura*2)
    return round (IMC,2)


def Calculo_de_calorias_en_reposo (peso: int, altura:float , edad:int):
    calorias_en_reposo = (10 * peso) + (6.25 * altura) - (5 * edad) + 5
    return calorias_en_reposo