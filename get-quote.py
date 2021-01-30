import random
def primary():
  # print("Keep it logically awesome.")

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  rnd = random.randint(0, len(quotes)-1)

  print(quotes[rnd])

if __name__== "__main__":
  primary()
