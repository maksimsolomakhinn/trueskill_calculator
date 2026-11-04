from trueskill import TrueSkill, Rating

#SETUP THE TRUESKILL ENVIRONMENT
env = TrueSkill(beta=4.7,
                tau=0.15,
                draw_probability=0)
env.make_as_global()

#GATHER PLAYER INFO
print("ENTER COMMA SEPARATED LIST OF PLAYER PLACEMENTS")
players = input().split(", ")

#EXECUTE TRUESKILL ALGORITHM
ffa_teams = [(Rating(),) for i in range(len(players))]
placings = [i for i in range(len(players))]
updated_teams = env.rate(ffa_teams, ranks=placings)

#PRINT RESULTS
for i in range(len(players)):
    print((players[i], updated_teams[i][0].mu - 3 * updated_teams[i][0].sigma))