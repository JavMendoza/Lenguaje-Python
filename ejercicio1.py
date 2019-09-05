horaEnSegundos = 3600
diaEnHoras = 24
anioEnDias = 365

nombre = input("Hola. ¿Cual es tu nombre? ")
edad = int(input("¿Cuántos años tenés? "))
peso = int(input("Ok. Última pregunta: ¿cuánto pesás? "))

edadEnSegundos = (horaEnSegundos * diaEnHoras * anioEnDias) * edad  
pesoLuna = round(peso / 9.81 * 1.622, 2)
pesoSol = round(peso / 9.81 * 274, 2)

print("\nSi no te funcionara el Shift, tu nombre se escribiría " + nombre.lower())

print("\nAhora, si tuvieses el Caps Lock trabado, sería " + nombre.upper())

print("\nSi un nene chiquito te quisiera llamar la atención, tu nombre se volvería: " + nombre*5)

print("\nTu edad es de", edadEnSegundos ,"segundos.")

print("\n¿Sabías que en la Luna pesarías sólo", pesoLuna ,"kilos?")

print("\nAhora bien, en el Sol, tu peso sería de", pesoSol ,"(aunque no por mucho...)")

input("\nPresionar enter para continuar...")