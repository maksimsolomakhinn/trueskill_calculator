from tools.trueskill_tool import trueskill_tool
from tools.leaderboard_tool import leaderboard_tool
import time

time.sleep(1)
print("HEAT LEAGUE RANKINGS")
time.sleep(1)
print("Presented by TMM")

if __name__ == "__main__":
    while True:
        time.sleep(1)
        print("----------------------")
        time.sleep(1)
        mode = input("[R]New Race\n[L]Leaderboard\nSelect a function: ")
        time.sleep(1)
        print("----------------------")
        time.sleep(1)

        if mode.upper() == "R":
            trueskill_tool()

        elif mode.upper() == "L":
            leaderboard_tool()

        else:
            print("Invalid input")
        