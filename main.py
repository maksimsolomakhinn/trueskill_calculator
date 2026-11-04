from functions.trueskill_calc import trueskill_calc

print("HEAT LEAGUE RANKINGS\nBrought to you by TMM")

if __name__ == "__main__":
    while True:
        print("----------------------")
        

        mode = input("[R]New Race\n[L]Leaderboard\nSelect a function: ")

        print("----------------------")

        if mode.upper() == "R":
            trueskill_calc()

        else:
            print("Invalid input")

        