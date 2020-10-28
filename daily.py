
x = int(input("hoeveel geld heb je? : "))

if x <5:
	print("wel erg weinig geld man.")
elif x <20:
	print("is al iets meer maar niet veel.")
elif x <100: 
	print("dat is wel genoeg.")
else:
	print("veel geld man.")

y = int(input("hoe oud ben je? : "))

if y <10:
	print("hmm dat is wel erg jong.")
elif y <15: 
	print("nogsteeds jong maar bijna mijn leeftijd.")
elif y <20:
	print("je zit nu wel bij mijn leeftijd.")
else: 
	print("je bent wel oud man.")

p = int(input("hoeveel kilometer moet je reizen met de trein om op school te komen? : "))
if p <10:
	print("valt wel mee hoever je moet.")
elif p <25:
	print("dat is best wel te doen maar ook wel een beetje lang.")
else:
	print("dat is wel ver man.")

v = int(input("hoeveel uur besteedt je aan huiswerk per dag? : "))
if v <3:
	print("dat is wel genoeg gemiddeld per dag.")
elif v <5:
	print("dat is best wel veel alleen soms is het nodig.")
else: 
	print("dat is echt wel veel man.")

print("je word gebeld tijdens je date met een persoon, 'ik neem op' of 'ik negeer het'? : ")
choice = input()
if choice == 'ik neem op':
	print("je date vind het wel een beetje ongepast maar accepteert het.")
elif choice == 'ik negeer het':
	print("je date vind het aardig dat je de telefoontje negeert en word er blijer van.")
else:
	print(choice, "wrong input")


