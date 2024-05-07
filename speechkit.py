import requests
from config import *
from creds.creds import get_creds  # модуль для получения токенов

iam_token, folder_id = get_creds()  # получаем iam_token и folder_id из файлов

def speech_to_text(data):
    # iam_token, folder_id для доступа к Yandex SpeechKit
    # Указываем параметры запроса
    params = "&".join([
        "topic=general",  # используем основную версию модели
        f"folderId={'b1g566iiqn0ovmhs44gr'}",
        "lang=ru-RU"  # распознаём голосовое сообщение на русском языке
    ])

    # Аутентификация через IAM-токен
    headers = {
        'Authorization': f'Bearer {"t1.9euelZrHl8ubycmPlpCVmI6Rz8yPl-3rnpWakM7Mio2OzM6bnZfJk4qVnZTl9PdTaRZO-e9OJjzC3fT3ExgUTvnvTiY8ws3n9euelZqUz8_KksebzMaYyp2Uisiaje_8xeuelZqUz8_KksebzMaYyp2Uisiajb3rnpWazYyNzJnHzYmWisqVmMvIj8m13oac0ZyQko-Ki5rRi5nSnJCSj4qLmtKSmouem56LntKMng.B6MsiOAqZaipNjN4EXHztAAtSAMg-H7X-RbhWCbYFvl2wHSFfcRjsykppsDRk8yaCDoaJP2OQlh04Y-5JrF5Dg"}',
    }

    # Выполняем запрос
    response = requests.post(
        f"https://stt.api.cloud.yandex.net/speech/v1/stt:recognize?{params}",
        headers=headers,
        data=data
    )

    # Читаем json в словарь
    decoded_data = response.json()
    # Проверяем, не произошла ли ошибка при запросе
    if decoded_data.get("error_code") is None:
        return True, decoded_data.get("result")  # Возвращаем статус и текст из аудио
    else:
        return False, "При запросе в SpeechKit возникла ошибка"


def text_to_speech(text):
    # iam_token, folder_id для доступа к Yandex SpeechKit

    # Аутентификация через IAM-токен
    headers = {
        'Authorization': f'Bearer {"t1.9euelZrHl8ubycmPlpCVmI6Rz8yPl-3rnpWakM7Mio2OzM6bnZfJk4qVnZTl9PdTaRZO-e9OJjzC3fT3ExgUTvnvTiY8ws3n9euelZqUz8_KksebzMaYyp2Uisiaje_8xeuelZqUz8_KksebzMaYyp2Uisiajb3rnpWazYyNzJnHzYmWisqVmMvIj8m13oac0ZyQko-Ki5rRi5nSnJCSj4qLmtKSmouem56LntKMng.B6MsiOAqZaipNjN4EXHztAAtSAMg-H7X-RbhWCbYFvl2wHSFfcRjsykppsDRk8yaCDoaJP2OQlh04Y-5JrF5Dg"}',
    }
    data = {
        'text': text,  # текст, который нужно преобразовать в голосовое сообщение
        'lang': 'ru-RU',  # язык текста - русский
        'voice': 'filipp',  # мужской голос Филиппа
        'folderId': 'b1g566iiqn0ovmhs44gr',
    }
    # Выполняем запрос
    response = requests.post(
        'https://tts.api.cloud.yandex.net/speech/v1/tts:synthesize',
        headers=headers,
        data=data
    )
    if response.status_code == 200:
        return True, response.content  # возвращаем статус и аудио
    else:
        return False, "При запросе в SpeechKit возникла ошибка"