# Doel:
# Hoger / Lager spelletje moet als volgt werken.
# De speler wordt een random getal getoond van 1 t/m 10
# De speler moet daarna raden of het volgende random getal hoger of lager wordt
# Aan het einde moet de speler weten of hij/zij gewonnen heeft.

# Stappenplan:
# 1. Een willekeurig nummer van tot 1 t/m 10 maken. 
# 2. De speler voert in of het hoger of lager wordt. 
# 3. Er moet een volgend getal gegenereerd worden.
# 4. Er moet gekeken worden of de speler gelijk heeft.
# 5. De speler moet weten of hij/zij gewonnen of verloren heeft.



import random

willekeur = random.randrange(1, 11)
print(willekeur)

if (input() > willekeur):
    print("lager")