from connect import *

def order():
    ids = []
    newIDs = []
    count = 1
    indexPos = 0
    rows = cursor.execute("SELECT AnimeID FROM anime").fetchall()
    for id in rows:
        id = list(id)
        ids.append(id[0])
        newIDs.append(count)
        count += 1

        cursor.execute(f"UPDATE anime SET AnimeID = {newIDs[indexPos]} WHERE AnimeID = {ids[indexPos]}")
        conn.commit()

        indexPos += 1

if __name__ == "__main__":
    order()