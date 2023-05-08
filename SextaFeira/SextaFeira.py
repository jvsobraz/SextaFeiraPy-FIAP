import speech_recognition as sr
import pyttsx3
import platform
from datetime import datetime
import requests

recon = sr.Recognizer()
texto_arquivo = []
with sr.Microphone(0) as mic:

    recon.adjust_for_ambient_noise(mic, duration=2)
    print("Diga ok sexta-feira")
    audio = recon.listen(mic)
    print("Reconhecendo...")
    frase = recon.recognize_google(audio, language='pt')
    print(frase)
    if 'ok sexta-feira' in frase:
        print("Sim, mestre. O que posso fazer?")
        en = pyttsx3.init()
        en.say("Sim, mestre. O que posso fazer?")
        en.runAndWait()
        while True:
            print("O que posso fazer?")
            recon.adjust_for_ambient_noise(mic, duration=2)
            audio = recon.listen(mic)
            print("Reconhecendo...")
            frase2 = recon.recognize_google(audio, language='pt')
            frase2 = frase2.upper()
            print(frase2)
            if 'CADASTRAR EVENTO NA AGENDA' in frase2:
                print("Ok, qual evento devo cadastrar?")
                en = pyttsx3.init()
                en.say("Ok, qual evento devo cadastrar?")
                en.runAndWait()
                recon.adjust_for_ambient_noise(mic, duration=2)
                audio = recon.listen(mic)
                print("Reconhecendo...")
                frase3 = recon.recognize_google(audio, language='pt')
                print(frase3)
                with open(f"evento_cadastrado.csv", "a") as inv:
                    for linha in frase3:
                        inv.write(linha)
                pass
            elif 'LER AGENDA' in frase2:
                with open(f"evento_cadastrado.csv", "r") as arq:
                    for line in arq:
                        texto_arquivo.append(line)
                print(texto_arquivo)
                pass
            elif 'QUE HORAS SÃO' in frase2:
                agora = datetime.now()
                hora = agora.hour
                minuto = agora.minute
                texto = "Agora são" + str(hora) + "horas e" + str(minuto) + "minutos"
                en = pyttsx3.init()
                en.setProperty('rate', 155)
                en.setProperty('value', 1.0)
                en.setProperty('voice', b'brasil')
                en.say(texto)
                en.runAndWait()
                pass
            elif 'QUE DIA É HOJE' in frase2:
                dia = datetime.today().day
                mes = datetime.today().month
                ano = datetime.today().year
                texto = "dia" + str(dia) + "do mês" + str(mes) + "do ano" + str(ano)
                en = pyttsx3.init()
                en.setProperty('rate', 155)
                en.setProperty('volume', 1.0)
                en.setProperty('voice', b'brasil')
                en.say(texto)
                en.runAndWait()
                print("Posso fazer mais algo?")
                pass
            elif 'INFORMAÇÃO DO COMPUTADOR' in frase2:
                print('Platform processor:', platform.processor())
                print('Platform architecture:', platform.architecture())
                print('System info:', platform.system())
                pass
            elif 'COMO ESTÁ O CLIMA' in frase2:
                url = 'https://wttr.in/'
                parametros = {'format': '%C'}
                clima = requests.get(url, params=parametros).text.strip()
                en.say(f'O clima atual está {clima}.')
                en.runAndWait()
                pass
            elif 'FALE SOBRE PYTHON' in frase2:
                texto = 'Python é uma linguagem de programação interpretada, de alto nível e de propósito geral. Ela é fácil de aprender e ler, e possui uma grande variedade de bibliotecas que facilitam o desenvolvimento de projetos complexos. É amplamente utilizada em diversas áreas, como ciência de dados, inteligência artificial, desenvolvimento web, automação de tarefas, entre outras. O nome "Python" é inspirado no grupo de comédia britânico Monty Python.'
                en = pyttsx3.init()
                en.say(texto)
                en.runAndWait()
                pass
            elif 'FALE SOBRE A FIAP' in frase2:
                texto = 'A FIAP é uma das principais instituições de ensino superior em tecnologia do Brasil, oferecendo cursos de graduação, pós-graduação e MBA nas áreas de Tecnologia da Informação, Gestão e Negócios, Marketing Digital e Design. Com uma metodologia de ensino focada em projetos, a FIAP busca formar profissionais capacitados e preparados para atender às demandas do mercado de trabalho. Além disso, a instituição conta com uma infraestrutura moderna e tecnológica, incluindo laboratórios equipados com equipamentos de ponta e um corpo docente altamente qualificado, formado por professores atuantes no mercado. A FIAP é reconhecida como uma das melhores instituições de ensino em tecnologia do país e tem contribuído significativamente para o desenvolvimento do setor de TI no Brasil.'
                en = pyttsx3.init()
                en.say(texto)
                en.runAndWait()
                pass
            elif 'CITE UM POEMA' in frase2:
                texto = """O amor é fogo que arde sem se ver;
                        É ferida que dói e não se sente;
                        É um contentamento descontente;
                        É dor que desatina sem doer."""
                en = pyttsx3.init()
                en.say(texto)
                en.runAndWait()
                pass
            elif 'EMERGÊNCIA' in frase2:
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
                en = pyttsx3.init()
                en.say(texto)
                en.runAndWait()
                pass
            elif frase2 == 'PARAR':
                break

        #except:
    #   print("Erro")
