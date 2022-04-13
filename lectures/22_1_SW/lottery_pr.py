import random
import pandas as pd
df_sheet_index = pd.read_excel('./출석부.xls')
print(df_sheet_index)

# random.seed(4478)

# teams = list(range(1,40))

# random.shuffle(teams)

# for ind, team in enumerate(teams):
#     if ind < 10:
#         print(f"월요일 {ind+1} 번째 팀 = {team} 조")
#     else: 
#         print(f"수요일 {ind-10} 번째 팀 = {team} 조")



