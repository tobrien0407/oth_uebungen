darlehenskapital = 150000  # Darlehensbetrag in Euro
ezb_leitzinssatz = 0.5  # Offizieller EZB-Leitzinssatz in Prozent (0.5% = 0.005)
erhoehungswert = 1.49  # Erhöhungswert über den EZB-Leitzinssatz in Prozent (1.49% = 0.0149)
kreditlaufzeit = 1  # Laufzeit des Kredits in Jahren

# Umrechnung der Prozentwerte in Dezimalzahlen
ezb_leitzinssatz_decimal = ezb_leitzinssatz / 100
erhoehungswert_decimal = erhoehungswert / 100

# Berechnung des effektiven Zinssatzes
effektiver_zinssatz = ezb_leitzinssatz_decimal + erhoehungswert_decimal

# Berechnung der monatlichen Zinszahlungen
monatlicher_zinsbetrag = (darlehenskapital * effektiver_zinssatz) / 12

print("Monatlicher Zinsbetrag:", monatlicher_zinsbetrag)