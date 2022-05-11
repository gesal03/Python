import requests
import json

city = "Seoul"
apikey = "f364fe04309916af0a2d56f4d0908ab2"
lang = "kr"
api = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={apikey}&lang={lang}&units=metric" #f-string

result = requests.get(api)



data = json.loads(result.text)
print(data)
print(data["name"], "의 날씨입니다.")
print("날씨는 ", data["weather"][0]["description"], "입니다.") # 왜 이것만 다른지 공부
print("온도는 ", data["main"]["temp"], "입니다.")
print("체감온도는 ", data["main"]["feels_like"], "입니다.")
print("최저 기온은 ", data["main"]["temp_min"], "입니다.")
print("최고 기온은 ", data["main"]["temp_max"], "입니다.")
print("습도는 ", data["main"]["humidity"], "입니다.")
print("기압은 ", data["main"]["pressure"], "입니다.")
print("풍향은 ", data["wind"]["deg"], "입니다.")
print("풍속은 ", data["wind"]["speed"], "입니다.")