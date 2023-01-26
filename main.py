from time import sleep
from readAnime import read
from addAnime import insertAnime
from updateAnime import update
from deleteAnime import delete
from swapAnime import swap
from searchAnime import search

def proceed():
    sleep(2)
    input("\nPress Enter to Continue...")
    sleep(1)

def menuOptions():
    option = 0
    availOptions = ["1", "2", "3", "4", "5", "6", "7"]
    while option not in availOptions:
        print(
"""\nAnime List Menu\n
Pick an Option Below:
1. Show Anime List
2. Add an Anime
3. Update an Anime
4. Remove an Anime
5. Swap two Anime Positions
6. Search Anime List
7. Exit Application
        """)
        option = input("What would you like to do?: ")

        if option not in availOptions:
            print(f"\n{option} is not a valid choice, please try again")
            sleep(2)
        
    return option
    
mainProgram = True
while mainProgram:
    mainMenu = menuOptions()
    if mainMenu == "1":
        read()
        proceed()
    elif mainMenu == "2":
        insertAnime()
        proceed()
    elif mainMenu == "3":
        update()
        proceed()
    elif mainMenu == "4":
        delete()
        proceed()
    elif mainMenu == "5":
        swap()
        proceed()
    elif mainMenu == "6":
        search()
        proceed()
    else:
        mainProgram = False
input("\nThanks for using this Application. Press Enter to Quit.")