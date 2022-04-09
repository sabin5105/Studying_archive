# 딕셔너리
# : 사전형태의 자료형

# 딕셔너리 생성
stock_a = {"삼성전자" : 82000, "LG전자" : 150000}

stock_b = {
    "삼성전자" : [81000, 81500, 82000, 81500, 82000],
    "LG전자" : (150000, 151000, 149000, 1520000)
}

stock_c = {
    "삼성전자" : {
        "현재가" : 82000,
        "보유수량" : 5,
        "매수단가" : 81000
    }
}

print(stock_a)
print(stock_b)
print(stock_c)

# 딕셔너리 접근
print(stock_a["삼성전자"])
print(stock_c["삼성전자"]["보유수량"])

# 딕셔너리 할당
stock_a["삼성전자"] = 85000
print(stock_a)

# 딕셔너리 삭제
del stock_a["LG전자"]
print(stock_a)

# 딕셔너리 함수
stock_d = {
    "삼성전자" : 82000,
    "SK하이닉스" : 123000,
    "네이버" : 370000,
    "카카오" : 133000
}
# items() : key & data 반환
for item in stock_d.items():
    print(item)

# keys() : key 반환
for key in stock_d.keys():
    print(key)

# values() : value 반환
for value in stock_d.values():
    print(value)
    