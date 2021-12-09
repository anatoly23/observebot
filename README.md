# observebot
Бот оперативного вывода информации с камер видеонаблюдения объектов строительства

## Установка бота.

Создаем бота через BotFather и получаем токен, его нужно сохранить в файл **.env** 

**TELEBOT_BOT_TOKEN = "Ваш ID"**

Создаем канал и добавляем туда нашего бота и бота **@myidbot**. Выполняем **/getgroupid@myidbot** и получем **ID группы**. 

Вставляем его в файл **.env**  
**GROUP_CHAT_ID = "ID Группы"** 

Выкидываем бота @myidbot из нашего канала.

Создаем самоподписной сертификат по [инструкции](https://core.telegram.org/bots/self-signed)

С помощю файла **webhooktelegram.html** переключаем бота с режима опроса на режим отправки сообщений на наш URL **webhooks/bot**, не забываем указать порт **443** и наш открытый сертификат.

Скачиваем проект и выполняем pip install -r requirements.txt

Запускаем бота python manage.py runserver_plus 0.0.0.0:443 --cert-file public.pem --key-file private.pem
