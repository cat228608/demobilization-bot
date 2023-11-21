import datetime
import vk_api
import time

ACCESS_TOKEN = '' #тут ваш ацес токен вк

def captcha_handler(captcha):
    key = input("Enter Captcha {0}: ".format(captcha.get_url())).strip()
    return captcha.try_again(key)

vk_session = vk_api.VkApi(token=ACCESS_TOKEN, captcha_handler=captcha_handler)


vk = vk_session.get_api()

user_id = '' #id вашего профиля вк

wall_posts = vk.wall.get(owner_id=user_id, count=1)
post_id = wall_posts['items'][0]['id']
message = wall_posts['items'][0]['text']

while True:
    target_date = datetime.datetime(2024, 6, 29) #дата дембеля или еще чего то
    now = datetime.datetime.now()
    delta = target_date - now
    total_seconds = delta.total_seconds()
    days = divmod(total_seconds, 86400)
    hours = divmod(days[1], 3600)
    minutes = divmod(hours[1], 60)
    seconds = minutes[1]
    text_msg = f"До даты {target_date} осталось: \nДней - {int(days[0])} дней, \nЧасов - {int(hours[0])} часов, \nМинут - {int(minutes[0])} минут, \nСекунд - {int(seconds)} секунд\n\nP.s Обновление таймера раз в 31 секунду потому вто инаве вк требует капчу"
    vk.wall.edit(owner_id=user_id, post_id=post_id, message=text_msg)
    time.sleep(31
