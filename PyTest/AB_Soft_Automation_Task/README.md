**AB Soft Automation Task**

**Для запуска теста необходимо:**

Важно! Убедитесь, что структура файлов и папок такая: **скриншот структуры**  https://picua.org/image/annotation-2020-05-03-014227.p9w6MB

**1.**/ Подготовить интерпретатор Python

**2.**/ Установить все необходимые плагины из **requirements.txt**

**3.**/ Получить API Key от GMAIL, чтобы можно было отправить письмо, ссылка с инструкцией как это сделать: https://developers.google.com/gmail/api/quickstart/python

**3.1.**/ После получения '**client_id.json**', этот файл необходимо поместить в папку '**helpers**'

**3.2.**/ Изменить в файле '**send_mail.py**' в строке (номер строки #143) **sender = "test2020api@gmail.com"**' изменить адрес почты "test2020api@gmail.com" на свой 

**4.**/ Для запуска теста необходимо ввести в консоль команду **pytest -v -s test_send_mail.py**

**Опционально:**

**5./** Установка Allure Report (чтобы после его можно было просмотреть), ссылка с инструкцией как это сделать: https://docs.qameta.io/allure/#_get_started

**5.1.**/ Чтобы cгенерировать Allure Report при прохождении теста, команда **pytest -v -s --alluredir="reports" test_send_mail.py**

**5.2.**/ Чтобы просмотреть Allure Report необходимо ввести в консоль команду **allure serve -o reports**

**5.3.**/ Пример Allure Report'a по **данному тесту** представлен по ссылке: https://angry-yonath-4ab6ca.netlify.app/#suites/92a6db84f76545974e48f7c1f27d8f15/d76db9c3a6db1f93/

**Environment**: 

1. Chrome Version 81.0.4044.129;

2. chromedriver 81.0.4044.69;

3. Python v3.7.6;

4. IDE: PyCharm 2019.3.2; 

5. WIN 10;
