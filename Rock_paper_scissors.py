import random
def play_rock_paper_scissors():

  options = ["rock", "paper", "scissors"]
  computer_choice = random.choice(options)
  user_choice = input("Enter your choice (rock, paper, scissors): ").lower()
  while user_choice not in options:
    print("Invalid choice. Please enter rock, paper, or scissors.")
    user_choice = input("Enter your choice (rock, paper, scissors): ").lower()

  print(f"Computer chose: {computer_choice}")
  if user_choice == computer_choice:
    print("It's a tie!")
  elif user_choice == "rock":
    if computer_choice == "scissors":
      print("Rock smashes scissors! You win!")
    else:
      print("Paper covers rock! You lose.")
  elif user_choice == "paper":
    if computer_choice == "rock":
      print("Paper covers rock! You win!")
    else:
      print("Scissors cuts paper! You lose.")
  elif user_choice == "scissors":
    if computer_choice == "paper":
      print("Scissors cuts paper! You win!")
    else:
      print("Rock smashes scissors! You lose.")

if __name__ == "__main__":
  play_rock_paper_scissors()