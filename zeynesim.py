import requests
import console

console.set_color(0.0, 0.6, 1.0)
print("""
  ______                
 |___  /                
    / / ___ _   _ _ __  
   / / / _ \ | | | '_ \ 
  / /_|  __/ |_| | | | |
 /_____\___|\__, |_| |_|
             __/ |      
            |___/       """)
print("")
console.set_color(1.0, 0.5, 0.0)
print("                        𝓜𝓐𝓜𝓔𝓓")
console.set_color(1.0, 0.0, 1.0)
print("    Kodlarım yalan danışmaz")
console.set_color(0.6, 0.0, 0.8)
print("       ama insan danışar..")
print("")
print("")
console.set_color()

console.set_color(0.6, 0.0, 0.8)
print("TG: @zeynmamed")
print("")
console.set_color()

console.set_color(0.0, 0.6, 1.0)
eposta = input("[@]Gmail Yaz: ")
console.set_color()

# -------------------- Kod GÖnderme --------------------#
url1 = "https://iweb.yesim.app//v1/auth_email?email=" + eposta + "&version=4.0.8&lang=en&platform=3"
headers1 = {
    'Host': 'iweb.yesim.app'
}
res1 = requests.post(url1, headers=headers1)
sonuc1 = res1.json()

# ------------------- Kod Onaylama session id çekme ---------------#
console.set_color(0.0, 0.6, 1.0)
kod = input("[</>]Kodu Yaz: ")
console.set_color()
url2 = "https://iweb.yesim.app/v1/auth_code?code="+kod+"&email="+eposta+"&version=4.1.8&lang=en&platform=3"
headers2 = {
    'Host': 'iweb.yesim.app'
}
res2 = requests.post(url2, headers=headers2)
sonuc2 = res2.json()["sessionId"]

# ------------- Y Coin Çekme -----------#
url3 = "https://api2.yesim.app/code_apply?ref_code&web_key="+sonuc2+"&ref_code=NQVO420&lang=en"
headers3 = {
    'Host': 'iweb.yesim.app'
}

try:
	res3 = requests.get(url3, headers=headers3, verify=False)
	sonuc3 = res3.json() == ['success']
	console.set_color(0.0, 1.0, 0.0)
	print("[+]500MB Əlavə olundu/Added")
except:
	print("Bir problem var Adminə yaz @zeynmamed")
	raise SystemExit()

try:
	dark = requests.get("https://iweb.yesim.app/v1/activate_pay_as_you_go?web_key="+sonuc2+"&lang=en", timeout=5)
	sonuc4 = dark.json() == "Ok"
	console.set_color(0.0, 1.0, 0.0)
	print("[+]Esimi Alırıq ")
except:
	console.set_color(1.0, 0.0, 0.0)
	print("[-]Esimi Ala Bilmədik")
	print("Bir problem var Adminə yaz @zeynmamed")
	raise SystemExit()

try:
    dark1 = requests.get("https://iweb.yesim.app/v1/show_my_qrs?web_key=" + sonuc2 + "&lang=en", timeout=5)
    sonuc5 = dark1.json()["Qrs"]
    console.set_color(0.0, 1.0, 0.0)
    print("[+]Esim Gmailə Göndərildi :)")
except:
    console.set_color(1.0, 0.0, 0.0)
    print("[-]Esimi Ala Bilmedik ):")
    print("Bir problem var Adminə yaz @zeynmamed")
    raise SystemExit()
