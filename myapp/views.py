from django.shortcuts import render
 
def index_template(request):
    return render(request, 'index.html')
import requests
import re
from datetime import datetime
import requests
from bs4 import BeautifulSoup


city_code = "270000" # 大阪府（東大阪市）のcityコード270000
url = "https://weather.tsukumijima.net/api/forecast/city/" + city_code

try:
    response = requests.get(url)
    response.raise_for_status()     # ステータスコード200番台以外は例外とする
    print(response.status_code)
except requests.exceptions.RequestException as e:
    print("エラー : ",e)

else:
    weather_json = response.json()
    print(weather_json)
    print(weather_json['forecasts'][0]['image']['title']) # 0:今日 1:明日 2:明後日
    a = weather_json['forecasts'][1]['image']['title']
    print(a[0])
    b = a[0]
    print (b)
    if b in "雷":
        print("雷")
        kaminari = 'background-image: url(https://media.loom-app.com/gizmodo/dist/images/2017/12/05/171206_lightning.gif?w=640)'

    else:
        kaminari = 'background-color: #fcd184'
    if b == "晴":
        print(1)
    elif b == "曇":
        print(2)
    elif b == "雨":
        print(3)
    elif b == "雪":
        print(4)
    else:
        print("Error")
# 現在の時間の降水確率を取得していく
    now_hour = datetime.now().hour
    print(weather_json['forecasts'][0]['chanceOfRain'])
    b = weather_json['forecasts'][0]['chanceOfRain']['T00_06']
    c = weather_json['forecasts'][0]['chanceOfRain']['T06_12']
    d = weather_json['forecasts'][0]['chanceOfRain']['T12_18']
    e = weather_json['forecasts'][0]['chanceOfRain']['T18_24']
    if 0 <= now_hour and now_hour < 6:
        cor = weather_json['forecasts'][0]['chanceOfRain']['T00_06']
        print("0<6")
        if cor == "--%":
            print(weather_json['forecasts'][0]['chanceOfRain']['T06_12'])
    elif 6 <= now_hour and now_hour < 12:
        cor = weather_json['forecasts'][0]['chanceOfRain']['T06_12']
        print("6<12")
        if cor == "--%":
            print(weather_json['forecasts'][0]['chanceOfRain']['T12_18'])
    elif 12 <= now_hour and now_hour < 18:
        cor = weather_json['forecasts'][0]['chanceOfRain']['T12_18']
        print("12<18")
        if cor == "--%":
            print(weather_json['forecasts'][0]['chanceOfRain']['T18_24'])
    else:
        cor = weather_json['forecasts'][0]['chanceOfRain']['T18_24']
        if cor == "--%":
            print("a")

    print("現在の降水確率 {}".format(cor))
    kintetsu1Line_URL = "https://transit.yahoo.co.jp/diainfo/284/0"
    kintetsu1Line_Requests = requests.get(kintetsu1Line_URL)
    kintetsu1Line_Soup = BeautifulSoup(kintetsu1Line_Requests.text, 'html.parser')
    if kintetsu1Line_Soup.find('dd',class_='trouble'):
        kintetsu1 = 0
    else:
        kintetsu1 = 1

    kintetsu2Line_URL = "https://transit.yahoo.co.jp/diainfo/285/0"
    kintetsu2Line_Requests = requests.get(kintetsu2Line_URL)
    kintetsu2Line_Soup = BeautifulSoup(kintetsu2Line_Requests.text, 'html.parser')
    if kintetsu2Line_Soup.find('dd',class_='trouble'):
        kintetsu2 = 0
    else:
        kintetsu2 = 1
    if not kintetsu1 + kintetsu2 == 2:
        print("近鉄遅れ")
        kintetsu = "遅れ"
        kintetsucss = "color: red;"
    else:
        print("近鉄平常")
        kintetsu = "平常"
        kintetsucss = "color: black"
    
    keihanLine_URL = "https://transit.yahoo.co.jp/diainfo/300/0"
    keihanLine_Requests = requests.get(keihanLine_URL)
    keihanLine_Soup = BeautifulSoup(keihanLine_Requests.text, 'html.parser')
    if keihanLine_Soup.find('dd',class_='trouble'):
        keihan = print("京阪遅れ")
        keihan = "遅れ"
        keihancss = "color: red;"
    else:
        keihan = print("京阪平常")
        keihan = "平常"
        keihancss = "color: black"
    jrLine_URL = "https://transit.yahoo.co.jp/diainfo/263/0"
    jrLine_Requests = requests.get(jrLine_URL)
    jrLine_Soup = BeautifulSoup(jrLine_Requests.text, 'html.parser')
    if jrLine_Soup.find('dd',class_='trouble'):
        print("jr遅れ")
        jr = "遅れ"
        jrcss = "color: red;"
    else:
        print("jr平常")
        jr = "平常"
        jrcss = "color: black"
        # https://qiita.com/hirohiroto522/items/6ff29be1344be805ecb0
image = weather_json['forecasts'][0]['image']['url']
print(image)
print(kaminari)
from django.shortcuts import render
from django.http.response import HttpResponse
 
def index_template(request):
    
    myapp_data = {
    'app': 'Django',
    'wether': a,
    'a':b,
    'b':c,
    'c':d,
    'd':e,
    'kintetsu':kintetsu,
    'jr':jr,
    'keihan':keihan,
    'image':image,
    'kaminari':kaminari,
    'kintetsucss':kintetsucss,
    'jrcss':jrcss,
    'keihancss':keihancss

    }
    return render(request, 'index.html', myapp_data)
