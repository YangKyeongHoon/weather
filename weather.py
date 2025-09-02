# 1. 필요한 라이브러리 불러오기
import requests
import json

# 2. 설정
# TODO: OpenWeatherMap에서 발급받은 API 키를 입력하세요.
API_KEY = "4015f0b004fb1563bc0a33aa38bb4b0c"
CITY_NAME = "Seoul"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

# 3. API 요청 URL 만들기
url = f"{BASE_URL}?q={CITY_NAME}&appid={API_KEY}&units=metric&lang=kr"

# 4. 날씨 정보 요청 및 받아오기
print("날씨 정보를 가져오는 중입니다...")
response = requests.get(url)
data = response.json()

# 5. 응답 데이터 확인 및 결과 출력
if response.status_code == 200:
    # 성공적으로 데이터를 받아온 경우
    # 전체 데이터 구조를 보려면 아래 줄의 주석을 해제하세요.
    # print(json.dumps(data, indent=4, ensure_ascii=False))
    
    # 필요한 정보 추출
    city_name = data["name"]
    weather_desc = data["weather"][0]["description"]
    temp = data["main"]["temp"]
    
    # 결과 출력
    print(f"도시: {city_name}")
    print(f"날씨: {weather_desc}")
    print(f"온도: {temp}°C")
else:
    # 에러가 발생한 경우
    print(f"오류가 발생했습니다: {data.get('message', '알 수 없는 오류')}")
