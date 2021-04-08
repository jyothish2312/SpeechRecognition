import speech_recognition as sr
import webbrowser as wb

r1 = sr.Recognizer()
r2 = sr.Recognizer()
r3 = sr.Recognizer()

with sr.Microphone() as src:
    print('Say google to search in google')
    print('...speak now-')
    command1 = r3.listen(src)
    print('voice captured')
    wakeword = r3.recognize_google(command1)
    print(wakeword)
if 'Google' in r2.recognize_google(command1):
    #r2 = sr.Recognizer()
    url = 'https://www.google.com/search?q='
    with sr.Microphone() as src:
        print('What do you want to search?')
        query = r2.listen(src)

        try:
            question = r2.recognize_google(query)
            print(question)
            wb.get().open_new(url+question)
        except sr.UnknownValueError:
            print('error')
        except sr.RequestError as e:
            print('failed to get results' .format(e))