bitcoin_adress = None
   
def sef_bitcoin_adress():
    global bitcoin_adress
    bitcoin_adress = input("Gebe deine Bitcoin Adresse ein!")
    print("Deine Bitcoin Adresse wurde gespeichert!")    

def display_bitcoin_adress():
    if bitcoin_adress:
        print("Deine Bitcoin Adresse ist")
        print(bitcoin_adress)
    else:
        print("Du hast keine Bitcoin Adresse angegeben!")

while True:
    command = input("Gib 'anzeigen' ein um deine Bitcoin Adresse anzuzeigen oder einstellen um eine neue Bitcoin Adresse einzugeben die dir dann angezeigt wird")

    if command.lower() == 'anzeigen':
        display_bitcoin_adress()
    elif command.lower() == 'einstellen':
        sef_bitcoin_adress()
    else:("Sie haben etwas eingegeben wo ihnen das hier angezeigt wird.")