import random

symbols = ['🍒', '🍇', '🍉', '7️⃣']
results = random.choices(symbols, k=3)
print(results[0] + "|" + results[1] + "|" + results[2])
sevens = False
for i in range(0, len(results)-1):
  if results[i] == '7️⃣' and results[i+1] == '7️⃣':
    sevens = True and sevens
  else:
    sevens = False

if sevens == True:
  print("Jackpot!")
else:
  print("Thanks for playing!")
