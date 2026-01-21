from functions import add_festival, display_season, display_by_artist

def menu(festivals):
    print ("Welcome to the menu!")
    while True:
        print ("Choose one option:")
        print ("1. Add festival")
        print ("2. Display artists during a season")
        print ("3. Display artist's festivals sorted by month")
        print ("4. Exit")
        try:
            o=int(input("Your choice:"))
        except ValueError:
            print("Invalid input. You should choose from 1-4.")
            continue
        if o == 1:
            name = input("Enter the name of the festival:")
            try:
                month = int(input("Enter the month of the festival:"))
                if month < 1 or month > 13:
                    print("Month should be between 1 and 12.")
                    continue
            except ValueError:
                print("Invalid input. You should choose from 1-12.")
                continue
            tc = int(input("Enter the ticket cost:"))
            la = input("Enter the list of artists (comma separated): ").split(",")
            la = [artist.strip() for artist in la]

            add_festival(festivals, name, month, tc, la)
            print("Those are the festivals")
            for f in festivals:
                print(f)

        if o == 2:
            print("Choose the season:")
            print("winter")
            print("spring")
            print("summer")
            print("autumn")
            try:
                season = input("Your choice:")
                if season != "winter" and season != "spring" and season != "summer" and season != "autumn":
                    print("NOt a season. Try again.")
                    continue
            except ValueError:
                print("Invalid input. You should choose a valid season.")
                continue
            result=display_season(festivals, season)

            print("Those are the festivals in this season:")
            for f in result:
                print(f)

        if o == 3:
            la = input("Enter the artist name:")
            result, cnt = display_by_artist(festivals, la, 0)

            if cnt == 0:
                print("The artist does not have any festivals.")
            else:
                print("Those are the festivals in this season:")
                for f in result:
                    print(f)

        if o == 4:
            print("Thanks for your attention! Goodbye!")
            exit()

def console(festivals):
    print("Welcome to the console. Type 'help' to see the comands.")
    while True:
        o = input(" >").strip()
        parts = o.split()
        cmd = parts[0].lower()

        if cmd == "help":
            print ("add <name> <month> <ticket cost> <a list of artists> \n"
                   "show <season> \n"
                   "show <artist>")

        if cmd == "add":
            name = parts[1]
            month = parts[2]
            tc = parts[3]
            la = parts[4]
            add_festival(festivals, name, month, tc, la)

            print("Those are the festivals")
            for f in festivals:
                print(f)

        if cmd == "show":
            if parts[1].lower() == "winter":
                result = display_season(festivals, "winter")
                print("the list:")
                for f in result:
                    print(f)
            elif parts[1].lower() == "spring":
                result = display_season(festivals, "spring")
                print("the list:")
                for f in result:
                    print(f)
            elif parts[1].lower() == "summer":
                result = display_season(festivals, "summer")
                print("the list:")
                for f in result:
                    print(f)
            elif parts[1].lower() == "autumn":
                result = display_season(festivals, "autumn")
                print("the list:")
                for f in result:
                    print(f)
            else:
                result, cnt = display_by_artist(festivals, parts[1], 0)

                if cnt == 0:
                    print("nothing to display")
                else:
                    print("the list:")
                    for f in result:
                        print(f)

if __name__ == "__main__":
    festivals = [{"name": "Untold","month":12, "ticket cost":"500", "a list of artists":["John", "Tom"]},
                 {"name": "BeachPlease","month":5, "ticket cost":"200", "a list of artists":["Cloe"]},
                 {"name": "Start","month":3, "ticket cost":"700", "a list of artists":["Dan", "Sam"]},
                 {"name": "Music","month":2, "ticket cost":"850", "a list of artists":["John", "BigMan", "Tom"]},
                 {"name": "Song","month":7, "ticket cost":"50", "a list of artists":["Tonny"]},
                 {"name": "The Day","month":1, "ticket cost":"450", "a list of artists":["Anna", "Zoe"]},]
    menu(festivals)
    #console(festivals)
