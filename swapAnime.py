from connect import *
from readAnime import read, readName
from orderAnime import order
from genList import genIDs, genNames
from time import sleep

def swap():
    ids = genIDs()
    names = genNames()

    swap1 = "Null"
    while swap1 not in ids and swap1 not in names:
        swap1 = input("\nEnter the Name or ID of the Anime you wish to swap: ").title()

        if swap1 not in ids and swap1 not in names:
            print(f"\n{swap1} is not a valid choice, please try again.")
            sleep(2)

    swap2 = "Null"
    while swap2 not in ids and swap2 not in names:
        swap2 = input("\nEnter the Name or ID of the Anime you wish to swap with: ").title()

        if swap2 not in ids and swap2 not in names:
            print(f"\n{swap2} is not a valid choice, please try again.")
            sleep(2)
    
    indexPos = 0
    while swap1 != names[indexPos] and swap1 != ids[indexPos]:
        indexPos += 1

    idField = ids[indexPos]

    indexPos = 0
    while swap2 != names[indexPos] and swap2 != ids[indexPos]:
        indexPos += 1

    swapID = ids[indexPos]

    print(f"\nSwapping {readName(idField)} with {readName(swapID)}...")
    sleep(2)

    print("\nEntries have been swapped.")
    sleep(2)

    for entry in cursor.execute(f"SELECT Title, Season, Genre, Episodes, Progress, Status, Score FROM anime WHERE AnimeID = {swapID}"):
        entry = list(entry)
    
    cursor.execute(f"DELETE FROM anime WHERE AnimeID = {swapID}")
    conn.commit()

    cursor.execute(f"UPDATE anime SET AnimeID = {swapID} WHERE AnimeID = {idField}")
    conn.commit()

    cursor.execute(f"INSERT INTO anime VALUES({idField}, ?, ?, ?, ?, ?, ?, ?)", entry)
    conn.commit()

    read()

if __name__ == "__main__":
    swap()
