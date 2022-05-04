print("Let's Learning korean")

koreans = ['사랑해','귀엽다', '고마워', '행복해']

correct = 0
wrong = 0

for korean in koreans:
    print(korean)
    word = input()
    if word == korean:
        correct += 1
    elif word != korean:
        wrong += 1

print("맞은 문제 개수: ", correct)
print("틀린 문제 개수: ", wrong)