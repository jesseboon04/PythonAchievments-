print("Mijn wekker gaat af, wat ga ik doen OPSTAAN en kleren aan trekken, SNOOZE en val dan weer in slaap?")
Choice = input()
if Choice.upper() == "OPSTAAN": 
   print("nu ik ga naar beneden en eten")
elif Choice.upper() == "SNOOZE":
     print("nu ben ik te laat")
else:
    print("keuze is niet goed kies een van de bovenstaande")
    

print("ik heb nu mijn tanden gepoets en mijn spullen gepakt met welk vervoersmiddel ga ik naar het station? een AUTO, FIETS?")
Choice = input()
if Choice.upper() == "AUTO":
      print("ik heb geen rijbewijs dus helaas kan het niet")
elif Choice.upper() == "FIETS":
     print("ja dat klopt")
else:
     print("kies er iut de AUTO of de FIETS")


print("ik zit 35 minuten in de trein naar school, op welk station stap ik uit? op AMSTERDAM CENTRAAL of SLOTERDIJK?")
Choice = input()
if Choice.upper() == "AMSTERDAM CENTRAAL": 
   print("dit is fout want sloterdijk is het dichtsbij")
elif Choice.upper() ==  "SLOTERDIJK":
     print("dat is goed")
else:
    print("kies AMSTERDAM CENTRAAL OF SLOTERDIJK")

print("ik ben nu op het station, ga ik LOPEND naar school of met de BUS?")
Choice = input()
if Choice.upper() == "LOPEND":
   print("ik ga liever met de bus")
elif Choice.upper() == "BUS":
     print(" dit klopt de bus is sneller en kost minder moeite")
else:
    print("dit is fout")


print("Na een hele dag op school te hebben gezeten ga ik naar het station. Ga ik LOPEND of ga ik met de BUS ?")
Choice = input()
if Choice.upper() == "LOPEND": 
   print("Ja dat klopt ik ga liever even een stukje lopen na een hele dag zitten.")
elif Choice.upper == "BUS":
     print("Fout na een hele dag zitte ga ik liever lopen")
else:
    print("kies Volgende keer uit de LOPEND of BUS")
