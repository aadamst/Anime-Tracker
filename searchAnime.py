from connect import *
from time import sleep

def search():  
    fieldName = "Null"
    while fieldName not in ["AnimeID", "Title", "Season", "Genre", "Episodes", "Progress", "Status", "Score"]:
        print(
"""\nWhich field would you like to search in?:
1. ID
2. Title
3. Season
4. Genre
5. Episodes
6. Progress
7. Status
8. Score
"""
        )
        fieldName = input("Enter field to search: ").title()
        if fieldName == "1" or fieldName == "Id":
            fieldName = "AnimeID"
            searchValue = int(input("\nEnter ID to searh: "))

        elif fieldName == "2" or fieldName == "Title":
            fieldName = "Title"
            searchValue = input("\nEnter Title to search: ").title()

        elif fieldName == "3" or fieldName == "Season":
            fieldName = "Season"
            searchValue = int(input("\nEnter Season to search: "))

        elif fieldName == "4" or fieldName == "Genre":
            fieldName = "Genre"
            searchValue = input("\nEnter Genre to search: ").title()

        elif fieldName == "5" or fieldName == "Episodes":
            fieldName = "Episodes"
            searchValue = int(input("\nEnter Episodes to search: "))

        elif fieldName == "6" or fieldName == "Progress":
            fieldName = "Progress"
            searchValue = int(input("\nEnter Progress to search: "))

        elif fieldName == "7" or fieldName == "Status":
            fieldName = "Status"
            searchValue = "Null"
            while searchValue not in ["Watching", "Re-Watching", "Completed", "On Hold", "Dropped", "Plan to Watch"]:
                print(
"""\nPick a Status to search?
1. Watching
2. Re-Watching
3. Completed
4. On Hold
5. Dropped
6. Plan to Watch
"""
                )
                searchValue = input("Enter Status: ").title()
                if searchValue == "1" or searchValue == "Watching":
                    searchValue = "Watching"
                elif searchValue == "2" or searchValue == "Re-Watching":
                    searchValue = "Re-Watching"
                elif searchValue == "3" or searchValue == "Completed":
                    searchValue = "Completed"
                elif searchValue == "4" or searchValue == "On Hold":
                    searchValue = "On Hold"
                elif searchValue == "5" or  searchValue == "Dropped":
                    searchValue = "Dropped"
                elif searchValue == "6" or searchValue == "Plan To Watch":
                    searchValue = "Plan to Watch"
                else:
                    print(f"\n{searchValue} is not a valid choice, please try again.")
                    sleep(2)

        elif fieldName == "8" or fieldName == "Score":
            fieldName = "Score"
            searchValue = "Null"
            while searchValue not in ["-", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]:
                print(
"""\nPick a Score to search?:
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
                searchValue = input("Enter Score: ")
                if searchValue not in ["-", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]:
                    print(f"\n{searchValue} is not a valid choice, please try again.")

        else:
            print(f"{fieldName} is not a valid choice, please try again.")
            sleep(2)

    
    searchValue = f"'{searchValue}'"

    print("\nSearching...")
    sleep(1)
    print("")
    results = ""
    for results in cursor.execute(f"SELECT AnimeID, Title, 'Season: ' || Season, Genre, '(' || Progress || '/' || Episodes || ')', Status, '(' || Score || '/10)'  FROM anime WHERE {fieldName} = {searchValue}"):
        print(results)
    
    if results == "":
        print("No Results :(")


if __name__ == "__main__":
    search()
