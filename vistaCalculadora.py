import calculadora as cal


def InciarApp ():
    opcion = int(input("Digite la opcion a calcular  1. Calcular IMC 2. Calcular TMB 3. Calculo de calorias en reposo 4. calcculo de calorias a adelgazar 5. porcentaje de grasa"))     
    if opcion==1:
        print ("ejecutar calculadora de IMC", cal.calcularIMC)
    elif opcion == 2:
        peso = float(input("Ingrese su peso en kg: "))
        altura = float(input("Ingrese su altura en cm: "))
        edad = int(input("Ingrese su edad en años: "))
        valor_genero = float(input("Ingrese su genero (5 para hombres, -161 para mujeres): "))
        resultado_tmb = cal.calcular_tmb(peso, altura, edad, valor_genero)
        print("Su TMB es:", resultado_tmb)
    elif opcion==3:
        #aqui va a llamar
        print()
    elif opcion==4:
        #aqui va a llamar
        print()
    elif opcion==5:
        #aqui va a llamar
        print()     
    else:
        print("Opcion no valida")
InciarApp()
