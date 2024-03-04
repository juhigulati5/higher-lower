from game_data import data
import random
from art import logo, vs
from replit import clear


def celeb_assignment():
  rand_num = random.randint(0,49)
  celeb = data[rand_num]
  return celeb

def compare_followers(a,b):
  if a["follower_count"] > b["follower_count"]:
    return "a"
  elif a["follower_count"] < b["follower_count"]:
    return "b"

celebA = celeb_assignment()
celebB = celeb_assignment()
score = 0

keep_going = True

print(logo)

while keep_going:

  print(f"Compare A: {celebA['name']}, {celebA['description']}, from {celebA['country']}.")

  print(vs)

  print(f"Against B: {celebB['name']}, {celebB['description']}, from {celebB['country']}.")

  more_followers = input("Who has more followers, A or B?: ").lower()
  if more_followers == compare_followers(celebA,celebB):
    clear()
    score +=1
    print(f"You're right! Current score: {score}")
    celebA = celebB
    celebB = celeb_assignment()
  else:
    clear()
    print(f"Sorry, that's wrong. Final score: {score}")
    keep_going = False


