from re import S
from time import sleep
import sys
import time
def slowprint(s):
	for c in s + '\n':
		sys.stdout.write(c)
		sys.stdout.flush()
		time.sleep(1./10)

def printsleep(sleeptime, txt):
    sleep(sleeptime)
    print(txt)

slowprint("Gemaakt door")
slowprint("Donny de Vries, Klas 1D")
slowprint("Geniet ervan!!")

printsleep(1.5, "Je staat midden in het bos")
printsleep(1.5, "Het is donker, koud, en akelig stil")
printsleep(1.5, "wat doe je?")
print("A: Je gaat het bos uit.")
print("B: Je gaat een rondje lopen door het bos.")
vraag1 = input("wat ga je doen? ").upper()
if vraag1 == 'A':
    print("\n\nJe loopt het bos uit, en gaat naar huis.")
    printsleep(1.5, "jou verhaal word saai met dit soort keuzes!")
    print("JE OVERLEEFT HET NAAR HUIS, MAAR GAAT DOOD DOOR VERVELING.")
    exit()
elif vraag1 == 'B':
    print("\n\nJe loopt verder door het bos, je bent heel bang, maar geeft nog niet op.")




printsleep(1.5, "Je kijkt veel om je heen, je merkt dat je verdwaald bent.")
printsleep(1.8, "Je raakt gestrest, en begint te zweten. ")
printsleep(3.0, "je ziet een schaduw voorbij vliegen, en wilt erachter aan rennen!")
printsleep(1.5, "wat doe je?")
printsleep(1.5, "A: je blijft waar je bent.")
printsleep(1.5, "B: je rent erachter aan!.")


sleep(2.0); vraag2 = input("Wat wil je gaan doen? ").upper()
if vraag2 == 'A':
    printsleep(1.5, "\n\n Je besluit om stil te blijven staan. ")
    printsleep(1.5, "Het monster vindt je en vermoord je! ")
    printsleep(2.0, "Jammer, volgende keer beter!")
elif vraag2 == 'B':
    printsleep(2.0, "\n\nJe besluit om erachter aan te rennen! ")
    printsleep(2.0, "Je raakt het monster uiteindelijk kwijt, en blijft proberen te zoeken.")
    printsleep(2.0, "Je ziet een verlaten toren!")
    printsleep(1.0, "wat doe je?")
    printsleep(1.5, "A: je betreedt de toren. ")
    printsleep(1.5, "B: Je gaat de toren niet in, en zoekt een uitgang uit het bos. ")

    keuze2 = input("Wat doe je? ").upper()
    if keuze2 == 'A':
        printsleep(1.5, "\n\nJe bent de toren in gelopen.")
        printsleep(1.5, "Je opent de deur en er vallen allemaal dode insecten op je.")
        printsleep(1.5, "Je ziet een trap naar links, en naar rechts.")
        printsleep(1.5, "A: Je loopt de trap naar links op.")
        printsleep(1.5, "B: Je loopt de trap naar rechts op.")

        keuze3 = input("Wat ga je doen? ").upper()
        if keuze3 == 'A':
            printsleep(1.5, "\n\nJe gaat de trap links op.")
            printsleep(1.5, "Je ziet allemaal tekeningen op de muren. ")
            printsleep(1.5, "Je bent aan het einde van de trap, en ziet een deur.")
            printsleep(1.5, "wat doe je? ")
            printsleep(1.5, "A: Je doet de deur open. ")
            printsleep(1.5, "B: Je loopt terug naar beneden. ")

            keuze4 = input("Wat doe je? ").upper()
            if keuze4 == 'A':
                printsleep(1.5, "\n\nJe besluit door de deur heen te gaan.")
                printsleep(1.5, "Je ziet een map liggen.")
                printsleep(1.5, "Je pakt de map en je beleest hem." )
                printsleep(1.5, "Je merkt dat deze map bevloekt is. ")
                printsleep(1.5, "A: Je rent snel terug naar de ingang. ")
                printsleep(1.5, "B: Je verscheurt de map snel.")
                
                keuze5 = input("wat doe je? ").upper()
                if keuze5 == 'A':
                    printsleep(1.5, "\n\nJe rent naar de uitgang in paniek")
                    printsleep(1.5, "Je valt zo van de trap af en breekt je nek, en bloed dood op de grond.")
                    printsleep(1.5, "Jammer, volgende keer beter.")
                elif keuze5 == 'B':
                    print("\n\nJe hebt de map verscheurd en alle kleine stukjes papier vallen op de grond. ")
                    printsleep(1.5, "Uit het niets vliegt het in de vik!")
                    printsleep(1.5, "Je probeert er op te stampen, maar het doet niets, dus je probeert water! ")
                    printsleep(1.5, "A: Je blijft stampen. ")
                    printsleep(1.5, "B: Je gooit een hele fles water erover heen. ")

                    keuze6 = input("Wat is je keuze? ").upper()
                    if keuze6 == 'A':
                        print("\n\nJe blijft erop stampen zo hard als je kan! ")
                        printsleep(1.5, "Het vuur gaat uit. ")
                        printsleep(1.5, "Je raapt de stukjes papier op, en beleest ze nog een keer.")
                        printsleep(1.5, "Je ziet dat er andere tekst op staat!")
                        printsleep(1.5, "Je probeert het goed te lezen. ")
                        printsleep(1.5, "Je kan er geen tekst vanuit maken, en je begint geluiden om je heen te horen.")
                        printsleep(1.5, "Je wordt uit het niets aangevallen door het monster.")
                        printsleep(1.5, "Je begaat een slome en tragische dood.")
                        printsleep(1.5, "Jammer, volgende keer beter!")

                    elif keuze6 == 'B':
                        print("\n\nJe gooit een hele fles water erop. ")
                        printsleep(1.5, "Het vuur gaat uit.")
                        printsleep(1.5, "Je bekijkt de grond.")
                        printsleep(1.5, "Je merkt dat er helemaal geen brandvlekken op de grond zit.")
                        printsleep(1.5, "Je ruikt wel dat het verbrand is.")
                        printsleep(1.5, "Je spuit wat parfum rond. ")
                        printsleep(1.5, "De lucht verdwijnt niet.")
                        printsleep(3.0, "Er komt een sterke lucht naar binnen.")
                        printsleep(3.0, "je word licht in je hoofd en begint duizelig te worden.")
                        printsleep(3.0, "je wilt snel wegrennen.")
                        printsleep(1.5, "A: Je rent snel naar buiten.")
                        printsleep(1.5, "B: je besluit binnen te blijven staan.")

                        keuze7 = input("wat doe je? ").upper()
                        if keuze7 == 'A':
                            print("\n\nje valt in slaap")
                            printsleep(1.5, "*YOU SURVIVED*")
                        elif keuze7 == 'B':
                            print("\n\nJe laat zien dat je dommer bent dat een aardappel en checkt het geluid")
                            printsleep(1.5, "het is de pop van je halicunatie")
                            printsleep(1.5, "je checkt de pop, maar er gebeurd niks")
                            printsleep(1.5, "je loopt naar je bed omdat je besluit te moe te zijn voor meer gekkigheid ")
                            printsleep(1.5, "Je loopt naar je bed maar sterft plots aan een hartaanval")
                            printsleep(1.5, "YOU DIED!")



            elif keuze4 == 'B':
                print("\n\nJe besluit om naar beneden te lopen. ")
                printsleep(3.0, "Je komt beneden aan en ziet een kamer.")
                printsleep(3.0, "Je loopt de kamer in, het is van een kind geweest.")
                printsleep(3.0, "Je kijkt rond in zijn kamer, en je ziet dezelfde schaduw rond rennen!")
                printsleep(3.0, "Je probeert op hem te focusen.")
                printsleep(3.0, "Maar hij beweegt veels te snel, sneller dan een mens kan!")
                printsleep(3.0, "Je probeert jezelf de overtuigen dat je dingen verbeeld.")
                printsleep(3.0, "Je blijft het zien, en dan ben je ervan overtuigd.")
                printsleep(3.0, "Je beeld het je helemaal niet in.")
                printsleep(3.0, "Je blijft door de toren lopen.")
                printsleep(3.0, "Je ziet nog meer kamers.")
                printsleep(3.0, "Je wilt eigenlijk gaan kijken.")
                printsleep(1.5, "A: Je kiest ervoor om niet te gaan kijken.")
                printsleep(1.5, "B: Je besluit te gaan kijken")

                keuze6 = input("wat doe je? ").upper()
                if keuze6 == 'A':
                    print("\n\nJe rent zo snel als je kan naar buiten.")
                    printsleep(1.5, "JE HEBT HET OVERLEEFT!")
                elif keuze6 == 'B':
                    print("\n\nJe blijft binnen staan.")
                    printsleep(1.5, "Je visie begint te draaien en het word wazig.")
                    printsleep(1.5, "De schaduw van eerder loopt naar je toe terwijl je op de grond valt.")
                    printsleep(1.5, "Hij valt je aan, en begint je sloom op te eten. ")
                    printsleep(1.5, "Het beeld word zwart en je gaat langzaam dood.")
                    printsleep(1.5, "Jammer, volgende keer beter.")
        elif keuze3 == 'B':
            printsleep(1.5, "\n\nJe opent de deur en word verast, het is een kleurvolle kamer.")
            printsleep(2.0, "Je loopt naar binnen om het te onderzoeken. ")
            printsleep(2.0, "Het ziet er nog te nieuw uit om verlaten te zijn..")
            printsleep(1.5, "Je vertrouwt het niet meer.")
            print("A: Je verlaat de kamer zo snel als je kan.")
            print("B: Je blijft in de kamer rond kijken.")

            antwoordje1 = input("Wat is je keuze? ").upper()
            if antwoordje1 == 'A':
                print("\n\nJe kiest ervoor om de kamer uit te rennen, en word benaderd door de schaduw, hij eet je sloom op.")
                printsleep(1.5, "Jammer, volgende keer beter.")
            elif antwoordje1 == 'B':
                print("\n\nJe hebt ervoor gekozen om de kamer te onderzoeken.")
                printsleep(1.5, "plotseling staat de schaduw achter, hij laat een zware kast op je vallen, en je gaat dood door de druk.")  
                printsleep(1.5, "Jammer, volgende keer beter.")
    elif keuze2 == 'B':
        printsleep(1.5, "\n\nJe kiest ervoor om buiten te blijven.")
        printsleep(1.5, "Je blijft proberen een uitgang uit het bos te vinden. ")
        printsleep(2.0, "Maar je hebt 0 progressie. ")
        printsleep(1.5, "Wat ga je nu doen?")
        printsleep(1.5, "A Je gaat terug naar de toren. ")
        printsleep(1.5, "B Je blijft staan waar je nu staat. ")

        antwoordje2 = input("Wat is je keuze? ").upper()
        if antwoordje2 == 'A':
            print("\n\nOnderweg naar de toren,")
            printsleep(1.5, "Zie je meerdere schaduwen om je heen.")
            printsleep(1.5, "Je begint te stressen, en begint te rennen.")
            printsleep(1.5, "A: Je rent naar links.")
            printsleep(1.5, "B: Je rent naar rechts.")
            
            antwoordje3 = input("Wat doe je? ").upper()
            if antwoordje3 == 'A':
                print("\n\nJe rent naar links, en word door de groep schaduwen aangevallen.")
                printsleep(1.5, "Jammer, volgende keer beter.")
            elif antwoordje3 == 'B':
                print("\n\nJe rent naar rechts, en word door de groep schaduwen aangevallen. ")
                printsleep(1.5, "Jammer, volgende keer beter.")

        elif antwoordje2 == 'B':
            print("\n\nDe schaduw vind je, en valt je aggresief aan.")
            printsleep(1.5, "Jammer, volgende keer beter.")  