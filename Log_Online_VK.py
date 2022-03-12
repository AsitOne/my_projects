import re
import requests
import time
from threading import Thread

CONTINUE = True  # Константа, необходимая для выхода из цикла потока.


def get_name_acc(url: str) -> str:
    """
    Функция получает на вход ссылку и пытается определить имя аккаунта, в случае успеха возвращает его.
    В случае, если error404 (страница не найдена) есть в тексте возвращаемой страницы, вовращается Error и
    обрабатывается
    :param url:
    :return name:
    """
    try:
        response = requests.get(url)
        name = re.findall('<h2 class=\"op_header\">(\w* \w*)', response.text)
    except:
        return 'Output'
    else:
        if 'error404' in response.text:
            return 'Error'
        return name[0] + '.txt'


def monitoring(acc: str = ''):
    """
    Функция вызывается фоновым потоком и каждые 5 секунд получает страницу, парсит её статус и записывает этот статус в
    файл с именем аккаунта.
    :param acc:
    """
    if not acc:
        print('Вы ввели пустую строку!')
    else:
        last_online = []  # Нужен для того, чтоб функция не записывала в файл один и тот же статус. Является своего рода
        #  стеком статусов пользователя.
        iteration = 0  # создал для просмотра предыдущего статуса аккаунта.
        url = 'https://vk.com/' + acc
        name = get_name_acc(url)
        if name == 'Error':
            print('Страница не существует!')
        elif name == 'Output':
            print('Ошибка получения имени страницы')
        else:
            try:  # Попытка открытия файла
                file = open(name, 'a')
            except Exception as ex:
                print('Ошибка создания файла.')
            else:
                while CONTINUE:
                    try:
                        response = requests.get(url)
                        status = "online" if '<span class="pp_last_activity_text">Online</span>' in response.text else \
                            "offline"  # Проверка и получение статуса аккаунта в возвращаемом тексте страницы.
                    except requests.HTTPError as http_err:
                        print(f'HTTP error: {http_err}')
                        break
                    except Exception as err:
                        print(f'Неизвестная ошибка: {err}')
                        break
                    else:
                        if not last_online:  # Первая итерация, запись в любом случае
                            file.write(f"[{time.strftime('%d/%m/%Y %H:%M:%S', time.localtime())}] {status} \n")
                            last_online.append(status)
                            iteration += 1
                        elif last_online[iteration - 1] != status:  # последующие итерации, запись только если
                            #  предыдущий статус не равен текущему.
                            file.write(f"[{time.strftime('%d/%m/%Y %H:%M:%S', time.localtime())}] {status} \n")
                            last_online.append(status)
                            iteration += 1
                        time.sleep(5)
                file.close()
    print('Завершение потока')


if __name__ == '__main__':
    print('Программа логирует онлайн пользователя VK. Для работы требуется интернет соединение!')
    page_vk = input('Введите адрес страницы (Без https://vk.com): ')
    while True:
        choice = input('1) Запуск;\n'
                       '2) Настройки;\n'
                       '0) Выход.\n'
                       'Ввод: ')
        match choice:
            case '1':
                thread = Thread(target=monitoring, args=(page_vk,), daemon=True)
                thread.start()
                choice_run = input('Поток запущен. Чтобы завершить - введите любой символ и дождитесь завершения.\n')
                CONTINUE = False
                thread.join()
            case '2':
                choice_settings = input(f'Текущая страница: {page_vk} (изменить - 1), \n'
                                        f'Ввод (назад - 0): ')
                match choice_settings:
                    case '1':
                        page_vk = input('Введите адрес страницы (Без https://vk.com): ')
                    case '0':
                        pass
                    case _:
                        print('Введите корректные данные!')
            case '0':
                print('Завершение работы.')
                break
            case _:
                print('Введите корректные данные!')
        CONTINUE = True
