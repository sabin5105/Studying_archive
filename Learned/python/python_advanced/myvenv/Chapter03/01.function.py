# 1. 위치 매개변수
# 가장 기본적인 매개변수

def my_func(a,b):
    print(a,b)

my_func(1,2)

# 2. 기본 매개변수
# 매개변수의 기본값을 지정할 수 있다

def post_info(title, content='내용없음'):
    print("제목 : ", title)
    print("내용 : ", content)

post_info("출석합니다")

# 3. 키워드 매개변수
# 함수 호출 시 키워드를 붙여서 호출
# 매개변수의 순서를 지키지 않아도 됨

def post_info(title, content):
    print("제목 : ", title)
    print("내용 : ", content)

post_info(content="content", title="title")
