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
source venv/Scripts/activate # (Mac `venv\bin\activate`)   
pip install -r requirements.txt
```

### 환경 변수 설정
**.env** 파일을 프로젝트 루트에 생성하고 

