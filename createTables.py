from connect import *

cursor.execute(
    """
    CREATE TABLE "anime" (
        "AnimeID" INTEGER NOT NULL UNIQUE,
        "Title" TEXT,
        "Season" INTEGER,
        "Genre" TEXT,
        "Episodes" INTEGER,
        "Progress" INTEGER,
        "Status" TEXT,
        "Score" INTEGER,
        PRIMARY KEY ("AnimeID" AUTOINCREMENT)
    )
    """
)