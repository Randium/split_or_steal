import random
import math

def speel_spel(spelers,kieskeurigheid):
    # Maak een scoretabel aan.
    score_tabel = [0 for i in range(len(spelers))]

    # Laat elke speler tegen vijf willekeurige spelers spelen.
    for i in range(len(spelers)):

        for j in range(len(spelers)):

            # Ga na of beide spelers WILLEN spelen (en het team niet tegen zichzelf speelt).
            if spelers[i] > kieskeurigheid[j] and spelers[j] > kieskeurigheid[i] and i!=j:
                speler1 = spelers[i]
                speler2 = spelers[j]

                # Laat beide spelers een keuze maken.
                keuze_1 = random.random()
                keuze_2 = random.random()

                # Als een speler steelt, gebeurt er niks.
                # Ga daarom enkel na wat er gebeurt wanneer een speler split.
                if keuze_1 < speler1:
                    score_tabel[j] += 1
                    if keuze_2 > speler2:
                        score_tabel[j] += 99
                if keuze_2 < speler2:
                    score_tabel[i] += 1
                    if keuze_1 > speler1:
                        score_tabel[i] += 99
    
    return score_tabel

def bepaal_succes(resultaat):
    waarde_tabel = []

    for i in range(len(resultaat)):
        speler_tabel = [resultaat[i],i]
        waarde_tabel.append(speler_tabel)
    
    waarde_tabel.sort()

    return [waarde_tabel[-i-1][1] for i in range(len(resultaat)/2)]

def print_generatie(spelers,resultaat,succes_spelers):
    return True

def genereer_nieuwe_generatie(spelers,succes_spelers,g):
    nieuwe_generatie = []

    for i in succes_spelers:
        p = spelers[i]
        if p > 0.5:
            p = 1 - p
        
        x = max(g,2)

        afwijking = (random.random()-0.5) * p/math.log(x,2)
        nieuwe_generatie.append(p + afwijking)
        afwijking = (random.random()-0.5) * p/math.log(x,2)
        nieuwe_generatie.append(p + afwijking)
    
    return nieuwe_generatie

def bereken_gemiddelde(tabel):
    sum = 0

    for n in tabel:
        sum += n
    
    return float(sum) / len(tabel)
