import platform
import speech_recognition as sr
import pyttsx3
from datetime import datetime
import requests
from pydub import AudioSegment
from pydub.playback import play

reconhecimento = sr.Recognizer()
voz = pyttsx3.init()
voz.setProperty('volume', 1.0)

nome = input('Digite o seu nome: ')

def cadastrar_evento():
    print("Ok, qual evento devo cadastrar?")
    voz.say("Ok, qual evento devo cadastrar?")
    voz.runAndWait()
    reconhecimento.adjust_for_ambient_noise(mic, duration=2)
    audio = reconhecimento.listen(mic)
    print("Reconhecendo...")
    frase = reconhecimento.recognize_google(audio, language='pt')
    print(frase)
    with open(f"Evento.txt", "a") as evento:
        for linha in frase:
            evento.write(linha)
def ler_evento():
    with open(f"Evento.txt", "r") as evento:
        texto = []
        for linha in evento:
            texto.append(linha)
    print(texto)
    voz.say(texto)
    voz.runAndWait()
def falar_horas():
    agora = datetime.now().strftime('%H:%M')
    print(f'Agora são: {agora}')
    voz.say(f'Agora são: {agora} horas')
    voz.runAndWait()
def falar_python():
    texto = '''
    Python é uma linguagem de programação interpretada, de alto nível e de propósito geral. 
    Ela é fácil de aprender e ler, e possui uma grande variedade de bibliotecas que facilitam o desenvolvimento de projetos complexos. 
    É amplamente utilizada em diversas áreas, como ciência de dados, inteligência artificial, desenvolvimento web, automação de tarefas, entre outras.
    O nome "Python" é inspirado no grupo de comédia britânico Monty Python.
    '''
    print(texto)
    voz.say(texto)
    voz.runAndWait()
def falar_fiap():
    texto = '''
    A FIAP é uma das principais instituições de ensino superior em tecnologia do Brasil, 
    oferecendo cursos de graduação, pós-graduação e MBA nas áreas de Tecnologia da Informação, Gestão e Negócios, Marketing Digital e Design. 
    Com uma metodologia de ensino focada em projetos, 
    a FIAP busca formar profissionais capacitados e preparados para atender às demandas do mercado de trabalho. 
    Além disso, a instituição conta com uma infraestrutura moderna e tecnológica, 
    incluindo laboratórios equipados com equipamentos de ponta e um corpo docente altamente qualificado, formado por professores atuantes no mercado. 
    A FIAP é reconhecida como uma das melhores instituições de ensino em tecnologia do país e tem contribuído significativamente para o desenvolvimento
    do setor de TI no Brasil.
    '''
    print(texto)
    voz.say(texto)
    voz.runAndWait()
def falar_emergencia():
    numeros_emergencia = {
        'Polícia Militar': '190',
        'Corpo de Bombeiros': '193',
        'Samu': '192',
        'Defesa Civil': '199',
        'Polícia Rodoviária Federal': '191',
        'Polícia Federal': '194',
        'Polícia Civil': '197',
    }
    texto = 'Em caso de emergência, ligue para:'
    for nome, numero in numeros_emergencia.items():
        texto += f'\n{nome}: {numero}'
    print(texto)
    voz.say(texto)
    voz.runAndWait()
def falar_poema():
    texto = """O amor é fogo que arde sem se ver;
            É ferida que dói e não se sente;
            É um contentamento descontente;
            É dor que desatina sem doer."""
    print(texto)
    voz.say(texto)
    voz.runAndWait()
def clima_hoje():
    url = 'https://wttr.in/'
    parametros = {'format': '%C'}
    clima = requests.get(url, params=parametros).text.strip()
    voz.say(f'O clima atual está {clima}.')
    voz.runAndWait()
def falar_adeus():
    texto = f'Adeus mestre {nome}'
    print(texto)
    voz.say(texto)
    voz.runAndWait()

with sr.Microphone() as mic:

    reconhecimento.adjust_for_ambient_noise(mic, duration=3)
    print("Diga ok sexta-feira para iniciar a aplicação")
    audio = reconhecimento.listen(mic)
    print("Reconhecendo...")
    try:
        fala = reconhecimento.recognize_google(audio, language='pt')
        print(fala)
        if 'ok sexta-feira' in fala:
            print(f"Sim, mestre {nome}. O que posso fazer?")
            voz.say(f"Sim, mestre {nome}. O que posso fazer?")
            voz.runAndWait()
            while True:
                print("O que posso fazer hoje por você?")
                reconhecimento.adjust_for_ambient_noise(mic, duration=2)
                audio = reconhecimento.listen(mic)
                print("Reconhecendo...")
                try:
                    frase = reconhecimento.recognize_google(audio, language='pt')
                    frase = frase.upper()
                    print(frase)
                    if 'CADASTRAR EVENTO NA AGENDA' in frase:
                        cadastrar_evento()
                    elif 'LER AGENDA' in frase:
                        ler_evento()
                    elif 'QUE HORAS SÃO' in frase:
                        falar_horas()
                    elif 'FALE SOBRE PYTHON' in frase:
                        falar_python()
                    elif 'FALE SOBRE A FIAP' in frase:
                        falar_fiap()
                    elif 'ESTOU COM UMA EMERGÊNCIA' in frase:
                        falar_emergencia()
                    elif 'CITE UM POEMA' in frase:
                        falar_poema()
                    elif 'COMO ESTÁ O CLIMA' in frase:
                        clima_hoje()
                    elif 'ENCERRAR' or 'SAIR' in frase:
                        falar_adeus()
                        break
                except sr.UnknownValueError:
                    print("Não entendi o que você falou.")
                except sr.RequestError as e:
                    print(f"Não foi possível realizar a operação. Erro: {e}")
    except sr.UnknownValueError:
        print("Não entendi o que você falou.")
    except sr.RequestError as e:
        print(f"Não foi possível realizar a operação. Erro: {e}")
