# 1. 필요한 라이브러리 불러오기
import requests
from datetime import datetime

# 2. 설정
API_KEY = "4015f0b004fb1563bc0a33aa38bb4b0c" # 사용자의 API 키
BASE_URL = "http://api.openweathermap.org/data/2.5/"

def get_current_weather(city_name):
    """지정된 도시의 현재 날씨 정보를 가져와 출력하는 함수"""
    url = f"{BASE_URL}weather?q={city_name}&appid={API_KEY}&units=metric&lang=kr"
    print(f"\n'{city_name}'의 현재 날씨 정보를 가져오는 중입니다...")
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        weather_desc = data["weather"][0]["description"]
        temp = data["main"]["temp"]
        feels_like = data["main"]["feels_like"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]
        
        print(f"✅ 날씨: {weather_desc}")
        print(f"✅ 온도: {temp}°C (체감온도: {feels_like}°C)")
        print(f"✅ 습도: {humidity}%")
        print(f"✅ 풍속: {wind_speed}m/s")
    else:
        print(f"❌ 오류가 발생했습니다. 도시 이름을 확인해주세요.")

def get_forecast(city_name):
    """지정된 도시의 5일치 예보를 가져와 출력하는 함수"""
    url = f"{BASE_URL}forecast?q={city_name}&appid={API_KEY}&units=metric&lang=kr"
    print(f"\n'{city_name}'의 5일 예보 정보를 가져오는 중입니다...")
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        print("--- 5일 예보 (매일 정오 기준) ---")
        for forecast in data['list']:
            # 'dt_txt'를 datetime 객체로 변환
            forecast_time = datetime.strptime(forecast['dt_txt'], '%Y-%m-%d %H:%M:%S')
            # 매일 정오(12시) 데이터만 선택하여 출력
            if forecast_time.hour == 12:
                date_str = forecast_time.strftime('%m월 %d일')
                weather_desc = forecast['weather'][0]['description']
                temp = forecast['main']['temp']
                print(f"🗓️  {date_str}: {weather_desc}, {temp}°C")
        print("---------------------------------")
    else:
        print(f"❌ 오류가 발생했습니다. 도시 이름을 확인해주세요.")


# 3. 챗봇 메인 루프
print("안녕하세요! 날씨를 알고 싶은 도시 이름을 입력해주세요.")
print("프로그램을 종료하려면 '종료'라고 입력하세요.")

while True:
    city_input = input("\n도시 이름: ")
    
    if city_input.lower() == '종료':
        print("날씨 챗봇을 종료합니다. 이용해주셔서 감사합니다!")
        break
    
    while True:
        choice = input("어떤 정보가 필요한가요? (1: 현재 날씨, 2: 5일 예보, c: 도시 변경): ")
        if choice == '1':
            get_current_weather(city_input)
            break
        elif choice == '2':
            get_forecast(city_input)
            break
        elif choice.lower() == 'c':
            break
        else:
            print("잘못된 선택입니다. 1, 2, c 중에서 입력해주세요.")
