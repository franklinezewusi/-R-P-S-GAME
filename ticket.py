
person1 = input("rock/paper/scissors:> ").lower()
person2 = input("rock/paper/scissors:> ").lower()
check1 = person1.strip()
print(check1)
check2 = person2.strip()
print(check2)
if person1 == 'rock' and person2 == 'scissors':
    print(person1, "person1 wins")
elif person1 == 'rock' and person2 == 'paper':
    print("person2 wins")
elif person1 == 'scissors' and person2 == 'rock':
    print("person2 wins")
elif person1 == 'scissors' and person2 == 'paper':
    print("person1 wins")
elif person1 == 'paper' and person2 == 'rock':
    print("person2 wins")
elif person1 == 'paper' and person2 == 'scissors':
    print("person2 wins")
elif person1 == person2:
    print("TIE")
elif person1 != ("rock", "paper", "scissors") or person2 != ("rock", "paper", "scissors"):
    print("invalid choice")
else:
    print("End of the Game")