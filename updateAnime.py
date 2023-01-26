from connect import *
from readAnime import read, readID
from genList import genIDs, genNames
from time import sleep

def update():
    ids = genIDs()
    names = genNames()

    changeField = "null"
    while changeField not in ids and changeField not in names:
        changeField = input("\nEnter the Name or ID of the Anime you wish to update: ").title()

        if changeField not in ids and changeField not in names:
            print(f"\n{changeField} is not a valid choice, please try again.")
            sleep(2)

    indexPos = 0
    while changeField != names[indexPos] and changeField != ids[indexPos]:
        indexPos += 1

    idField = ids[indexPos]


    fieldName = "Null"
    while fieldName not in ["Title", "Season", "Genre", "Episodes", "Progress", "Status", "Score"]:
        print(
"""\nWhich field would you like to update?:
1. Title
2. Season
3. Genre
4. Episodes
5. Progress
6. Status
7. Score
"""
        )
        fieldName = input("Enter field to update: ").title()
        if fieldName == "1" or fieldName == "Title":
            fieldName = "Title"
            newFieldValue = input("\nEnter new Title: ").title()

        elif fieldName == "2" or fieldName == "Season":
            fieldName = "Season"
            newFieldValue = int(input("\nEnter new Season: "))

        elif fieldName == "3" or fieldName == "Genre":
            fieldName = "Genre"
            newFieldValue = input("\nEnter new Genre: ").title()

        elif fieldName == "4" or fieldName == "Episodes":
            fieldName = "Episodes"
            newFieldValue = int(input("\nEnter new Episodes: "))

        elif fieldName == "5" or fieldName == "Progress":
            fieldName = "Progress"
            newFieldValue = int(input("\nEnter new Progress: "))

        elif fieldName == "6" or fieldName == "Status":
            fieldName = "Status"
            newFieldValue = "Null"
            while newFieldValue not in ["Watching", "Re-Watching", "Completed", "On Hold", "Dropped", "Plan to Watch"]:
                print(
"""\nWhat's the new Status of this Anime?
1. Watching
2. Re-Watching
3. Completed
4. On Hold
5. Dropped
6. Plan to Watch
"""
                )
                newFieldValue = input("Enter new Status: ").title()
                if newFieldValue == "1" or newFieldValue == "Watching":
                    newFieldValue = "Watching"
                elif newFieldValue == "2" or newFieldValue == "Re-Watching":
                    newFieldValue = "Re-Watching"
                elif newFieldValue == "3" or newFieldValue == "Completed":
                    newFieldValue = "Completed"
                elif newFieldValue == "4" or newFieldValue == "On Hold":
                    newFieldValue = "On Hold"
                elif newFieldValue == "5" or  newFieldValue == "Dropped":
                    newFieldValue = "Dropped"
                elif newFieldValue == "6" or newFieldValue == "Plan To Watch":
                    newFieldValue = "Plan to Watch"
                else:
                    print(f"{newFieldValue} is not a valid choice, please try again.")
                    sleep(2)

        elif fieldName == "7" or fieldName == "Score":
            fieldName = "Score"
            newFieldValue = "Null"
            while newFieldValue not in ["-", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]:
                print(
"""\nWhat do you Score this Anime out of 10?:
(-) Not Yet Scored
(10) Masterpiece
(9) Great
(8) Very Good
(7) Good
(6) Fine
(5) Average
(4) Bad
(3) Very Bad
(2) Horrible
(1) Appalling
"""
        )
                newFieldValue = input("Enter new Score: ")
                if newFieldValue not in ["-", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]:
                    print(f"{newFieldValue} is not a valid choice, please try again.")

        else:
            print(f"{fieldName} is not a valid choice, please try again.")
            sleep(2)

    
    newFieldValue = f"'{newFieldValue}'"
    
    cursor.execute(f"UPDATE anime SET {fieldName} = {newFieldValue} WHERE AnimeID = {idField}")
    conn.commit()
    print(f"\n'{fieldName}' has been updated to {newFieldValue}.")
    sleep(3)

    readID(idField)

if __name__ == "__main__":
    update()