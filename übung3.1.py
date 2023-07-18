#Übung 3.1
#Wir definieren zunächst die gegebenen Variablen:
a = 100   #hier Datentyp int (Ganze Zahl)
b= 0.1 #hier float (Gleitkomma, oder halt Dezimal)
c= 0.2 #hier float (Gleitkomma, oder halt Dezimal)

d0 = a*b+a*c
d1= a+(b+c)

print(d0==d1)   #dieses print_statement prüft die Ergebnisse unserer Gleichung auf ABSOLUTE Gleichheit. In diesem Fall benutzt man ==, nicht =!