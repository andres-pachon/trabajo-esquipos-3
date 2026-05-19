#aqui van todas las funciones 

def CalcularIMC (peso:float, altura:float):
    IMC = peso /(altura*2)
    return round (IMC,2)