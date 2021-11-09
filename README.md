# IgraGlagolovBot
В данном проекте присутствует два бота: бот для Vkontakte и бот для Telegram.  
Пользователь может задать свои вопросы боту и получить ответ.  
Ответ предоставляется с помощью сервиса DialogFlow (Используя машинное обучения выбирается ответ на вопрос пользователя)  
[Список возможных вопросов и ответов к боту, которые использовались для его обучения](https://github.com/Starcoding/IgraGlagolovBot/blob/main/training_phrases.json)

## Деплой
Боты размещены на площадке Heroku.
Для использования ```Google api credentials json``` на Heroku - [ссылка](https://stackoverflow.com/questions/47446480/how-to-use-google-api-credentials-json-on-heroku)

## Демо версии
[Ссылка на группу ВК](https://vk.com/public208703955)  
[Ссылка на телеграм бота](https://t.me/IgraGlagolov_bot)

### Демонстрация работы
<img src="https://i.imgur.com/Wf60DP1.gif" data-canonical-src="https://i.imgur.com/Wf60DP1.gif" height="250" />  

## Развертывание проекта
- Зарегистрируйтесь на DialogFlow, создайте агента для проекта, создайте сервисный аккаунт с необходимыми правами  
- Получите (скачайте) json файл для аутентификации сервисного аккаунта  

Пропишите переменные окружения  
- ```GOOGLE_APPLICATION_CREDENTIALS``` - путь до вашего json файла для сервисного аккаунта, например: ```"/igraglagolov-333212-65e2ab7f0b87.json"```
- ```PROJECT_ID``` - id Google Cloud проекта
- ```TELEGRAM_TOKEN``` - токен для вашего телеграм бота
- ```VK_API_KEY``` - токен для группы ВК

```pip install -r requirements.txt``` установит необходимые библиотеки  

Запустите любого бота:
- ```python3 vk_bot.py```
- ```python3 telegram_bot.py```

Обучите DialogFlow на своих фразах:  
```python3 create_intents.py``` - будет искать ```json``` файл под названием ```training_phrases.json```)  
Теперь вы можете попробовать написать сообщение запущенному боту.
