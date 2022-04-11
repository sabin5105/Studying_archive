import sqlite3

conn = sqlite3.connect('./myvenv/Chapter05/SQL_db.db')

# cursor = 데이터 전달 버스
cur = conn.cursor()

# SQL 명령작성
CREATE_SQL = """
    CREATE TABLE IF NOT EXISTS Items(
        id integer primary key autoincrement,
        code text not null,
        name text not null,
        price integer not null
    )
"""

# SQL 명령 실행
cur.execute(CREATE_SQL)

# 데이터베이스 닫기
conn.close()