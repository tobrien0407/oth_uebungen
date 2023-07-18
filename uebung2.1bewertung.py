punktzahl = float(input("Bitte geben sie die Punktzahl ein.")) #Hier wird nach Ausführung des Codes im Terminal nach einer Punktzahl gefragt
#Der Datentyp float diehnt hierbei Dezimaldarstellungen (bspw. 66.5 Punkte als input erlaubt)
#Die Variable punktzahl wird also von uns selbst definiert und eingegeben 

if punktzahl >= 82: #hier die erste Kondition: Wenn Punktzahl, dann 
    print("Hervorragend!") #print Befehl dient der Ausgabe, also wenn, dann Ausgabe
elif punktzahl>=76.5: #elif ist sozusagen eine Alternativmöglichkeit mit anderer Kondition und Ausgabe
        print("Sehr gut")
elif punktzahl >= 66:
        print("Gut")
elif punktzahl >=45:
        print("Da ist noch Luft nach oben!")
else: print("Haben sie es überhaupt versucht") # Alles was kleiner als 45 ist
    

        