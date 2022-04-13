
if __name__=='__main__':
    import random
    import pandas as pd
    
    df_sheet_index = pd.read_excel('./lectures/22_1_SW/출석부.xls')
    gwa = df_sheet_index["학과"].to_list()
    name = df_sheet_index["성명"].to_list()
    N = len(gwa)

    seed_ = 4478
    random.seed(seed_)
    teams = list(range(1,N+1))  

    random.shuffle(teams)

    for ind, (g,n) in enumerate(zip(gwa,name)):
        if ind < N/2:
            print(f"오늘 발표 {ind+1} 번째 = {g} {n[:-1]}* ")
        else: 
            print(f"다음 발표 {ind-(N//2)} 번째 ={g} {n[:-1]}*")
    
# teams = list(range(1,40))

# random.shuffle(teams)

# for ind, team in enumerate(teams):
#     if ind < 10:
#         print(f"월요일 {ind+1} 번째 팀 = {team} 조")
#     else: 
#         print(f"수요일 {ind-10} 번째 팀 = {team} 조")



