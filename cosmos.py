import colorama
import requests
from bs4 import BeautifulSoup
import speech_recognition as sr

r2= sr.Recognizer()
r1 = sr.Recognizer()
print(colorama.Fore.BLUE,'Hi there! This is COSMOS')
def query():
    with sr.Microphone() as source:
        print(colorama.Fore.YELLOW,'Ask your query')
        print(colorama.Fore.RESET, )
        audio = r2.listen(source)

        try:
            user_query = r2.recognize_google(audio)

            print('Your question is...')
            print(user_query + ' ?')
            URL = "https://www.google.co.in/search?q=" + user_query

            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36'
            }
            page = requests.get(URL, headers=headers)
            soup = BeautifulSoup(page.content, 'html.parser')
            try:
                result = soup.find(class_='Z0LcW XcVN5d').get_text()
            except Exception:
                result = soup.find(class_='Z0LcW XcVN5d AZCkJd').get_text()
            print(colorama.Fore.LIGHTMAGENTA_EX,result)
        except sr.UnknownvValueError:
            print('error')
        except sr.RequestError as e:
            print('failed'.format(e))


while True:
    try:
        query()
    except Exception:
        print('Sorry no result, please be clear')
    with sr.Microphone() as source:
        print(colorama.Fore.LIGHTGREEN_EX,'Want to continue say "CONTINUE" or say "END"')
        audio = r1.listen(source)

        try:
            user_input = r1.recognize_google(audio)
            if user_input!='continue':
                print(colorama.Fore.MAGENTA,'Thankyou For Using...')
                break

        except sr.UnknownvValueError:
            print(colorama.Fore.MAGENTA,'Thankyou For Using...')
            break

        except sr.RequestError as e:
            print(colorama.Fore.MAGENTA,'Thankyou'.format(e))
            break