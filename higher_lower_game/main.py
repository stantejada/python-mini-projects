from random import choice
import os


database = {
    "instagram": 694,
    "Cristiano Ronaldo": 664,
    "Lionel Messi": 506,
    "Selena Gomez": 417,
    "Kylie Jenner": 392,
    "Dwayne Johnson": 392,
    "Ariana Grande": 374,
    "Kim Kardashian": 355,
    "Miley Cyrus": 212,
    "Katy Perry": 202
}


def choice_random_pair():
    person_one = choice(list(database.keys()))
    person_two = choice(list(database.keys()))

    while person_one == person_two:
        choice(person_two)

    return person_one, person_two

def score(point, last_score):
    new_score = last_score + point
    last_score = new_score

    return new_score, last_score


print("""

#    $$\   $$\ $$\           $$\                                 
#    $$ |  $$ |\__|          $$ |                                
#    $$ |  $$ |$$\  $$$$$$\  $$$$$$$\   $$$$$$\   $$$$$$\        
#    $$$$$$$$ |$$ |$$  __$$\ $$  __$$\ $$  __$$\ $$  __$$\       
#    $$  __$$ |$$ |$$ /  $$ |$$ |  $$ |$$$$$$$$ |$$ |  \__|      
#    $$ |  $$ |$$ |$$ |  $$ |$$ |  $$ |$$   ____|$$ |            
#    $$ |  $$ |$$ |\$$$$$$$ |$$ |  $$ |\$$$$$$$\ $$ |            
#    \__|  \__|\__| \____$$ |\__|  \__| \_______|\__|            
#                  $$\   $$ |                                    
#                  \$$$$$$  |                                    
#                   \______/                                     
#    $$\                                                         
#    $$ |                                                        
#    $$ |      $$$$$$\  $$\  $$\  $$\  $$$$$$\   $$$$$$\         
#    $$ |     $$  __$$\ $$ | $$ | $$ |$$  __$$\ $$  __$$\        
#    $$ |     $$ /  $$ |$$ | $$ | $$ |$$$$$$$$ |$$ |  \__|       
#    $$ |     $$ |  $$ |$$ | $$ | $$ |$$   ____|$$ |             
#    $$$$$$$$\\$$$$$$  |\$$$$$\$$$$  |\$$$$$$$\ $$ |             
#    \________|\______/  \_____\____/  \_______|\__|             
#                                                                
#                                                                
#                                                                

""")

last_score = score(0,0)[1]
print("Rules: Choice from option 1 or 2 who famous has more follower on instagram.")



game_over = False

while not game_over:
    print(f"Score: {last_score}")
    famous = choice_random_pair()

    if database[famous[0]] > database[famous[1]]:
        higher = famous[0]
    else:
        higher = famous[1]

    answer = input(f"1. {famous[0]}\n2. {famous[1]}\nAnswer: ")

    if answer == '1' and famous[0] == higher:
        last_score = score(1, last_score)[1]
    elif answer == '2' and famous[1] == higher:
        last_score = score(1, last_score)[1]
    else:
        game_over = True

    os.system("cls")


print(f"Total Score: {last_score}")



