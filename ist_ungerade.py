#Einführung in funktionen
def ist_ungerade(x):     #Wir definieren eine Funktion, die Prüfen soll, ob eine Zahl gerade oder ungerade ist
    if x % 2 != 0:    #hier haben wir die condition, wenn x modulo 2 nicht NULL ist, die Aussage Wahr getroffen wird
        return True
    else:
        return False #andernfals wird Falsch ausgegeben (also ist die zahl gerade)
    
x=0
result= ist_ungerade(x)
print(result)