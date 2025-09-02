# 1. 필요한 라이브러리 불러오기
import requests
import json

# 2. 설정
# TODO: OpenWeatherMap에서 발급받은 API 키를 입력하세요.
API_KEY = "YOUR_API_KEY"
CITY_NAME = "Seoul"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

# 3. API 요청 URL 만들기
url = f"{BASE_URL}?q={CITY_NAME}&appid={API_KEY}&units=metric&lang=kr"

# 4. 날씨 정보 요청 및 받아오기
print("날씨 정보를 가져오는 중입니다...")
# response = requests.get(url)
# data = response.json()

# 5. 결과 출력
# print(json.dumps(data, indent=4, ensure_ascii=False))

print("날씨 앱 준비 완료!")
