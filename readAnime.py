from connect import *
from time import sleep
from  orderAnime import order

def read():
    order()

    print("\nLoading...\n")
    sleep(1)

    anime = ""
    for anime in cursor.execute("SELECT AnimeID, Title, 'Season: ' || Season, Genre, 'Episodes: ' || Progress || '/' || Episodes, Status, 'Score: ' || Score || '/10' FROM anime"):
        print(anime)

    if anime == "":
        print("No Results :(")


def readID(idField):
    print("")
    for anime in cursor.execute(f"SELECT AnimeID, Title, 'Season: ' || Season, Genre, 'Episodes: ' || Progress || '/' || Episodes, Status, 'Score: ' || Score || '/10' FROM anime WHERE AnimeID = {idField}"):
        print(anime)

    order()

def readName(idField):
    for row in cursor.execute(f"SELECT Title FROM anime WHERE AnimeID = {idField}"):
        row = list(row)
        return row[0]


if __name__ == "__main__":
    read()