# 교통약자를 위한 길안내 웹 서비스 - GuardianPath 🚶‍♂️🛡️

## 배포 주소
> **https://guardianpath.duckdns.org** (2024/10 ~ 2025/02)

--- 

## 👥 팀원 소개

| 이름 | Github |
| --- | --- |
| 서민승 | https://github.com/gnuesnim |
| 김상준 | https://github.com/Saangjun00 |
| 최성민 | https://github.com/songmean00 |
| 박다빈 | https://github.com/suwontaran |

---

## 🚀 프로젝트 개요

- **문제점**
  - 이동에 제약이 있는 개인들은 적절한 교통수단이나 경로를 찾는 데 어려움을 겪음

- **목적**
  - 교통 취약계층이 보다 쉽게 교통 서비스를 이용할 수 있도록 **사용자 친화적인 경로 탐색 플랫폼** 구축하기 위함

---

## 개발 환경

| 분류 | 활용 기술 및 프레임워크 |
| ----- | ----- |
| **Programing** | Python, JavaScript |
| **Frontend** | HTML, CSS, JavaScript |
| **Backend** | Django |
| **Cloud Service** | AWS EC2, AWS RDS(MariaDB) |
| **Database** | MariaDB |
| **API & SDK** | Tmap API, Kakao API, Google API |
| **Web Server** | uWSGI, Nginx |
| **Authentication** | Kakao OAuth, Google OAuth |
| **Deployment & DevOps** | Ubuntu, Let's Encrypt (SSL) |
| **Collaboration** | GitHub, Discord |

---

## 🛠️ How to Use

### 프로젝트 클론
```bash
git clone https://github.com/Saangun00/guardianPath.git
cd guardianPath
```

### 가상 환경 설정 및 패키지 설치
```bash
python -m venv venv
source venv/Scripts/activate # (Mac인 경우 venv\bin\activate)   
pip install -r requirements.txt
```

### 환경 변수 설정
```.env``` 파일을 프로젝트 루트에 생성하고, 실제 값으로 변경하여 환경 변수를 추가합니다.
```env
# Django Secret Key
SECRET_KEY=your_django_secret_key

# Database 설정
DB_NAME=your_db_name
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=your_db_host
DB_PORT=your_db_port

# API Keys
KAKAO_CLIENT_ID=your_kakao_client_id
GOOGLE_CLIENT_ID=your_google_client_id
TMAP_API_KEY=your_tmap_api_key
```

### 마이그레이션 및 서버 실행
```bash
python manage.py migrate
python manage.py runserver
```

---

## 화면 구성 📺
| 메인 페이지 | 즐겨찾기 및 검색기록 |
| :----------------------: | :---------------------: |
| ![image](https://github.com/user-attachments/assets/da34c45d-2d92-41e0-b5f6-f6a3adc5106d) | ![image](https://github.com/user-attachments/assets/5ac7f781-ca19-4c86-b635-abfb761eef49) |
| **경로 결과 페이지(상세정보 포함)** |  **경로 결과 페이지(엘리베이터 사용자)**|
| ![image](https://github.com/user-attachments/assets/de3eb478-7ea6-4f02-a7a3-bcc5bb09f2de) | ![image](https://github.com/user-attachments/assets/6806b7fe-9a67-472f-969a-77527df6d8f1) |

---

## 주요 기능

### ⭐️ 사용자 유형에 따른 경로 탐색 기능
  - 휠체어 사용자, 유모차 사용자 등 교통 약자를 위해 에스컬레이터와 엘리베이터 위치를 마커로 시각화하여, 이동 시 편의성을 제공함

### ⭐️ 교통수단 별 경로 색상 구분 기능
  - 버스, 지하철, 도보 등 교통수단에 따라 경로를 서로 다른 색상으로 구분하여 표시함

### ⭐️ 경로 즐겨찾기 및 검색 기록
- 사용자가 자주 이용하는 경로를 저장하여 간편하게 경로 검색 가능
- 최근 10개의 경로 검색 기록 지원

---

## 아키텍처

### 시스템 아키텍처
![GuardianPath System Architecture](https://github.com/user-attachments/assets/5650c348-bc6c-4c7a-ada9-727147170ef8)

### 데이터베이스 설계도(ERD)
![image](https://github.com/user-attachments/assets/cdc7ca12-5edd-49fd-abc4-290f55365567)

### 디렉토리 구조
```bash
GuardianPath
 ┣ .config
 ┃ ┣ nginx
 ┃ ┃ ┗ GuardianPath.conf
 ┃ ┗ uwsgi
 ┃ ┃ ┣ GuardianPath.ini
 ┃ ┃ ┗ uwsgi.service
 ┣ GuardianPath
 ┃ ┣ static
 ┃ ┣ asgi.py
 ┃ ┣ middleware.py
 ┃ ┣ settings.py
 ┃ ┣ urls.py
 ┃ ┣ wsgi.py
 ┃ ┗ __init__.py
 ┣ home
 ┃ ┣ migrations
 ┃ ┃ ┣ __pycache__
 ┃ ┃ ┗ __init__.py
 ┃ ┣ static
 ┃ ┃ ┣ css
 ┃ ┃ ┃ ┗ style.css
 ┃ ┃ ┣ img
 ┃ ┃ ┃ ┣ elevator-icon.png
 ┃ ┃ ┃ ┣ escalator-icon.png
 ┃ ┃ ┃ ┣ general-icon.png
 ┃ ┃ ┃ ┣ gps-icon.png
 ┃ ┃ ┃ ┗ profile-icon.png
 ┃ ┃ ┗ js
 ┃ ┃ ┃ ┗ home.js
 ┃ ┣ templates
 ┃ ┃ ┗ home.html
 ┃ ┣ admin.py
 ┃ ┣ apps.py
 ┃ ┣ models.py
 ┃ ┣ tests.py
 ┃ ┣ urls.py
 ┃ ┣ views.py
 ┃ ┗ __init__.py
 ┣ map
 ┃ ┣ migrations
 ┃ ┃ ┣ 0001_initial.py
 ┃ ┃ ┣ 0002_searchhistory.py
 ┃ ┃ ┣ 0003_elevatorlocation_escalatorlocation.py
 ┃ ┃ ┗ __init__.py
 ┃ ┣ static
 ┃ ┃ ┣ css
 ┃ ┃ ┣ img
 ┃ ┃ ┃ ┣ departure-marker.png
 ┃ ┃ ┃ ┣ destination-marker.png
 ┃ ┃ ┃ ┣ ele_img.png
 ┃ ┃ ┃ ┗ esc_img.png
 ┃ ┃ ┗ js
 ┃ ┃ ┃ ┗ map.js
 ┃ ┣ templates
 ┃ ┃ ┗ search_results.html
 ┃ ┣ admin.py
 ┃ ┣ apps.py
 ┃ ┣ models.py
 ┃ ┣ tests.py
 ┃ ┣ urls.py
 ┃ ┣ views.py
 ┃ ┗ __init__.py
 ┣ staticfiles
 ┃ ┣ css
 ┃ ┣ img
 ┃ ┗ js
 ┣ users
 ┃ ┣ migrations
 ┃ ┃ ┣ 0001_initial.py
 ┃ ┃ ┗ __init__.py
 ┃ ┣ static
 ┃ ┃ ┣ css
 ┃ ┃ ┃ ┗ login_style.css
 ┃ ┃ ┣ img
 ┃ ┃ ┃ ┣ kakao_login_medium_narrow.png
 ┃ ┃ ┃ ┗ web_light_sq_SI@1x.png
 ┃ ┃ ┗ js
 ┃ ┃ ┃ ┗ main.js
 ┃ ┣ templates
 ┃ ┃ ┣ registration
 ┃ ┃ ┃ ┣ password_change.html
 ┃ ┃ ┃ ┣ password_change_success.html
 ┃ ┃ ┃ ┣ password_reset_confirm.html
 ┃ ┃ ┃ ┣ password_reset_done.html
 ┃ ┃ ┃ ┣ password_reset_email.html
 ┃ ┃ ┃ ┣ password_reset_form.html
 ┃ ┃ ┃ ┗ password_reset_subject.txt
 ┃ ┃ ┣ login.html
 ┃ ┃ ┗ profile.html
 ┃ ┣ adapters.py
 ┃ ┣ admin.py
 ┃ ┣ apps.py
 ┃ ┣ models.py
 ┃ ┣ tests.py
 ┃ ┣ urls.py
 ┃ ┣ views.py
 ┃ ┗ __init__.py
 ┣ .env
 ┣ .gitignore
 ┣ manage.py
 ┗ requirements.txt
```


