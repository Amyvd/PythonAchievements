print("Hello You!, ik ben Amy.")
print("Wie ben jij?")
naam = input("Typ hier je naam>>")
print("Hello", naam)
print("Ik ben een nieuwkomer op het Mediacollege Amsterdam.") 
print(" Door een aantal vragen over mij te beantwoorden leer je mij beter kennen. ")
print("")

print("Voor dat ik naar het Mediacollege Amsterdam kwam, zat ik op de school \n A. Het Katholieke Scholengemeenschap Hoofddorp \n B. Het Haarlemmermeer Lyceum \n C. Het Kajmunk College.")
print("")
antwoord = input("Kies A, B of C:  ")

if(antwoord == "A"):
	print("Welke nivea heb ik dan gedaan? \n A. Mavo \n B. Havo \n C. Vwo")
	aw = input("Welk nivea heb ik gedaan: ")
	if(aw == "A" or aw == "a"):
		print("het antwoord is correct. ik heb op het Katholieke Scholengemeenschap Hoofddorp gezeten op het nivea mavo.")
	else:
		print("het antwoord is fout!")
elif(antwoord == "B" or antwoord == "b"): 
	print("Welke nivea heb ik dan gedaan? \n A. Mavo \n B. Havo \n C. Vwo")
	aw = input("Welk nivea heb ik gedaan: ")
	if(aw == "A" or aw == "a"):
		print("Het antwoord is goed. Alleen het eerste antwoord is fout ik heb niet ophet Haarlemmermeer lyceum gezeten.")
	else:
		print("het antwoord is fout")
elif(antwoord == "C" or antwoord == "c"):
	print("Welke nivea heb ik dan gedaan? \n A. Mavo \n B. Havo \n C. Vwo")
	aw = input("Welk nivea heb ik gedaan: ")
	if(aw == "A" or aw == "a"):
		print("het antwoord is correct. Alleen het eerste antwoord is fout ik heb niet op het kajmunk College gezeten.")
	else:
		print("Het antwoord is fout.")






