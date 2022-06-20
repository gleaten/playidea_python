import random

seed_ = 5394
random.seed(seed_)

teams = list(range(1,15))

random.shuffle(teams)

for ind, team in enumerate(teams):
    if ind < 10:
        print(f"월요일 {ind+1} 번째 팀 = {team} 조")
    else: 
        print(f"수요일 {ind-9} 번째 팀 = {team} 조")
    