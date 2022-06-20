
if __name__=='__main__':
    import random
    import pandas as pd
    
    df_sheet_index = pd.read_excel('./lectures/22_1_SW/출석부.xls')
    gwa = df_sheet_index["학과"].to_list()
    name = df_sheet_index["성명"].to_list()
    N = len(gwa)

    seed_ = 2204251101
    random.seed(seed_)
    teams = list(range(0,N))  

    random.shuffle(teams)
    
    gwa_ = [gwa[i] for i in teams]
    name_ = [name[i] for i in teams]
    
    for ind, (g,n) in enumerate(zip(gwa_,name_)):
        if ind < N/2:
            print(f"4월 27일 수요일 발표 {ind+1} 번째 = {g} {n[:-1]}* ")
        else: 
            print(f"5월 2일 발표 {ind-(N//2)} 번째 ={g} {n[:-1]}*")
    
# teams = list(range(1,40))

# random.shuffle(teams)

# for ind, team in enumerate(teams):
#     if ind < 10:
#         print(f"월요일 {ind+1} 번째 팀 = {team} 조")
#     else: 
#         print(f"수요일 {ind-10} 번째 팀 = {team} 조")



