from connect import *
from readAnime import read
from time import sleep

def insertAnime():
    anime = []

    title = input("\nEnter Anime Title: ").title()
    season = int(input("\nEnter the Anime Season: "))
    genre = input("\nEnter Anime Genre: ").title()
    status = "Null"
    while status not in ["Watching", "Re-Watching", "Completed", "On Hold", "Dropped", "Plan to Watch"]:
        print(
"""\nWhat's the status of this Anime?
1. Watching
2. Re-Watching
3. Completed
4. On Hold
5. Dropped
6. Plan to Watch
"""
        )
        status = input("Enter an option: ").title()
        if status == "1" or status == "Watching":
            status = "Watching"
        elif status == "2" or status == "Re-Watching":
            status = "Re-Watching"
        elif status == "3" or status == "Completed":
            status = "Completed"
        elif status == "4" or status == "On Hold":
            status = "On Hold"
        elif status == "5" or  status == "Dropped":
            status = "Dropped"
        elif status == "6" or status == "Plan To Watch":
            status = "Plan to Watch"
        else:
            print(f"\n{status} is not a valid choice, please try again.")
            sleep(2)

    episodes = input("\nHow many episodes does this Anime have?: ")
    progress = int(input(f"\nEnter your Progress (?/{episodes}): "))
    score = "Null"
    while score not in ["-", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]:
        print(
"""\nWhat do you score this Anime out of 10?:
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
        score = input("Enter your Score: ")
        if score not in ["-", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]:
            print(f"\n{score} is not a valid choice, please try again.")
            sleep(2)


    anime.append(title)
    anime.append(season)
    anime.append(genre)
    anime.append(episodes)
    anime.append(progress)
    anime.append(status)
    anime.append(score)
    ## print(anime)

    cursor.execute("INSERT INTO anime VALUES(NULL, ?, ?, ?, ?, ?, ?, ?)", anime)
    conn.commit()
    print(f"\n{title} has been added to the Anime list.")
    sleep(2)

    read()

if __name__ == "__main__":
    insertAnime()