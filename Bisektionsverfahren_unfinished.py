# Initiale Intervallgrenzen
x0 = 3.0     #Intervallgrenze 1
x1 = 6.0     #INtervallgrenze 2

# Python-Ausdruck der auszuwertenden Funktion als Zeichenkette (String)
f = "x**3 - 6*x**2 + 4*x + 12"

# Verwende 15 Wiederholungen ("Iterationen")
for n in range(15):            #Hier wird also kleinschrittig 15 mal das gleiche "Halbierungsverfahren" verwendet
    # Berechne die Intervallmitte (d. h. die mittige Zwischenstelle zwischen den Intervallgrenzen)
    x_m = (x0 + x1) / 2

    # Werte die Funktion f(x) an der linken Intervallgrenze x0 aus
    x = x0
    f0 = eval(f)

    # Werte die Funktion f(x) in der Intervallmitte x_m aus
    x = x_m
    f_m = eval(f)

    # Überprüfe das Vorzeichen des Funktionswerts an der Intervallmitte
    # Dies ist der wichtigste Schritt: denn, wenn Vorzeichen an der linken Intervallgrenze (f0) und das Vorzeichen in der Mitte (fx_m) unterschiedlich sind,
    #bedeutet dies ja, dass sich die Nullstelle zwischen diesen zwei Punkten befindet
        
    if f_m * f0 < 0:     
        x1 = x_m    #in diesem Fall: wird x1, also die rechte Intervallgrenze zu x_m transformiert, da die Nullstelle ja jetzt in diesem Intervall liegen muss 
    else:
        x0 = x_m   

    print(n, x_m, f_m)