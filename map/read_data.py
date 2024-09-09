import pymysql

# MySQL 연결 설정
conn = pymysql.connect(
    host='localhost',
    user='root',
    password='root',  # MySQL 비밀번호
    db='navi',   # 데이터베이스 이름
    charset='utf8'
)

# 커서 생성
cur = conn.cursor()

# 데이터베이스에서 좌표 데이터 가져오기
cur.execute("SELECT longitude, latitude FROM elevater_location")
coords = cur.fetchall()

# 연결 종료
cur.close()
conn.close()
