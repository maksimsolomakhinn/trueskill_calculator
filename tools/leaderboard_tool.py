import psycopg
from dotenv import load_dotenv
import os

def leaderboard_tool():
    #INITIALISE CONNECTION TO DATABASE
    load_dotenv()
    DATABASE_URL = os.getenv("DATABASE_URL")
    conn = psycopg.connect(DATABASE_URL)

    #FETCHES PLAYER DATA
    leaderboard = []

    with conn.cursor() as cur:
        cur.execute("SELECT *" \
                    "FROM players")
        rows = cur.fetchall()

        for row in rows:
            id, name, mu, sigma = row
            rank = mu - 3 * sigma
            leaderboard.append({"Name": name, "Rank" : rank})

    #PRINTS LEADERBOARD
    leaderboard.sort(key=lambda item: item["Rank"], reverse=True)

    for i in range(len(leaderboard)):
        print(f"{i + 1}. {leaderboard[i]["Name"]}")