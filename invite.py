:
    print(f"""
░▄▀▀░▀█▀░▄▀▄░▀▄▀▒▄▀▄░█▄▀░░░█▄▒▄█▒▄▀▄░█▄▀░▄▀▀▒▄▀▄
▒▄██░▒█▒░▀▄▀░▒█▒░█▀█░█▒█▒░░█▒▀▒█░█▀█░█▒█▒▄██░█▀█


by @NAKATIKA_NAEBUKA
        """)
        

cpass = configparser.RawConfigParser()
cpass.read('config.data')

try:
    api_id = cpass['cred']['id']
    api_hash = cpass['cred']['hash']
    phone = cpass['cred']['phone']
    client = TelegramClient(phone, api_id, api_hash)
except KeyError:
    os.system('clear')
    banner()
    print(re+"[!] run python3 setup.py first !!\n")
    sys.exit(1)

client.connect()
if not client.is_user_authorized():
    client.send_code_request(phone)
    os.system('clear')
    banner()
    client.sign_in(phone, input(gr+'[+] Хуйника код: '+re))
 
os.system('clear')
banner()
input_file = sys.argv[1]
users = []
with open(input_file, encoding='UTF-8') as f:
    rows = csv.reader(f,delimiter=",",lineterminator="\n")
    next(rows, None)
    for row in rows:
        user = {}
        user['username'] = row[0]
        user['id'] = int(row[1])
        user['access_hash'] = int(row[2])
        user['name'] = row[3]
        users.append(user)
 
chats = []
last_date = None
chunk_size = 200
groups=[]
 
result = client(GetDialogsRequest(
             offset_date=last_date,
             offset_id=0,
             offset_peer=InputPeerEmpty(),
             limit=chunk_size,
             hash = 0
         ))
chats.extend(result.chats)
 
for chat in chats:
    try:
        if chat.megagroup== True:
            groups.append(chat)
    except:
        continue
 
i=0
for group in groups:
    print(gr+'['+cy+str(i)+gr+']'+cy+' - '+group.title)
    i+=1

print(gr+'[+] Выберите группу для добавления Петухов')
g_index = input(gr+"[+] Введите номер : "+re)
target_group=groups[int(g_index)]
 
target_group_entity = InputPeerChannel(target_group.id,target_group.access_hash)
 
print(gr+"[1] Подтянуть Петуха за залупу (по ID)\n[2] Подтянуть Петуха за волосы (по имени).")
mode = int(input(gr+"Input : "+re)) 
n = 0
print(users)
print('before for') 
for user in users:
    n += 1
    if 1 == 1:
	    time.sleep(1)
	    try:
	        print ("Adding {}".format(user['id']))
	        if mode == 1:
	            if user['username'] == "":
	                continue
	            user_to_add = client.get_input_entity(user['username'])
	        elif mode == 2:
	            user_to_add = InputPeerUser(user['id'], user['access_hash'])
	        else:
	            sys.exit(re+"[!] Выбран хуйпонятный режим. пожалуйста, попробуйте снова.")
	        client(InviteToChannelRequest(target_group_entity,[user_to_add]))
	        print(gr+"[+] Не выебывайся где-то 10-30 секунд...")
	        time.sleep(random.randrange(10, 30))
	    except PeerFloodError:
	        print(re+"[!] Получаю Пиздюлей от telegram. \n[!] Сценарий сейчас останавливается. \n[!] Пожалуйста, повторите попытку через некоторое время.")
	    except UserPrivacyRestrictedError:
	        print(re+"[!] Настройки конфиденциальности Петуха не позволяют вам этого делать. Ложим хуй.")
	    except:
	        traceback.print_exc()
	        print(re+"[!] Непредвиденная ошибка")
	        continue
