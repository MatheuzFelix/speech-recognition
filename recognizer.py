from tkinter.filedialog import askopenfilename
import speech_recognition as sr
import PySimpleGUI as sg
import docx2txt
import pyttsx3
import PyPDF2
import os


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

def text_speech(text):
    speaker = pyttsx3.init()

    speaker.setProperty('voice', 'brazil' )
    rate =speaker.getProperty('rate')
    speaker.setProperty('rate', rate-25)

    speaker.say(text)
    speaker.runAndWait()

def read_file():
    file_path = askopenfilename(title='Selecione um arquivo')
    file_name = os.path.basename(file_path)

    if file_name.split(".")[-1] == 'txt':
        with open(file_path) as text_to_read:
            txt = text_to_read.read()
            text_speech(txt)

    elif file_name.split(".")[-1] == 'docx':
        docx_text = docx2txt.process(file_path)
        text_speech(docx_text)

    elif file_name.split(".")[-1] == 'pdf':
        pdf_file_obj = open(file_path, 'rb')
        pdf_reader = PyPDF2.PdfFileReader(pdf_file_obj) 
        page_obj = pdf_reader.getPage(0) 
        pdf_text = page_obj.extractText() 
        text_speech(pdf_text)
        pdf_file_obj.close()

    else:
        print('selecione um arquivo "txt", "pdf" ou  "docx"')
