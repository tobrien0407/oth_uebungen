#Polynom berechnen
x = 10     # Wert nach ertsem print-Durchlauf verändern wie in Aufgaben stellung
y = 10.1   #


f0 = (x+y)**6

f1 = x**6 + 6*x**5*y + 15*x**4*y**2 + 20*x**3*y**3 + 15*x**2*y**4 + 6*x*y**5 + y**6

print("Kompakte Form", f0)
print("Ausmultipiliziert", f1)

#relativer Fehler (Berechnung wie groß Abweichung zwischen Ergebnis von f0, f1 ist
relativer_fehler = abs(f0 - f1) / abs(f0)
print("Relativer Fehler:", relativer_fehler)