time = input("표준입력 >>> ")

# 분만 있을 때
if time.find('시간') == -1:
    result = time.split('분')
    print(result[0])
# 시간만 있을 때    
elif time.find('시간') == True and time.find('분') == -1:
    result = time.split('시간')
    print(int(result[0])*60)
# 시간과 분이 있을 때
else:
    result = time.split()
    result2 = result[0].split('시간')
    result3 = result[1].split('분')
    output = int(result2[0])*60 + int(result3[0])
    print(output)
