import random
def primary():
  # print("Keep it logically awesome.")

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  rnd = random.randint(0, len(quotes)-1)
  chosen = quotes[rnd]
  
  if chosen[-1:] == '\n':
    chosen = chosen[:-1]

  print(chosen)

if __name__== "__main__":
  primary()
