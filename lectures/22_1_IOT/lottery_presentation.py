import random


random.seed(4478)

teams = list(range(1,15))

random.shuffle(teams)

for ind, team in enumerate(teams):
    if ind < 10:
        print(f"월요일 {ind+1} 번째 팀 = {team} 조")
    else: 
        print(f"수요일 {ind-10} 번째 팀 = {team} 조")
    