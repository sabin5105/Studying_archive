name = 'sabin'
duration =7

message = name + "님 수강기간이 " + str(duration) + "일 남았습니다"
print(message)

# 문자열 포매팅 사용
# f-string
message_format = f"{name}님 수강기간이 {duration}일 남았습니다"
print(message_format)

# format
message_format2 = "{}님 수강기간이 {}일 남았습니다".format(name, duration)
print(message_format2)