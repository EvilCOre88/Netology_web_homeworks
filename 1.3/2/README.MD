# Домашнее задание к лекции «Docker»

## Задание 2

- Клонируйте репозиторий командой <code>git clone https://github.com/EvilCOre88/web-hw.git</code> и перейдите в [каталог](/1.3/2) с Docker-файлом

> Для создания образа введите команду <code>docker build -t <название вашего образа (любое)> .</code>
  
> После создания можете его запускать командой <code>docker run --name <имя контейнера (любое)> -d -p 8888:8000 <название образа, созданный ранее></code>.

<details>
<summary>Опции:</summary>
Порт 8888 можете поменять на любой свой, как вам будет удобно.  
</details>

- Теперь можете проверить работу контейнера перейдя на [ваш сервер](http://localhost:8888/)
- Для работы через браузер перейдите по адресу [api](http://localhost:8888/api/)
  
> Для проверки работоспособности посылайте api-запросы удобным способом (IDE, postman, curl-запросы)

> Примеры:

<code>GET http://localhost:8888/api/clients/
Content-Type: application/json</code>

<code>POST http://46.183.163.79:8000/api/clients/
Content-Type: application/json

{  
  "id": 1,
  "phone": 79773232186,
  "code": 977,
  "tag": "tele",
  "timezone": "+0300"  
}</code>
