import requests
import json

city = "Seoul"
apikey = "8a16eba8e5a6258fd5159056c8667f94"
lang = "kr"

api = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={apikey}&lang={lang}&units=metric"
# units=metric -> 온도 단위: C
# units=imperial -> 온도 단위: K

result = requests.get(api) # requests.get() -> 서버에 요청 보내기
# print(result.text)

data = json.loads(result.text)

# print(type(result.text))
# print(type(data))

print(data["name"],"의 날씨입니다.")
print("날씨는 ",data["weather"][0]["description"],"입니다.")
print("현재 온도는 ",data["main"]["temp"],"입니다.")
print("체감 ",data["main"]["feels_like"],"일 거에요.")
print("최저 기온은 ",data["main"]["temp_min"],"입니다.")
print("최고 기온은 ",data["main"]["temp_max"],"입니다.")
print("습도는 ",data["main"]["humidity"],"입니다.")
print("기압은 ",data["main"]["pressure"],"입니다.")
print("풍향은 ", data["wind"]["deg"],"입니다.")
print("풍속은 ", data["wind"]["speed"],"입니다.")