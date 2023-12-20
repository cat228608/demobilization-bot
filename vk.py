import datetime
import vk_api
import time

ACCESS_TOKEN = '' #тут ваш ацес токен вк

def captcha_handler(captcha):
    key = input("Enter Captcha {0}: ".format(captcha.get_url())).strip()
    return captcha.try_again(key)

vk_session = vk_api.VkApi(token=ACCESS_TOKEN, captcha_handler=captcha_handler)


vk = vk_session.get_api()

user_id = '492361343' #id вашего профиля вк

while True:
    try:
    	target_date = datetime.datetime(2024, 6, 29) #дата дембеля или еще чего то
    	now = datetime.datetime.now()
    	delta = target_date - now
    	total_seconds = delta.total_seconds()
    	days = divmod(total_seconds, 86400)
    	hours = divmod(days[1], 3600)
    	minutes = divmod(hours[1], 60)
    	seconds = minutes[1]
    	text_msg = f"До даты ДМБ осталось: \n⌛{int(days[0])} дней, {int(hours[0])}ч : {int(minutes[0])}м : {int(seconds)}с\n\nUpdate: 31s"
    	vk.status.set(text=text_msg)
    	time.sleep(31)
    except:
    	time.sleep(31)
    	continue
