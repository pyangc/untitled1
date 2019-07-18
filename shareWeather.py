＃编码 = UTF8
导入请求
来自请求导入异常
来自
urllib.request
import urlopen

来自
bs4
进口
BeautifulSoup
来自
urllib.parse
导入
urlencode
来自线程导入计时器
进口重新
来自
wxpy
import *
# 进口
计划
进口
时间
导入
http
导入
json
导入日期时间
随机导入

bot = Bot（cache_path = True，console_qr = 1）
我 = bot.self
bot.enable_puid（' wxpy_puid.pkl '）

def api（


    url）：
header = {
    '接受'： ' text / html，application / xhtml + xml，application / xml; q = 0.9，image / webp，* / *; q = 0.8 '，
' Accept-Encoding '： ' gzip，deflate '，
'接受 - 语言'： ' zh-CN，zh; q = 0.8 '，
'连接'： '保持活力'，
' User-Agent '： ' Mozilla / 5.0（Windows NT 6.3; WOW64）AppleWebKit / 537.36（KHTML，像Gecko）Chrome / 43.0.235 '
}
超时 = random.choice（范围（80，180））
data = requests.get（url，headers = header，timeout = timeout）

return data.json（）

def sendweather（


    city，xx）：
URL = ' https://free-api.heweather.com/s6/weather/forecast?location= ' + 城市 + '＆键=和风键'
PMurl = ' https://free-api.heweather.com/s6/air/now?parameters&location= ' + 城市 + '＆键=和风键'
lifeurl = ' https://free-api.heweather.com/s6/weather/lifestyle?location= ' + 城市 + '＆键=和风键'

temp = api（url）
temp = temp[' HeWeather6 '][0]
update = temp[' update ']
now = temp[' daily_forecast '][0]
nowTime = datetime.datetime.now（）。strftime（'％Y-％m- ％d％H：％M：％S '）

pm = api（PMurl）
pm = pm[' HeWeather6 '][0]
airnow = pm[' air_now_city ']

life = api（lifeurl）

生命 = 生命[' HeWeather6 '][0]
生活 = 生活['生活方式']
result = xx + city + ' --- ' + ' \ n ' + ' \ n ' \
         + '           今天天气：' + 现在[' cond_txt_d '] + '转' + 现在[' cond_txt_n '] + ' \ n ' \
         + '           ：今天温度' + 现在[' tmp_min '] + ' °C〜' + 现在[' TMP_MAX '] + ' ℃的' + ' \ n ' \
         + '           风向：' + 现在[' wind_dir '] + '  ' + 现在[' wind_sc '] + '级' + 现在[' wind_spd '] + '公里/小时' + ' \ n ' \
         + '           相对湿度：' + now[' hum '] + '％' + ' \ n ' \
         + '           降水量：' + 现在[' pcpn '] + ' ml ' + '，降水概率：' + now[' pop '] + '％' + ' \ n ' \
         + '           能见度：' + 现在[' vis '] + '公里' + ' \ n ' \
         + ' ------------------------------------------ ' + ' \ n ' \
         + '今天空气质量：' + ' \ n ' \
         + '           空气质量指数：' + airnow[' aqi '] + ' \ n ' \
         + '           主要污染物：' + airnow[' main '] + ' \ n ' \
         + '           空气质量：' + airnow[' qlty '] + ' \ n ' \
         + '           二氧化氮指数：' + airnow[' no2 '] + ' \ n ' \
         + '           二氧化硫指数：' + airnow[' so2 '] + ' \ n ' \
         + '           一氧化碳指数：' + airnow[' co '] + ' \ n ' \
         + '           pm10指数：' + airnow[' pm10 '] + ' \ n ' \
         + '           pm25指数：' + airnow[' pm25 '] + ' \ n ' \
         + '           臭氧指数：' + airnow[' o3 '] + ' \ n ' \
         + ' ------------------------------------------ ' + ' \ n ' \
         + ' 1，' + 生活[0][' txt '] + ' \ n \ n ' \
         + ' 2，' + 生活[1][' txt '] + ' \ n \ n ' \
         + ' 3，' + 生活[2][' txt '] + ' \ n \ n ' \
         + ' 😄😊😉😍😘😚😜😝😳😁 ' + ' \ n \ n ' \
 \
    结果 = 结果 + '发送时间：' + nowTime + ' \ n '

返回结果


def auto_send（


    msg）：
weather = sendweather（'上海'，msg）
谎言 = bot.friends（）。搜索（你
'谎言'）[0]
QL = bot.friends（）搜索（û
'毛百万'）[0]
XLJ = bot.friends（）搜索（û
' 🌶 '）[0]
Lie.send（天气）
＃ ql.send（天气）
# xlj.send（sendweather（'烟台'，msg））


schedule.every（）。day.at（“ 13: 56 ”）.do（auto_send，'早上好，'）
schedule.every（）。day.at（“ 13: 57 ”）.do（auto_send，'晚上好，'）



而
真：
schedule.run_pending（）
time.sleep（1）