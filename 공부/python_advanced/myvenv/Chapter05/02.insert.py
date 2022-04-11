import sqlite3

conn = sqlite3.connect('./myvenv/Chapter05/SQL_db.db')

# cursor = 데이터 전달 버스
cur = conn.cursor()

# SQL 명령작성
INSERT_SQL = "INSERT INTO Item(code,name,price) VALUES(?,?,?);"
#UPDATE_SQL 응용가능
#DELETE_SQL 응용가능


# 데이터 여러개 한번에 추가하기
# data = (
#     ('A00001','게이밍 마우스',30000),
#     ('A00001','게이밍 마우스',30000),
#     ('A00001','게이밍 마우스',30000)
# )

# SQL 명령 실행
cur.execute(INSERT_SQL, ('A00001','게이밍 마우스',30000))
# cur.executemany(INSERT_SQL, data)

# 커밋 : INSERT ,UPDATE, DELETE는 commit을 해야 실제 DB에 반영된다
conn.commit()

# 데이터 조회
# rows = cur.fetchall()
# for row in rows:
#     print(row)

# 데이터베이스 닫기
conn.close()