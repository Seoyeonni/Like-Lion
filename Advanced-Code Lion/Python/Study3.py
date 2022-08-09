#날씨 정보 받아오기 주석 추가

# 파이썬의 f string 을 사용하기 위해선 문자열 앞에 f를 붙인다
# json = Javascript Object Notation

import requests
import json

city = "Seoul"
apikey = "d31460d33dd77c54cb626c3bc3fd532e" #나라는 사용자를 알리는 것. 깃허브에 올릴 때는 api 빼고 올리기.
temp = "metric"
api = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={apikey}&lang=kr&units={temp}" #f가 들어가 있으면 안에서 변수를 만들 수 있음. 파이썬 내장 객체?(import 모듈 없이)

# http://api.openweathermap.org/data/2.5/weather?q=Seoul&appid=d31460d33dd77c54cb626c3bc3fd532e&lang=kr&units=metric

result = requests.get(api)
print(result.text)

data = json.loads(result.text) #data를 json형식으로 road를 하겠다는 뜻.

# print(type(result.text))
# print(type(data))

print(data["name"],"의 날씨입니다.")
print("날씨는 ",data["weather"][0]["description"],"입니다.")
print("현재 온도는 ",data["main"]["temp"],"입니다.")
print("하지만 체감 온도는 ",data["main"]["feels_like"],"입니다.")
# 최저 기온 : main - temp_min
print("최저 기온은 ",data["main"]["temp_min"],"입니다.")
# 최고 기온 : main - temp_max
print("최고 기온은 ",data["main"]["temp_max"],"입니다.")
# 습도 : main - humidity
print("습도는 ",data["main"]["humidity"],"입니다.")
# 기압 : main - pressure
print("기압은 ",data["main"]["pressure"],"입니다.")
# 풍향 : wind - deg
print("풍향은 ",data["wind"]["deg"],"입니다.")
# 풍속 : wind - speed
print("풍속은 ",data["wind"]["speed"],"입니다.")