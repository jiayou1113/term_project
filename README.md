# 🐍 Term Project: Python Standard Library Web Server

본 프로젝트는 외부 라이브러리 설치 없이 **Python 표준 라이브러리(Standard Library)**만을 활용하여 구축한 경량 웹 서버 프로젝트입니다. 

## 1. 프로젝트 개요
- **핵심 기술:** `http.server`, `socketserver`
- **목표:** 외부 종속성 없이 실행 가능한 서버 로직 구현 및 웹 페이지 서빙

## 2. 주요 특징
- **No Dependencies:** `pip install` 과정이 전혀 필요 없는 순수 파이썬 코드입니다.
- **Auto-Generation:** 실행 시 자동으로 `index.html` 파일을 생성하고 서버를 호스팅합니다.
- **Standard Protocol:** HTTP 프로토콜을 준수하여 브라우저(Chrome, Edge 등)를 통해 결과를 확인할 수 있습니다.

## 3. 실행 방법 (How to Run)

1. 저장소를 클론하거나 `main.py` 파일을 다운로드합니다.
2. 터미널(또는 CMD)에서 아래 명령어를 입력합니다.
   ```bash
   python main.py
