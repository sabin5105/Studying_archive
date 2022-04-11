# 1. 위치 가변 매개변수 / tuple형식
def print_fruits(*args):
    for arg in args:
        print(arg)

print_fruits('apple','orange','mango')

# 2. 키워드 가변 매개변수 / dictionaruy형식
def comment_info(**kwargs):
    for key, value in kwargs.items():
        print(key, value)

comment_info(name="파린이", content="죄송합니다ㅜㅜ")

# 매개변수 작성 순서
# 위치 - 기본 - 위치 가변 - 키워드(기본) - 키워드 가변

def post_info(title, content, *tags, **kwargs):
    print(f"제목 : {title}")
    print(f"내용 : {content}")
    print(f"태그 : {tags}")

post_info('#파이썬','#함수',title='파이썬 함수 정리', content='다양한 매개변수를 정리합니다')