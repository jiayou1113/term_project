import http.server
import socketserver

# 서버 포트 설정 (기본 8000)
PORT = 8000

#  HTML 페이지 내용
html_content = """
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <title>2025 Term Project - Python Web Server</title>
    <style>
        body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; text-align: center; background-color: #f0f2f5; padding-top: 50px; }
        .card { background: white; padding: 40px; border-radius: 15px; box-shadow: 0 4px 15px rgba(0,0,0,0.1); display: inline-block; }
        h1 { color: #1a73e8; }
        p { color: #5f6368; line-height: 1.6; }
        .status { color: #34a853; font-weight: bold; }
    </style>
</head>
<body>
    <div class="card">
        <h1>🐍 Python Term Project</h1>
        <p>이 웹페이지는 외부 라이브러리 없이<br><b>Pure Python Standard Library</b>만으로 구축된 서버에서 구동 중입니다.</p>
        <hr>
        <p>제출자: [본인 이름]</p>
        <p class="status">● Server Status: Online</p>
    </div>
</body>
</html>
"""

# HTML 파일 생성
with open("index.html", "w", encoding="utf-8") as f:
    f.write(html_content)

# 서버 실행 로직
Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"✅ 서버가 성공적으로 시작되었습니다!")
    print(f"🌐 브라우저에서 http://localhost:{PORT} 를 입력하여 확인하세요.")
    print("종료하려면 Ctrl+C를 누르세요.")

    httpd.serve_forever()
