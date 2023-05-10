import speech_recognition as sr
import pyttsx3
from datetime import datetime
import requests
import random


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


def falar_clima():
    url = 'https://wttr.in/'
    parametros = {'format': '%C'}
    clima = requests.get(url, params=parametros).text.strip()
    temperatura = clima.split()[0]

    mensagem = f'Atualmente, a temperatura é de {clima} graus Celsius, mestre {nome}.'

    if temperatura > '30':
        mensagem += ' Está um dia quente lá fora, não se esqueça de se hidratar e passar o protetor solar!'
    elif temperatura < '10':
        mensagem += ' Está fazendo bastante frio, certifique-se de se vestir seu agasalho!'

    print(mensagem)
    voz.say(mensagem)
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

def falar_receita_bolo():
    texto = '''
    Claro, aqui está uma receita simples de bolo de chocolate:

    Ingredientes:

    1 e 3/4 xícaras de farinha de trigo
    3/4 xícara de cacau em pó
    1 e 1/2 colheres de chá de bicarbonato de sódio
    1 colher de chá de sal
    1 e 3/4 xícaras de açúcar
    1/2 xícara de óleo vegetal
    2 ovos
    1 colher de chá de essência de baunilha
    1 xícara de leite
    1 xícara de água quente

    Instruções:

    Pré-aqueça o forno a 180 graus Celsius.
    Em uma tigela grande, misture a farinha, o cacau em pó, o bicarbonato de sódio e o sal. Reserve.
    Em outra tigela, misture o açúcar, o óleo vegetal, os ovos e a essência de baunilha até que fiquem bem combinados.
    Adicione a mistura seca de farinha à mistura úmida de açúcar e ovos, alternando com o leite. 
    Misture bem até que a massa esteja homogênea.
    Adicione a água quente e misture novamente até ficar bem combinado.
    Despeje a massa em uma assadeira untada e enfarinhada e leve ao forno por cerca de 30 a 35 minutos, 
    ou até que um palito inserido no centro do bolo saia limpo.
    Retire do forno e deixe esfriar antes de servir. 
    Se quiser, polvilhe açúcar de confeiteiro ou decore com raspas de chocolate.

    Bom apetite!
    '''
    print(texto)
    voz.say(texto)
    voz.runAndWait()

def falar_to_be():
    texto = '''
    O verbo "to be" é um verbo muito importante em inglês, pois ele é utilizado para indicar estados, 
    qualidades e identidades. Ele é um verbo irregular, o que significa que não segue um padrão 
    regular de conjugação em todos os tempos e formas verbais.

    Aqui estão as conjugações básicas do verbo "to be" no presente, passado e futuro simples:

    Presente simples:

    I am (Eu sou/estou)
    You are (Você é/está)
    He/She/It is (Ele/Ela é/está)
    We are (Nós somos/estamos)
    You are (Vocês são/estão)
    They are (Eles/Elas são/estão)

    Passado simples:

    I was (Eu era/estava)
    You were (Você era/estava)
    He/She/It was (Ele/Ela era/estava)
    We were (Nós éramos/estávamos)
    You were (Vocês eram/estavam)
    They were (Eles/Elas eram/estavam)

    Futuro simples:

    I will be (Eu serei/estarei)
    You will be (Você será/estará)
    He/She/It will be (Ele/Ela será/estará)
    We will be (Nós seremos/estaremos)
    You will be (Vocês serão/estarão)
    They will be (Eles/Elas serão/estarão)

    O verbo "to be" também pode ser usado para formar a voz passiva em inglês, além de ter outras funções gramaticais
    importantes, como formar perguntas e respostas curtas. É um verbo muito comum na 
    língua inglesa e é essencial para se comunicar bem em inglês.
    '''
    print(texto)
    voz.say(texto)
    voz.runAndWait()

def falar_cnh():
    texto = '''
    Para tirar a CNH (Carteira Nacional de Habilitação) no Brasil, você precisa seguir alguns passos importantes:

    Requisitos básicos: para começar, você precisa ter no mínimo 18 anos de idade, 
    ser alfabetizado e possuir documento de identificação válido (RG, por exemplo).

    Fazer o curso teórico: o curso teórico é oferecido por autoescolas credenciadas pelo Detran (Departamento Estadual de Trânsito). Ele é composto por aulas teóricas sobre legislação de trânsito, direção defensiva, primeiros socorros e meio ambiente. Ao final do curso, é necessário fazer uma prova teórica para obter aprovação.

    Fazer o exame médico: o exame médico é realizado por um médico credenciado pelo Detran. Ele verifica as condições físicas e mentais do candidato para dirigir. O exame inclui avaliação de visão, coordenação motora, equilíbrio e outros aspectos relacionados à saúde.

    Fazer o curso prático: o curso prático é realizado na autoescola credenciada pelo Detran 
    e é composto por aulas práticas de direção veicular. O número de aulas pode variar de acordo com 
    a autoescola e com a necessidade do candidato. É necessário ter um número mínimo de aulas práticas para se 
    submeter ao exame prático.

    Fazer o exame prático: o exame prático é realizado por um avaliador do Detran e consiste em uma avaliação de 
    habilidades de direção veicular. O candidato precisa demonstrar habilidade para dirigir em diferentes 
    situações de trânsito. Se aprovado, o candidato recebe a CNH.

    É importante lembrar que o processo para tirar a CNH pode variar um pouco de estado para estado no Brasil. 
    Além disso, o custo do processo pode variar bastante, dependendo da autoescola escolhida e da cidade onde você mora.
    '''
    print(texto)
    voz.say(texto)
    voz.runAndWait()

def falar_fato():
    texto = '''
    Claro! Sabia que existem formigas que são capazes de "agricultura"? 
    Algumas espécies de formigas, como as chamadas "saúvas", cultivam um tipo específico de fungo em seus ninhos, 
    que servem como alimento para a colônia. As formigas cortam pedaços de folhas e as levam para seus ninhos, 
    onde alimentam o fungo com essas folhas. Em troca, o fungo produz uma substância nutritiva que as formigas consomem. 
    É incrível como a natureza é capaz de nos surpreender!
    '''
    print(texto)
    voz.say(texto)
    voz.runAndWait()

def piadas_e_enigmas():
    piadas_enigmas = [
        "Por que o computador foi ao médico? Porque estava com vírus!",
        "Qual é o país que tem mais carneiros que pessoas? O país de Gales!",
        "Qual é o número que é igual à metade de sua soma mais um? O número 2!",
        "O que é, o que é: quanto mais se tira, maior fica? O buraco!",
        "Por que o jacaré não usa a internet? Porque ele já tem o navegador!",
        "Qual é o lugar onde o tênis é sempre vencedor? Na sola do pé!",
        "O que é, o que é: fica no canto e viaja o mundo? O selo postal!",
        "Por que a bicicleta caiu? Porque estava sem pedal!",
        "Qual é o animal que come com a cauda? O macaco, porque a cauda é uma extensão do corpo!",
        "O que é, o que é: tem muitas agulhas, mas não costura? O pinheiro!",
        "Por que o pimentão sempre perde na corrida? Porque ele é sempre o último a sair do pote!",
        "Qual é o mês mais curto? Fevereiro, porque tem apenas 28 dias!",
    ]
    escolha = random.choice(piadas_enigmas)
    print(escolha)
    voz.say(escolha)
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

def falar_adeus():
    texto = f'Adeus mestre {nome}'
    print(texto)
    voz.say(texto)
    voz.runAndWait()


with sr.Microphone() as mic:

    reconhecimento.adjust_for_ambient_noise(mic, duration=3)
    print("Diga ok sexta-feira para iniciar a aplicacção")
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
                reconhecimento.adjust_for_ambient_noise(mic, duration=3)
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
                    elif 'COMO ESTÁ O CLIMA' in frase:
                        falar_clima()
                    elif 'FALE SOBRE PYTHON' in frase:
                        falar_python()
                    elif 'FALE SOBRE A FIAP' in frase:
                        falar_fiap()
                    elif 'FALE UMA RECEITA DE BOLO' in frase:
                        falar_receita_bolo()
                    elif 'EXPLIQUE O VERBO TO BE' in frase:
                        falar_to_be()
                    elif 'COMO TIRAR CNH' in frase:
                        falar_cnh()
                    elif 'FALE UM FATO CURIOSO' in frase:
                        falar_fato()
                    elif 'FALE UMA PIADA OU ENIGMA' in frase:
                        piadas_e_enigmas()
                    elif 'ESTOU COM UMA EMERGÊNCIA' in frase:
                        falar_emergencia()
                    elif 'ENCERRAR' or 'SAIR' in frase:
                        falar_adeus()
                        break
                except sr.UnknownValueError:
                    print("Não entendi o que você falou.")
                    voz.say("Não entendi o que você falou")
                except sr.RequestError as e:
                    print(f"Não foi possível realizar a operação. Erro: {e}")
    except sr.UnknownValueError:
        print("Não entendi o que você falou.")
        voz.say("Não entendi o que você falou")
    except sr.RequestError as e:
        print(f"Não foi possível realizar a operação. Erro: {e}")