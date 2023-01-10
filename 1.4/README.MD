# Домашнее задание к лекции «Docker Compose»

## Приложение для рассылки сообщений клиентам

> С помощью этого приложения можно создавать рассылки по клиентам (в том числе и отложенные) через стороний api-сервис для отправки смс-сообщений.

<details>
** Структура ссылок и api-запросов сервиса: **


- список рассылок: <code>http://localhost:8888/api/mailing-lists/</code>

	<details>
	<summary>Структура тела POST api-запроса:</summary>

	```
	{
		"mailing_date_time": null,
		"message": "",
		"filter_code": null,
		"filter_tag": "",
		"finish_date_time": null
	}
	```

	</details>

- детальный список рассылок: <code>http://localhost:8888/api/mailing-lists-details/</code>

- список клиентов: <code>http://localhost:8888/api/clients/</code>

	<details>
	<summary>Структура тела POST api-запроса:</summary>

	```
	{
		"phone": null,
		"code": null,
		"tag": "",
		"timezone": ""
	}
	```

	</details>

- список сообщений: <code>http://localhost:8888/api/messages/</code>

- детальный список сообщений: <code>http://localhost:8888/api/message-detail/</code>

- отправка рассылок: <code>http://localhost:8888/api/send/</code>

	<details>
	<summary>Структура тела POST api-запроса:</summary>

	```
	{
		"mailing_list_id": ""
	}
	```

	</details> 
</details>

## Запуск приложения:

- Клонируйте репозиторий командой <code>git clone https://github.com/EvilCOre88/web-hw.git</code> и перейдите в [каталог](/1.4) с Docker-файлами

> Для создания и запуска контейнеров введите команду <code>docker-compose up -d</code>

<details>
<summary>Опции:</summary>
Порты можете поменять на любые свои в docker-compose файле.  
</details>

- Теперь можете проверить работу приложения перейдя на [ваш сервер](http://localhost:8888/) (http://localhost:8888/)
- Для работы через браузер перейдите по адресу [api](http://localhost:8888/api/) (http://localhost:8888/api/)
  
> Для проверки работоспособности посылайте api-запросы удобным способом (IDE, postman, curl-запросы)

> Примеры:
```
GET http://localhost:8888/api/clients/
Content-Type: application/json
```

```
POST http://localhost:8888/api/clients/
Content-Type: application/json

{  
  "id": 1,
  "phone": 79773232186,
  "code": 977,
  "tag": "tele",
  "timezone": "+0300"  
}
```

> Для проверки рассылки (рассылка уже должна быть заполнена) посылайте POST api-запрос на <code>http://localhost:8888/api/send/</code> по форме:
```
POST http://localhost:8888/api/send/
Content-Type: application/json

{
	"mailing_list_id": <id рассылки>
}
```

