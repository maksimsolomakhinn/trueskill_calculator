from trueskill import TrueSkill, Rating
import psycopg
from dotenv import load_dotenv
import os

def trueskill_calc():
    #INITIALISE CONNECTION TO DATABASE
    load_dotenv()
    DATABASE_URL = os.getenv("DATABASE_URL")
    conn = psycopg.connect(DATABASE_URL)

    #SETUP THE TRUESKILL ENVIRONMENT
    env = TrueSkill(beta=4.7,
                    tau=0.15,
                    draw_probability=0)
    env.make_as_global()

    #GATHER PLAYER INFO
    players_input = input("Enter race result:").split(",")
    players = [player.strip().capitalize() for player in players_input]

    ffa_teams = []
    new_players = []

    for player in players:
        with conn.cursor() as cur:
            cur.execute("SELECT mu, sigma " \
                        "FROM players " \
                        "WHERE player = %s", 
                        (player,))
            result = cur.fetchone()

            if result:
                mu, sigma = result
                ffa_teams.append((Rating(mu, sigma), ))
            else:
                new_players.append(player)
                ffa_teams.append((Rating(), ))

    #CONFIRM ADDITION OF NEW PLAYERS TO THE RANKINGS

    #EXECUTE TRUESKILL ALGORITHM
    placings = [i for i in range(len(players))]
    updated_teams = env.rate(ffa_teams, ranks=placings)

    #UPDATE DATABASE
    for i in range(len(players)):
        if players[i] in new_players:
            with conn.cursor() as cur:
                cur.execute(
                    """
                    INSERT INTO players (player, mu, sigma)
                    VALUES (%s, %s, %s)
                    """,
                    (players[i], updated_teams[i][0].mu, updated_teams[i][0].sigma)
                )
            conn.commit()

        else:
            with conn.cursor() as cur:
                cur.execute(
                    """
                    UPDATE players
                    SET mu, sigma = (%s, %s)
                    WHERE player = %s
                    """,
                    (players[i], updated_teams[i][0].mu, updated_teams[i][0].sigma)
                )

    print("Results were successfully uploaded")