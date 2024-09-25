import os
import pymysql
import getpass

# 비밀번호 입력받기
db_password = getpass.getpass('Enter your database password: ')

# MySQL 연결 설정
conn = pymysql.connect(
    host=os.getenv('DB_HOST', 'localhost'),  # 환경 변수로부터 DB_HOST를 가져옴
    user=os.getenv('DB_USER', 'root'),       # 환경 변수로부터 DB_USER를 가져옴
    password=db_password,                    # 입력받은 비밀번호 사용
    db=os.getenv('DB_NAME', 'navi'),         # 환경 변수로부터 DB_NAME을 가져옴
    port=int(os.getenv('DB_PORT', 3306)),    # 환경 변수로부터 DB_PORT를 가져옴
    charset='utf8'                           # 문자셋 설정
)

# 커서 생성
cur = conn.cursor()

# 데이터베이스에서 좌표 데이터 가져오기
cur.execute("SELECT longitude, latitude FROM elevater_location")
cur.execute("SELECT esc_longitude, esc_latitude FROM escalator_location")
coords = cur.fetchall()

# 좌표 데이터 출력 (테스트용)

# 연결 종료
cur.close()
conn.close()
