pull_up = []

for i in range(1,8):
    pull_up.append(int(input("{}일차 턱걸이 횟수 >>> ".format(i))))
# input 함수는 1개의 parameter를 받음
# format 을 이용해 해결
    
average = (pull_up[0] + pull_up[1] + pull_up[2] + pull_up[3] + pull_up[4] + pull_up[5] + pull_up[6]) / 7
print(int(average))