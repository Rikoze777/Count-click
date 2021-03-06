# Обрезка ссылок с помощью Битли

Cокращение URL-адресов упрощает громоздкие веб-адреса до десяти символов. Сокращенный URL-адрес по-прежнему отправляет вас на исходный URL-адрес (унифицированный указатель ресурсов). Преимущества включают лучшее отображение, лучшие функции маркетинга и отслеживания.

### Как установить

Для использования необходимо: 
1. Зарегестрироваться на сайте https://app.bitly.com/. 
2. Получить `token` на сайте. 
3. Создайте пустой `.env` файл в корне с исполнительным файлом `main.py`

4. Поместите значение токена в `.env` файл, в переменную: 
```python
BITLY_TOKEN = "Bearer ваш токен"
```

Python3 должен быть уже установлен. 
Затем используйте `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```
### Запуск скрипта:
```bash
python3 main.py url
```
### Пример успешного запуска
В случае если данная ссылка является укороченной:
```
python3 main.py https://bit.ly/3yZaCHC
Количество переходов по ссылке битли 0
```
В случае если данная ссылка не является укороченной:
```
python3 main.py https://dvmn.org
https://bit.ly/3yZaCHC
```
### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).
