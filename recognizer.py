import speech_recognition as sr


def listen_mic():
    mic = sr.Recognizer()

    with sr.Microphone() as source:
        mic.adjust_for_ambient_noise(source)
        print('GRAVANDO >> Fale agora <<\n')
        audio = mic.listen(source)
   
    try:
        text = mic.recognize_google(audio, language='pt-BR')
        print(text)
    except sr.UnknownValueError:
        print('Fala não reconhecida. Tente novamente')

    return text

def write_txt(text):
    with open('text.txt', 'w', encoding='utf-8') as f:
        f.write(text)


text = text = listen_mic()
write_txt(text)


