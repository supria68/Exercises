"""
Rock beats paper, paper beats scissors and Scissors beats rock!

"""
import random

def playGame():
    user_score = 0
    pc_score = 0

    ran = ["rock", "paper", "scissors"]

    for i in range(3):
    
        pc_guess = random.choice(ran)
        guess = input("ROCK or PAPER or SCISSORS?  ").lower()
        print("\nYou played, " + guess + " and your computer played, " + pc_guess)
   
        if pc_guess == guess:
            print("IT IS A TIE!")
        else:
            if (guess == 'rock' and pc_guess == 'scissors') or (guess == 'paper' and pc_guess == 'rock') or (guess == 'scissors' and pc_guess == 'paper') :
                print("You WON :)")
                user_score += 1
            elif (guess == 'rock' and pc_guess == 'paper') or (guess == 'paper' and pc_guess == 'scissors') or (guess == 'scissors' and pc_guess == 'rock'):
                print("You lost :(")
                pc_score += 1
        i += 1 

    print("\nYour score = " + str(user_score))
    print("\nComputer score = " + str(pc_score))
    if pc_score > user_score:
        print("\nComputer Wins :( ")
    elif pc_score == user_score:
        print("\nIts a TIE! ")
    elif pc_score < user_score:
        print("\nYou WON :)")


if __name__ == "__main__":
    
    print("YOU ARE NOW PLAYING ROCK PAPER SCISSORS against your computer! This is a best of three game!\n")
    flag, count  = 1, 1 # count indicates rounds 
    
    while flag:
        playGame()
        flag = int(input('Want to play again? Press 1 for Yes , 0 for No : '))
        if flag == 1:
            count += 1
            print('Round ' + str(count))
