import sys
print("Hi, wie geht's dir,was führt dich hierher?")
input("")
z = 0
while z == 0:
    print("Schöne Geschichte, aber bist du M oder W?")
    x = input("")
    if x == "W":
        z = 1
    elif x == "M":
        print("Ach da liegt der Haase im Pfeffer \n Tschau")
        sys.exit()
while z == 1:
    print("Hast du kik Ja oder Nein")
    kik = input("")
    if kik == "Ja":
        print("Geil, gib mir mal dein Kik, dann kann ich dir ein Bild von meinem 21 cm Penis schicken")
        z = 2
    elif kik == "Nein":
        print("Na dann müssen wir wohl hier weiter schreiben und ich kann dir kein Bild von meinem Riesending senden.")
        z = 3
    else:
        print("Ich wiederhole!")
while z == 2:
    print("Gibst du mir deinen Kik? Ja oder Nein?")
    givekik = input("")
    if givekik == "Ja":
        print("Herzlichen Glückwunsch, sie haben sich erfolgreich zu einem Bild manovriert")
        print("welches aus einer Googlesuche stammt, viel Spaß damit.")
        sys.exit()
    elif givekik == "Nein":
        print("gut, dann lass hier weiter schreiben, ich hoffe du magt Riesenpenisse, ich habe nämlich einen")
        z = 3
    else:
        z = 2
while z == 3:
    print("Hast du einen festen Freund? Ja oder Nein?")
    boyfriend = input("")
    if boyfriend == "Ja":
        print("du undankbares Weib warst reine Zeiverschwendung!!!!!!!111!!!")
        input("")
        sys.exit()
    elif boyfriend == "Nein":
        z = 4
    else:
        print("sowas gibt es nicht")
while z == 4:
    print("Magst du riesige Penise? Ja oder Nein?")
    rp = input("")
    if rp == "Ja":
        print("Oh, dann wirst du meinen Lieben, den musst du gesehen haben.")
        z = 5
    elif rp == "Nein":
        z = 6
    else:
        print("Was denn nu?")
while z == 5:
    print("Gibst du mir deine Nummer? Dann kann ich dir ein Whastapp Bild senden. Ja oder Nein?")
    wa = input("")
    if wa == "Ja":
        print("Viel SPaß mit deinem Penisbild aus der Google Suche.")
        sys.exit()
    elif wa == "Nein":
        print("Was bist du eigentlich für ein Charakterloses Miststück?")
        input("")
        sys.exit()
    else:
        print("Du hast mich wohl falsch verstanden.")
while z == 6:
    print("Dann bist du entweder eine Charakterlose Lügnerin (jede Frau mag riesenpenisse) oder M")
    print("mit beidem will ich nichts zu tun haben")
    input("")
    sys.exit()