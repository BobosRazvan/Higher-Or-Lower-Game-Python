from game_data import data
import art
import random
from replit import clear

playing = True
score = 0
while playing == True:
  print(art.logo)
  index1 = random.randint(0, len(data) - 1)
  name1 = data[index1]['name']
  description1 = data[index1]['description']
  country1 = data[index1]['country']
  index2 = random.randint(0, len(data) - 1)
  name2 = data[index2]['name']
  description2 = data[index2]['description']
  country2 = data[index2]['country']
  print(f"Compare A: {name1}, {description1}, from {country1}.")
  print(art.vs)
  print(f"Against B: {name2}, {description2}, from {country2}.")
  guess = input("Who has more followers? Type 'A' or 'B': ")
  if guess == 'A':
    if (data[index1]['follower_count'] >= data[index2]['follower_count']):
      score = score + 1
      print(f"You're right! Current score: {score}")
    else:
      print("You're wrong!. Game over!")
      print(f"Final scored: {score}")
      playing = False
  elif guess == 'B':
    if (data[index1]['follower_count'] <= data[index2]['follower_count']):
      score = score + 1
      print(f"You're right! Current score: {score}")
    else:
      print("You're wrong!. Game over!")
      print(f"Final score: {score}")
      playing = False
