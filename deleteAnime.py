from connect import *
from readAnime import read, readID, readName
from genList import genIDs, genNames
from time import sleep

def delete():
    ids = genIDs()
    names = genNames()

    deleteRow = "null"
    while deleteRow not in ids and deleteRow not in names:
        deleteRow = input("\nEnter the Name or ID of the Anime you wish to remove: ").title()

        if deleteRow not in ids and deleteRow not in names:
            print(f"\n{deleteRow} is not a valid choice, please try again.")
            sleep(2)

    indexPos = 0
    while deleteRow != names[indexPos] and deleteRow != ids[indexPos]:
        indexPos += 1

    idField = ids[indexPos]


    print(f"\nRemoving {readName(idField)}...")
    sleep(3)

    print(f"\n{readName(idField)} Removed.")
    sleep(2)

    cursor.execute(f"DELETE FROM anime WHERE AnimeID = {idField}")
    conn.commit()

    read()

if __name__ == "__main__":
    delete()