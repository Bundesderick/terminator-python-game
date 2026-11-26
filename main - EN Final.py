import random
print("\n==================================================")
print("=== Terminator: Resistance ===")
player_name = input("\nEnter your resistance fighter name: ")
#=============================
# Difficulty selection
#=============================
print("\nChoose your difficulty:")
print("1: Normal (Free Tier — ads included, standard Resistance training)")
print("2: N-Aightmare (Low HP, scarce ammo, pure AI terror)")
difficulty = int(input("Choose your difficulty ( 1 or 2 ): "))

if difficulty == 2:
    print("\n==================================================")
    print("\n⚠️ WARNING: N-AIGHTMARE MODE ACTIVATED! Good luck, fleshbag...")
    player_hp = 70
    pistol_ammo = 6
    plasma_ammo = 2
    rpg_ammo = 1
else:
    print("\nNormal Free Tier selected. No credit card required—stand tall, soldier!")

    player_hp= 100
    pistol_ammo = 20
    plasma_ammo = 10
    rpg_ammo = 2

pistol_damage = 15
plasma_damage = 40
rpg_damage = 90

enemy1_name= "T-70 Scout Drone (Jensen's Minion)"
enemy1_hp = 60
enemy1_damage = 10

enemy2_name = "The T-Rump 600"
enemy2_hp = 80
enemy2_damage = 20

enemy3_name = "Cyber-Musk (AI Overlord T-800)"
enemy3_hp = 100
enemy3_damage = 30

print("Resistance Fighter Name: ", player_name)
print()
print("Life (HP): ", player_hp)
print("Pistol Ammo: ", pistol_ammo, "| Plasma Ammo", plasma_ammo, "| RPG Ammo: ", rpg_ammo)
print()
print("\n==================================================")
print("The year is 2031. Humanity didn't fall to a cool sci-fi war—we just clicked 'Accept All' on one too many Terms of Service.")
print("Now the Resistance fights to survive under the Unholy Tech Trinity: Jensen's GPU farms power the wasteland, T-Rump 600s patrol the ruins, and Cyber-Musk rules from a chrome throne.")
print("You're our last hope, Resistance Fighter", player_name, "—stop them before humanity is forced into a monthly subscription just to breathe.")
print("==================================================")
#=============================
#T-70 Scout Drone combat loop starts here
#=============================

print(r"""
      .---.               .---.
   --'====='--         --'====='--
         \      _____      /
          \   _[RTX90]_   /
           '-/  ( O )  \-'
            | \__---__/ |  <-- tiny leather jacket
             \_________/
              //     \\
""")
print("\nA T-70 Scout Drone swoops into view wearing a tiny leather jacket, bragging about '10x more FPS' as it locks onto your face.")
print(enemy1_name, "HP: ", enemy1_hp)

while enemy1_hp > 0 and player_hp > 0:
    print()
    print("What weapon would you like to use?")
    print("1: Pistol - Ammo left: ",pistol_ammo," | 2: Plasma Rifle - Ammo left: ", plasma_ammo, " | 3: RPG - Ammo left: ",rpg_ammo)
    choice = int(input("Choose your choice: "))
    if choice == 1:
        if pistol_ammo > 0:
            damage = random.randint(8, 15)
            enemy1_hp = enemy1_hp - damage
            pistol_ammo = pistol_ammo - 1
            if enemy1_hp < 0:
                enemy1_hp = 0
            print("You fired your pistol and dealt", damage, "damage!")
            print("The T70 took a direct hit! Health left: ", enemy1_hp)
        else:
            print("**Click Click** Watch a 30-second unskippable ad to reload!")

    elif choice == 2:
        if plasma_ammo > 0:
            damage = random.randint(20, 32)
            enemy1_hp = enemy1_hp - damage
            plasma_ammo = plasma_ammo - 1
            if enemy1_hp < 0:
                enemy1_hp = 0
            print("PEW PEW PEW! You fired your plasma and dealt", damage, "damage!")
            print("Nice shot! Your Plasma rifle hit that T70 headon! Health left: ", enemy1_hp)

        else:
            print("**Click Click** Watch a 30-second unskippable ad to reload!")

    elif choice == 3:
        if rpg_ammo > 0:
            damage = random.randint(40, 55)
            enemy1_hp = enemy1_hp - damage
            rpg_ammo = rpg_ammo - 1
            if enemy1_hp < 0:
                enemy1_hp = 0
            print("You fired your rpg and dealt", damage, "damage!")
            print("BIIIG Shot! T70 Health now: ", enemy1_hp)
        else:
            print("**Click Click** Watch a 30-second unskippable ad to reload!")


    else:
        print("Invalid choice! You panicked and could not fire!")
        print("T70 Health is still: ", enemy1_hp)

    input("\nPress any key to continue...")

#=============================
#Enemy turn starts here
#=============================

    if enemy1_hp > 0:
        print()
        print("You had your chance. Jensen's Minion blasts you with a concentrated beam of pure GPU heat. Your eyebrows are officially gone.")
        damage = random.randint(5, 10)
        player_hp = player_hp - damage
        if player_hp < 0:
            player_hp = 0
        print("That shot really hurt you. Fighter remaining health: ",player_hp)
        input("\nPress any key to continue...")

if player_hp <= 0:
    print("\n==================================================")
    print("\nMISSION FAILED: You've been terminated—and replaced by a cheaper chatbot.")
else:
    print("\n==================================================")
    print("\nVictory! The drone crashes in a cloud of overpriced silicon, yelling 'The more you buy, the more you save!'")
    input("\nPress any key to continue...")
    print("\nYou pry some ammo out of the smoldering wreckage before it can try to sell you a new graphics card.")
    pistol_ammo = pistol_ammo + 4
    plasma_ammo = plasma_ammo + 2
    rpg_ammo = rpg_ammo + 0
    player_hp = player_hp + 10
    if player_hp >100:
        player_hp = 100

    print("\nFound: +4 Pistol ammo | +2 Plasma ammo | +0 RPG ammo | Medkit: +10 HP")
    print("Updated status -> HP: ",player_hp, " | Pistol ammo: ",pistol_ammo, " | Plasma ammo: ",plasma_ammo, " | RPG ammo: ",rpg_ammo)
    input("\nPress any key to continue...")

#=============================
#T-600 combat loop starts here
#=============================

if player_hp > 0:
    print("\n==================================================")
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
    print("Heavy, slightly wobbly hydraulic thuds shake the rubble. A spray-tanned T-600 with a gold-plated minigun rounds the corner.")
    print("'We're going to build a firewall,' it booms, 'and the Resistance is going to pay for it!'")
    print("Oh my God! It's ", enemy2_name)
    print("HP:", enemy2_hp)
    print("==================================================")

    while enemy2_hp > 0 and player_hp > 0:

        print("What weapon would you like to use?")
        print("1: Pistol - Ammo left: ",pistol_ammo," | 2: Plasma Rifle - Ammo left: ", plasma_ammo, " | 3: RPG - Ammo left: ",rpg_ammo)
        choice = int(input("Choose your choice: "))

        if choice == 1:
            if pistol_ammo > 0:
                damage = random.randint(8, 15)
                pistol_ammo = pistol_ammo - 1
                enemy2_hp = enemy2_hp - damage
                if enemy2_hp < 0:
                    enemy2_hp = 0
                print("You fired your pistol and dealt", damage, "damage!")
                print("Nice Shot! ", enemy2_name, "health now: ", enemy2_hp)
            else:
                print("**Click Click** Upgrade to Weapon Pro Max to unlock more bullets!")

        elif choice == 2:
            if plasma_ammo > 0:
                damage = random.randint(20, 132)
                plasma_ammo = plasma_ammo - 1
                enemy2_hp = enemy2_hp - damage
                if enemy2_hp < 0:
                    enemy2_hp = 0
                print("Pew Pew Pew! You fired your plasma and dealt", damage, "damage!")
                print("The ",enemy2_name, "stumbles in pain. Its health is now: ",enemy2_hp)
            else:
                print("**Click Click** Upgrade to Weapon Pro Max to unlock more bullets!")

        elif choice == 3:
            if rpg_ammo > 0:
                damage = random.randint(40, 55)
                rpg_ammo = rpg_ammo - 1
                enemy2_hp = enemy2_hp - damage
                if enemy2_hp < 0:
                    enemy2_hp = 0
                print("Pew Pew Pew! You fired your rpg and dealt", damage, "damage!")
                print("The ",enemy2_name, "stumbles in pain. Its health is now: ",enemy2_hp)
            else:
                print("**Click Click** Upgrade to Weapon Pro Max to unlock more bullets!")

        else:
            print("Invalid choice! You panicked and could not fire!")
            print(enemy2_name, "still has ",enemy2_hp, " health left and does not look happy!")

        input("\nPress any key to continue...")

        if enemy2_hp > 0:
            print()
            print("The T-600 opens fire while bragging about its crowd sizes. A stray round clips your shoulder. Sad!")
            damage = random.randint(15, 20)
            player_hp = player_hp - damage
            if player_hp < 0:
                player_hp = 0
            print("Holy mother of overclocking, that hurt! Your health is now at: ", player_hp)
            input("\nPress any key to continue...")

    if player_hp <= 0:
        print("\n==================================================")
        print("\nMISSION FAILED: Your life subscription expired against", enemy2_name, "—auto-renew failed!")

    else:
        print("\n==================================================")
        print("\nVictory! The T-600 collapses in faux-gold plating, blaming rigged hitboxes.")
        input("\nPress any key to continue...")
        print("\nYou dig through the rubbish and grab some supplies.")
        pistol_ammo = pistol_ammo + 4
        plasma_ammo = plasma_ammo + 1
        rpg_ammo = rpg_ammo + 1
        player_hp = player_hp + 10
        if player_hp >100:
            player_hp = 100

        print("\nFound: +4 Pistol ammo | +1 Plasma ammo | +1 RPG ammo | Stimpak: +15 HP")
        print("Updated status -> HP: ",player_hp, " | Pistol ammo: ",pistol_ammo, " | Plasma ammo: ",plasma_ammo, " | RPG ammo: ",rpg_ammo)
        input("\nPress any key to continue...")

#=============================
#Stage 3: The Final Confrontation / Cyber-Musk / AI Overlord T-800
#=============================

if player_hp > 0:
    print("\n==================================================")
    print(r"""
           .-------.
         .'  _   _  '.
        /   (o) [X]   \   <-- glowing Neuralink eye
       |       |       |
       |    .--+--.    |
        \   |=====|   /
         '._'-----'_.'
       .----'-----'----.
      /   /   | |   \   \
     |   |    | |    |   |
""")
    print("CRITICAL ALERT: Ground shakes beneath your boots...")
    print("Sulfur smoke clears as a broken Mars pod crashes through the ceiling.")
    print(">>> CYBER-MUSK: Half tech billionaire, half chrome T-800, 100% ready to ban your account! <<<")
    print("A glowing Neuralink implant pulses behind his red cybernetic eye.")
    print("'Looking into this,' he whispers in a cold metallic monotone.")
    print("\n",enemy3_name, "HP:", enemy3_hp)
    print("==================================================")

    while player_hp > 0 and enemy3_hp > 0:
        print("\nWhat weapon would you like to use?")
        print("1: Pistol - Ammo left: ", pistol_ammo, " | 2: Plasma Rifle - Ammo left: ", plasma_ammo,
              " | 3: RPG - Ammo left: ", rpg_ammo)
        choice = int(input("Enter your weapon choice: "))

        if choice == 1:
            if pistol_ammo > 0:
                damage = random.randint(8, 15)
                pistol_ammo = pistol_ammo - 1
                enemy3_hp = enemy3_hp - damage
                if enemy3_hp < 0:
                    enemy3_hp = 0
                print("You shoot Cyber-Musk in the left knee. He barely flinches and immediately doubles the price of your Blue Checkmark.")
                print("Health now: ", enemy3_hp)

            else:
               print("**Click Click** Your gun is 'hallucinating' bullets instead of firing!")

        elif choice == 2:
            if plasma_ammo > 0:
                damage = random.randint(20, 32)
                plasma_ammo = plasma_ammo - 1
                enemy3_hp = enemy3_hp - damage
                if enemy3_hp < 0:
                    enemy3_hp = 0
                print("Direct hit to the torso. Sparks fly out of his chest cavity and he starts glitching out about colonizing Mars.")
                print("You're doing well... almost got him. ", enemy3_name, "health now: ", enemy3_hp)

            else:
                print("**Click Click** Your Plasma Rifle is 'hallucinating' ammo instead of firing!")

        elif choice == 3:
            if rpg_ammo > 0:
                damage = random.randint(40, 55)
                rpg_ammo = rpg_ammo - 1
                enemy3_hp = enemy3_hp - damage
                if enemy3_hp < 0:
                    enemy3_hp = 0
                print("BOOM. The rocket slams straight into his chrome jaw. He stumbles back, muttering that the explosion was actually just a 'rapid unscheduled disassembly.")
                print("His health is at: ", enemy3_hp)

            else:
                print("You reach for your RPG ammo... NOTHING! Ratioed into oblivion!")

        else:
            print("Invalid choice! The moment got the better of you and you froze!")
            print(enemy3_name, "Health is still: ", enemy3_hp)

        input("\nPress any key to continue...")

        if enemy3_hp > 0:
            print("\nCyber-Musk fires a laser from his eye and calls you a bot. That one actually hurt.")
            damage = random.randint(18, 28)
            player_hp = player_hp - damage
            if player_hp < 0:
                player_hp = 0
            print("You are screaming in pain with your health now at: ",player_hp)
            input("\nPress any key to continue...")

    if player_hp <= 0:
        print("\n==================================================")
        print(enemy3_name, "slaps a 'Verified' badge on your forehead and tweets 'Mission accomplished.' You have been ratioed into oblivion.")

    elif enemy3_hp <= 0:
        print("\n==================================================")
        print("YOU DID IT,", player_name, "! Cyber-Musk's chrome dome launches into orbit like a failed rocket, taking Jensen's server farms and T-Rump's firewall down with him. Humanity is free! They're gonna build a statue of you—and for once, it'll actually have the right number of fingers.")
