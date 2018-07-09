import functies as func
import random
import matplotlib.pyplot as plt

# Aantal spelers per generatie
# LET OP: moet een even getal zijn
n = 500

# Aantal generaties
g = 250000

# Maak n spelers aan voor generatie 1
spelers = [random.random() for i in range(n)]

# Bepaal hoe kieskeurig de spelers zijn; onder deze waarde weigeren ze het spel.
kieskeurigheid = [random.random() for i in range(n)]

#Houd een grafiek bij.
speler_historie = []
kieskeurigheid_historie = []

# Ga g generaties na.
for i in range(g):
    if i % 50 == 0:
        print('Nog', g-i, 'te gaan!')

    # Laat de spelers tegen elkaar spelen, en krijg hier bepaalde scores uit.
    resultaat = func.speel_spel(spelers,kieskeurigheid)

    # Aan de hand van deze scores, bepaal welke g/2 spelers gebruikt worden om de nieuwe generatie aan te maken.
    succes_spelers = func.bepaal_succes(resultaat)

    # Print de spelers uit, en print hun score en hun succes/falen.
    func.print_generatie(spelers,resultaat,succes_spelers)

    speler_historie.append(func.bereken_gemiddelde(spelers))
    kieskeurigheid_historie.append(func.bereken_gemiddelde(kieskeurigheid))

    #if i < g - 1:
        #raw_input('Druk op ENTER voor de volgende generatie. ')
    
    # Maak een nieuwe generatie aan.
    spelers = func.genereer_nieuwe_generatie(spelers,succes_spelers,i+1)
    kieskeurigheid = func.genereer_nieuwe_generatie(spelers,succes_spelers,i+1)

plt.ylim(0,1)
plt.plot(range(g),speler_historie,'b-')
plt.plot(range(g),kieskeurigheid_historie,'r-')
plt.show()

print('De optimale variatie is ', speler_historie[-1])
print('De optimale kieskeurigheid is ', kieskeurigheid[-1])
