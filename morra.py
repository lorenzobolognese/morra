#-------------------------------------------------------------------------------
# Name:        morra
# Purpose:
#
# Author:      Lorenzo Bolognese
#
# Created:     25/11/2019
# Copyright:   (c) Lorenzo Bolognese 2019
# Licence:     MIT
#-------------------------------------------------------------------------------

import random

ROUNDS = 100000

RESULTS = ["Draw", "P1 wins", "P2 wins"]
SEEDS = ["Rock", "Paper", "Scissors"]
WINNINGS_P1 = [ [0, 2], [1, 0], [2, 1] ]

def play():
    choice1 = random.randint(0,2)
    choice2 = random.randint(0,2)
    challenge = [choice1, choice2]
    if   choice1 == choice2:        return 0, challenge
    elif challenge in WINNINGS_P1:  return 1, challenge
    else:                           return 2, challenge

if __name__ == '__main__':
    count = [0, 0, 0]
    for i in range(0, ROUNDS):
        res, chlg = play()
        count[res] = count[res] + 1
        print("ROUND " + str(i) + ": P1 = " + SEEDS[chlg[0]] + " vs. P2 = " + SEEDS[chlg[1]] + " --> " + RESULTS[res] )

    idx = 0
    for c in count:
        print(RESULTS[idx] + ": " + str(round((c*100)/ROUNDS, 2)) + "%")
        idx = idx + 1