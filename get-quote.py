import random


def primary():
    # print("Keep it logically awesome.")

    f = open("quotes.txt")
    quotes = f.readlines()
    f.close()

    chosenList = []

    for i in range(random.randint(1, len(quotes))):
        rnd = random.randint(0, len(quotes)-1)
        chosen = quotes[rnd]

        if chosen[-1:] == '\n':
            chosen = chosen[:-1]

        if chosenList.count(chosen) == 0:
            chosenList.append(chosen)

    for i in chosenList:
        print(i)


if __name__ == "__main__":
    primary()
