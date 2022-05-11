# 1. 파일 쓰기
file = open("./Chapter10/data.txt", "w", encoding="utf-8")
file.write("1. 타르타르 콩콩콩")
file.close()

# 2. 파일 추가
file = file = open("./Chapter10/data.txt", "a", encoding="utf-8")
file.write("\n2. 룰루랄라 랄랄라")
file.close()

# 3. 파일 읽기
file = open("./Chapter10/data.txt", "r", encoding="utf-8")

# 3.1 파일 전체 읽기
data = file.read()
print(data)
file.close()

# 3.2 파일 한 줄 읽기
while True:
    data = file.readline()
    print(data, end="")     # end="" : 줄바꿈제거
    if data == "":
        break
file.close()
