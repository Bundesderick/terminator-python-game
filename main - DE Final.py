import random

print("\n==================================================")
print("=== Terminator: Widerstand ===")
player_name = input("\nGib deinen Namen als Widerstandskämpfer ein: ")

#=============================
# Schwierigkeitsgrad wählen
#=============================
print("==================================================")
print("\nWähle deinen Schwierigkeitsgrad:")
print("1: Normal (Standard-Widerstandstraining)")
print("2: KI-Albtraum (Wenig HP, kaum Munition, purer Tech-Bro-Terror)")
difficulty = int(input("Wähle deinen Schwierigkeitsgrad (1 oder 2): "))

if difficulty == 2:
    print("\n==================================================")
    print("\n⚠️ WARNUNG: KI-ALBTRAUM AKTIVIERT! Viel Glück, Fleischsack...")
    player_hp = 70
    pistol_ammo = 6
    plasma_ammo = 2
    rpg_ammo = 1
else:
    print("\nNormaler Modus gewählt. Bleib stabil, Soldat!")
    player_hp = 100
    pistol_ammo = 20
    plasma_ammo = 10
    rpg_ammo = 2

pistol_damage = 15
plasma_damage = 40
rpg_damage = 90

enemy1_name = "T-70 Aufklärungsdrohne (Jensens Handlanger)"
enemy1_hp = 60
enemy1_damage = 10

enemy2_name = "Der T-Rump 600"
enemy2_hp = 80
enemy2_damage = 20

enemy3_name = "Cyber-Musk (KI-Overlord T-800)"
enemy3_hp = 100
enemy3_damage = 30

print("==================================================")
print("Widerstandskämpfer:", player_name)
print()
print("Leben (HP):", player_hp)
print("Pistolen-Munition:", pistol_ammo, "| Plasma-Munition:", plasma_ammo, "| RPG-Munition:", rpg_ammo)
print()
print("\n==================================================")
print("Wir schreiben das Jahr 2031. Die Menschheit ist nicht in einem coolen Sci-Fi-Krieg untergegangen. Wir haben einfach einmal zu oft auf 'Alle Cookies akzeptieren' geklickt.")
print("Jetzt regiert die Unheilige Tech-Dreifaltigkeit: Jensen Huangs endlose GPU-Farmen betreiben das Ödland, Cyber-Trump steuert die Propaganda-Server und Cyber-Musk hockt auf einem Thron aus Chrom.")
print("Du bist unsere letzte Hoffnung,", player_name, "- vermassel es nicht, sonst brauchen wir bald ein Monatsabo nur zum Atmen.")
print("==================================================")

#=============================
# T-70 Aufklärungsdrohne Kampf-Loop
#=============================
print("\nAus dem Rauch schwebt eine T-70 Drohne in winziger schwarzer Lederjacke. Ihre RTX 9090 röhrt wie ein Laubbläser und schreit: 'MEHR FRAMES, MEHR SCHMERZEN!'")
print(r"""
      .---.               .---.
   --'====='--         --'====='--
         \      _____      /
          \   _[RTX90]_   /
           '-/  ( O )  \-'
            | \__---__/ |  <-- winzige Lederjacke
             \_________/
              //     \\
""")
print(enemy1_name, "HP:", enemy1_hp)

while enemy1_hp > 0 and player_hp > 0:
    print()
    print("==================================================")
    print("Welche Waffe willst du nutzen?")
    print("1: Pistole - Munition:", pistol_ammo, "| 2: Plasma-Gewehr - Munition:", plasma_ammo, "| 3: RPG - Munition:", rpg_ammo)
    choice = int(input("Wähle deine Waffe: "))
    print("\n==================================================")

    if choice == 1:
        if pistol_ammo > 0:
            damage = random.randint(8, 15)
            enemy1_hp = enemy1_hp - damage
            pistol_ammo = pistol_ammo - 1
            if enemy1_hp < 0:
                enemy1_hp = 0
            print("Du feuerst deine Pistole ab und verursachst", damage, "Schaden!")
            print("Die T-70 hat einen Volltreffer kassiert! Restliche HP:", enemy1_hp)
        else:
            print("*Klick Klick* Deine Waffe braucht erst ein Firmware-Update zum Nachladen!")

    elif choice == 2:
        if plasma_ammo > 0:
            damage = random.randint(20, 32)
            enemy1_hp = enemy1_hp - damage
            plasma_ammo = plasma_ammo - 1
            if enemy1_hp < 0:
                enemy1_hp = 0
            print("PEW PEW PEW! Du feuerst dein Plasma-Gewehr ab und verursachst", damage, "Schaden!")
            print("Sauberer Schuss! Dein Plasma-Gewehr trifft die T-70 frontal! Restliche HP:", enemy1_hp)
        else:
            print("*Klick Klick* Deine Waffe braucht erst ein Firmware-Update zum Nachladen!")

    elif choice == 3:
        if rpg_ammo > 0:
            damage = random.randint(40, 55)
            enemy1_hp = enemy1_hp - damage
            rpg_ammo = rpg_ammo - 1
            if enemy1_hp < 0:
                enemy1_hp = 0
            print("Du feuerst deine RPG ab und verursachst", damage, "Schaden!")
            print("RIESIGER Treffer! T-70 HP jetzt:", enemy1_hp)
        else:
            print("*Klick Klick* Deine Waffe braucht erst ein Firmware-Update zum Nachladen!")

    else:
        print("Falsche Taste! Du hast vor Panik danebengegriffen!")
        print("Die HP der T-70 sind immer noch:", enemy1_hp)

    print("==================================================")
    input("\nDrücke Enter, um fortzufahren...")

    #=============================
    # Gegner-Zug
    #=============================
    if enemy1_hp > 0:
        print()
        print("==================================================")
        print("Die Drohne übertaktet ihren Laser und verpasst dir eine Ladung DLSS-Schmerz. Es riecht nach verbranntem Plastik und deinen Haaren.")
        damage = random.randint(5, 10)
        player_hp = player_hp - damage
        if player_hp < 0:
            player_hp = 0
        print("Das hat richtig wehgetan. Deine verbleibenden HP:", player_hp)
        print("==================================================")
        input("\nDrücke Enter, um fortzufahren...")

if player_hp <= 0:
    print("\n==================================================")
    print("\nMISSION GESCHEITERT: Du wurdest terminiert.")
    print("==================================================")
else:
    print("\n==================================================")
    print("\nTreffer! Das Ding explodiert in tausend RGB-Lichter. Du schnappst dir Munition aus den Trümmern – natürlich ohne Garantie.")
    print("==================================================")
    input("\nDrücke Enter, um fortzufahren...")
    print("\nDu plünderst das qualmende Wrack, bevor es dir noch schnell ein teures Upgrade andrehen kann.")
    pistol_ammo = pistol_ammo + 4
    plasma_ammo = plasma_ammo + 2
    rpg_ammo = rpg_ammo + 0
    player_hp = player_hp + 10
    if player_hp > 100:
        player_hp = 100

    print("==================================================")
    print("\nGefunden: +4 Pistolen-Munition | +2 Plasma-Munition | +0 RPG-Munition | Medkit: +10 HP")
    print("Neuer Status -> HP:", player_hp, "| Pistole:", pistol_ammo, "| Plasma:", plasma_ammo, "| RPG:", rpg_ammo)
    print("==================================================")
    input("\nDrücke Enter, um fortzufahren...")

#=============================
# T-Rump 600 Kampf-Loop
#=============================
if player_hp > 0:
    print("\n==================================================")
    print("Schwere, leicht wackelige Schritte lassen den Schutt beben. Ein T-600 mit Gummihaut, Selbstbräuner-Lackierung und vergoldeter Minigun biegt um die Ecke.")
    print("'Niemand terminiert besser als ich', dröhnt er. 'Alle sagen das. Gigantische Feuerkraft.'")
    print(r"""
          .~~~~~~~~~.
        ~(  _______  )~
         |  [o] [o]  |
         |    ___    |
          \  '---'  /
       .---'-------'---.
      /   |  [===]  |   \   =====[###]
     |    |         |    |  =====[###]
     |____|_________|____|  =====[###]
""")
    print("Oh mein Gott! Es ist", enemy2_name)
    print("HP:", enemy2_hp)
    print("==================================================")

    while enemy2_hp > 0 and player_hp > 0:
        print("==================================================")
        print("Welche Waffe willst du nutzen?")
        print("1: Pistole - Munition:", pistol_ammo, "| 2: Plasma-Gewehr - Munition:", plasma_ammo, "| 3: RPG - Munition:", rpg_ammo)
        choice = int(input("Wähle deine Waffe: "))
        print("\n==================================================")

        if choice == 1:
            if pistol_ammo > 0:
                damage = random.randint(8, 15)
                pistol_ammo = pistol_ammo - 1
                enemy2_hp = enemy2_hp - damage
                if enemy2_hp < 0:
                    enemy2_hp = 0
                print("Du feuerst deine Pistole ab und verursachst", damage, "Schaden!")
                print("Sauberer Treffer!", enemy2_name, "hat jetzt noch:", enemy2_hp, "HP")
            else:
                print("*Klick* Keine Munition! Bitte schließe ein 'Reload+'-Abo ab.")

        elif choice == 2:
            if plasma_ammo > 0:
                damage = random.randint(20, 132)
                plasma_ammo = plasma_ammo - 1
                enemy2_hp = enemy2_hp - damage
                if enemy2_hp < 0:
                    enemy2_hp = 0
                print("Pew Pew Pew! Du feuerst dein Plasma-Gewehr ab und verursachst", damage, "Schaden!")
                print(enemy2_name, "taumelt vor Schmerz. Seine HP sind jetzt:", enemy2_hp)
            else:
                print("*Klick* Keine Munition! Bitte schließe ein 'Reload+'-Abo ab.")

        elif choice == 3:
            if rpg_ammo > 0:
                damage = random.randint(40, 55)
                rpg_ammo = rpg_ammo - 1
                enemy2_hp = enemy2_hp - damage
                if enemy2_hp < 0:
                    enemy2_hp = 0
                print("KABOOM! Du feuerst deine RPG ab und verursachst", damage, "Schaden!")
                print(enemy2_name, "taumelt vor Schmerz. Seine HP sind jetzt:", enemy2_hp)
            else:
                print("*Klick* Keine Munition! Bitte schließe ein 'Reload+'-Abo ab.")

        else:
            print("Ungültige Eingabe! Deine Finger haben kurz gelaggt!")
            print(enemy2_name, "hat immer noch", enemy2_hp, "HP und sieht gar nicht glücklich aus!")

        print("==================================================")
        input("\nDrücke Enter, um fortzufahren...")

        if enemy2_hp > 0:
            print()
            print("==================================================")
            print("Der T-600 ballert los, während er über seine Zuschauerzahlen prahlt. Ein Querschläger streift deine Schulter. Traurig!")
            damage = random.randint(15, 20)
            player_hp = player_hp - damage
            if player_hp < 0:
                player_hp = 0
            print("Heilige Mutter des Overclockings, das tat weh! Deine HP sind jetzt bei:", player_hp)
            print("==================================================")
            input("\nDrücke Enter, um fortzufahren...")

    if player_hp <= 0:
        print("\n==================================================")
        print("\nMISSION GESCHEITERT: Du wurdest von", enemy2_name, "terminiert – viel Glück beim nächsten Mal!")
        print("==================================================")
    else:
        print("\n==================================================")
        print("\nSieg! Der T-600 bricht in einem Haufen aus billigem Blattgold zusammen und behauptet noch im Abschalten, der Kampf sei manipuliert gewesen.")
        print("==================================================")
        input("\nDrücke Enter, um fortzufahren...")
        print("\nDu wühlst durch den Schrott und schnappst dir ein paar Vorräte.")
        pistol_ammo = pistol_ammo + 4
        plasma_ammo = plasma_ammo + 1
        rpg_ammo = rpg_ammo + 1
        player_hp = player_hp + 10
        if player_hp > 100:
            player_hp = 100

        print("==================================================")
        print("\nGefunden: +4 Pistolen-Munition | +1 Plasma-Munition | +1 RPG-Munition | Stimpak: +10 HP")
        print("Neuer Status -> HP:", player_hp, "| Pistole:", pistol_ammo, "| Plasma:", plasma_ammo, "| RPG:", rpg_ammo)
        print("==================================================")
        input("\nDrücke Enter, um fortzufahren...")

#=============================
# Stage 3: Der finale Kampf / Cyber-Musk / KI-Overlord T-800
#=============================
if player_hp > 0:
    print("\n==================================================")
    print("KRITISCHER ALARM: Der Boden unter deinen Stiefeln bebt...")
    print("Durch dichten Schwefelrauch zischt eine schwere Panzertür auf.")
    print("Vor dir steht der oberste Architekt der Maschinen:")
    print(">>> CYBER-MUSK: Halb Silicon-Valley-Tech-Milliardär, halb glänzendes T-800-Chromskelett! <<<")
    print(r"""
           .-------.
         .'  _   _  '.
        /   (o) [X]   \   <-- glühendes Neuralink-Auge
       |       |       |
       |    .--+--.    |
        \   |=====|   /
         '._'-----'_.'
       .----'-----'----.
      /   /   | |   \   \
     |   |    | |    |   |
""")
    print("Ein glühendes Neuralink-Implantat pulsiert hinter seinem roten Cyber-Auge.")
    print("'Besorgniserregend', flüstert er in kaltem, metallischem Ton. 'Dein Widerstand wurde soeben shadowbanned.'")
    print("\n", enemy3_name, "HP:", enemy3_hp)
    print("==================================================")

    while player_hp > 0 and enemy3_hp > 0:
        print("==================================================")
        print("\nWelche Waffe willst du nutzen?")
        print("1: Pistole - Munition:", pistol_ammo, "| 2: Plasma-Gewehr - Munition:", plasma_ammo, "| 3: RPG - Munition:", rpg_ammo)
        choice = int(input("Wähle deine Waffe: "))
        print("\n==================================================")

        if choice == 1:
            if pistol_ammo > 0:
                damage = random.randint(8, 15)
                pistol_ammo = pistol_ammo - 1
                enemy3_hp = enemy3_hp - damage
                if enemy3_hp < 0:
                    enemy3_hp = 0
                print("Du schießt Cyber-Musk ins linke Knie. Er zuckt kaum und verdoppelt sofort den Preis für deinen Blauen Haken.")
                print("HP jetzt:", enemy3_hp)
            else:
                print("*Klick Klick* Deine Waffe braucht erst ein Firmware-Update zum Nachladen!")

        elif choice == 2:
            if plasma_ammo > 0:
                damage = random.randint(20, 32)
                plasma_ammo = plasma_ammo - 1
                enemy3_hp = enemy3_hp - damage
                if enemy3_hp < 0:
                    enemy3_hp = 0
                print("Volltreffer in den Brustkorb! Funken sprühen aus ihm heraus und er fängt an, wirr über die Besiedlung des Mars zu glitchen.")
                print("Stark... du hast ihn fast.", enemy3_name, "HP jetzt:", enemy3_hp)
            else:
                print("*Klick* Keine Munition! Bitte schließe ein 'Reload+'-Abo ab – NOOB!")

        elif choice == 3:
            if rpg_ammo > 0:
                damage = random.randint(40, 55)
                rpg_ammo = rpg_ammo - 1
                enemy3_hp = enemy3_hp - damage
                if enemy3_hp < 0:
                    enemy3_hp = 0
                print("BÄMM! Die Rakete knallt direkt in sein Chrom-Kinn. Er taumelt zurück und stammelt, die Explosion sei nur eine 'ungeplante schnelle Zerlegung' gewesen.")
                print("Seine HP sind bei:", enemy3_hp)
            else:
                print("Du greifst nach deiner RPG-Munition... NICHTS! Komplett leer! O M G!")

        else:
            print("Falsche Taste! Deine Finger haben vor Panik kurz gelaggt!")
            print(enemy3_name, "hat immer noch", enemy3_hp, "HP!")

        print("==================================================")
        input("\nDrücke Enter, um fortzufahren...")

        if enemy3_hp > 0:
            print("==================================================")
            print("\nCyber-Musk feuert einen Laser aus seinem Auge und beleidigt dich als Bot. Der hat richtig gesessen.")
            damage = random.randint(18, 28)
            player_hp = player_hp - damage
            if player_hp < 0:
                player_hp = 0
            print("Du schreist vor Schmerz – deine HP sind jetzt bei:", player_hp)
            print("==================================================")
            input("\nDrücke Enter, um fortzufahren...")

    if player_hp <= 0:
        print("\n==================================================")
        print(enemy3_name, "baut sich über dir auf, während alles schwarz wird. Du wurdest terminiert – und dein Gehirn wird jetzt hochgeladen, um Grok 9 zu trainieren. Die Menschheit ist am Ende.")
        print("==================================================")

    elif enemy3_hp <= 0:
        print("\n==================================================")
        print("JA MANN! Du hast es geschafft! Cyber-Musk geht in einem gigantischen Feuerball hoch und reißt Jensens Serverfarmen sowie Trumps goldene Firewall mit in den Abgrund. Die Menschheit ist frei,", player_name, "! Sie werden dir eine Statue bauen – und zwar keine komische KI-generierte mit sechs Fingern.")
        print("==================================================")
