# Мои проекты
## Log_Online_VK
Логирование онлайна пользователя ВК

**Для работы необходимо:** библиотека requests

**Функция:** при запуске скрипт предлагает ввести адрес аккаунта VK (его можно изменить позже в настройках). После запуска потока скрипт пытается получить имя пользователя, после чего создаёт txt файл с именем пользователя и начинает парсить страницу на наличие статуса. После успешного получения статуса скрипт записывает его в формате дата, время и статус. Для удобства чтения файла на выходе был сделан следующий трюк: если предыдущий статус страницы совпадает с текущим, то в файл не записывается ничего. Это сделано для того, чтобы не было повторов статуса, и файл на выходе получался менее громоздким и более удобным для чтения.
_____________
## Chiper
Шифр Цезаря и шифр номером

**Приложение поддерживает работу только с английской раскладкой!** Данное приложение я создавал около года назад, поэтому не судите строго.

**Для работы необходимо:** библиотека tkinter

**Функция:** при запуске скрипта открывается GUI интерфейс приложения для шифровки текста. На выбор есть два вида шифра: шифр Цезаря и номером(подстановочный). 

**Шифр Цезаря**
- Для однострочного текста можно использовать текущее меню интерфейса: выбирается сдвиг алфавита, вводится сообщение для шифра и нажимается кнопка Зашифровать. Для удобства есть кнопки Скопировать шифрованный текст или расшифрованный.
- Для многострочного текста (или ввода из файла) рекомендуется перейти в раздел "Big text". Для того, чтобы импортировать текст или шифр, используется Файл -> Открыть слева или справа соответственно, после чего выбирается сдвиг алфавита и нажимается нужная кнопка.

Скрипт также поддерживает различные знаки препинания и способен начинать новые предложения с заглавной буквы.

**Шифр номером**

С однострочным и многострочным вводом всё аналогично с шифром Цезаря. Для шифровки текста подстановочным способом необходимо ввести текст в нужное поле и нажать соответствующую кнопку. Алгоритм шифрования текста следующий: буквам в словаре соответствуют их порядковые номера, символам - другие символы. На это и происходит замена.
