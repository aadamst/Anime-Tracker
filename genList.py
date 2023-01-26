from connect import *

def genIDs():
    ids = []
    for id in cursor.execute("SELECT AnimeID FROM anime"):
        id = list(id)
        id[0] = str(id[0])
        ids.append(id[0])
    
    return ids


def genNames():
    names = []
    for name in cursor.execute("SELECT Title FROM anime"):
        name = list(name)
        names.append(name[0])

    return names