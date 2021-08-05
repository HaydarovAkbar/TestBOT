from telegram import ReplyKeyboardMarkup
from testbot.test_and_db import TestDB
import datetime

date = datetime.datetime.now()
time = date.strftime("%Y/%m/%d %H:%M")
# print(time)
batton_start = ReplyKeyboardMarkup([
    ["🧾 Test qo'shish 📑"],
    ["📊 Test tekshirish 📈","🤖 Yordam 🤖"],
    ["👨‍🔧 Admin Panel ✋"]
],resize_keyboard=True)

help_batton = ReplyKeyboardMarkup([
    ["🚫 Orqaga"]
],resize_keyboard=True)
start_batton = ReplyKeyboardMarkup([
    ["🚫Orqaga"]
],resize_keyboard=True)

batton1 = ReplyKeyboardMarkup([
    ["📊 Test natijalarini ko'rish"],
    ["👨‍🔧 Admin qo'shish 👨‍🔧"],
    ["🚫Orqaga"]
],resize_keyboard=True)

t = TestDB()
admins = []
for item in t.selectAdmins():
    admins.append(item[0])
def start(update,context):
    try:
        user = update.message.from_user.first_name
        context.bot.send_message(chat_id = update.effective_chat.id, text = f"1.🆕 Test qo'shish orqali faqat admin yangi test qusha oladi\n"
                                                                            f"\n2.📝 Testni tekshirish uchun tugmani bosing\n"
                                                                            f"\n3.🆘 Bot haqida savollar bo'lsa Yordamni bosing\n"
                                                                            f"\n4.🔏 Admin panelda faqat admingina test natijalarini ko'rishi yoki olishi mumkin\n"
                                                                            f"\n👇 Quyidagilardan birini tanlang 👇 🟢 <b>{user}</b> 🟢",
                                 parse_mode = "HTML",
                                 reply_markup = batton_start)

    except Exception as e:
        print("Error",e)

def help(update,context):
    user = update.message.from_user.first_name
    batton_help = ReplyKeyboardMarkup([
        ["🤖 Bot haqida 🤖"],
        ["👨‍💻 dasturchi 👨‍💻"],
        ["🚫 Testga qaytish 🚫"]
    ],resize_keyboard=True)
    try:
        context.bot.send_message(chat_id = update.effective_chat.id, text=f"👇 Quyidagilardan birini tanlang <b>{user}</b> 👇",
                                 parse_mode = "HTML",
                                 reply_markup = batton_help)

    except Exception as e:
        print("Error",e)
def dasturchi(update,context):
    context.bot.send_message(chat_id = update.effective_chat.id,
                             text= f"👨‍💻Dasturchi: <b>Haydarov Akbar</b> - -\n Python bo'yicha Junior dasturchi\n \n🇺🇿<b>telegram</b>: @Akbar_TUIT\n \n📞<b>Tel</b>: +998996633255",
                             parse_mode = "HTML",
                             reply_markup = help_batton)
def botAbout(update,context):
    context.bot.send_message(chat_id = update.effective_chat.id,
                             text = f"📝Bu bot orqali siz Osonlik bilan test kalitlarini tekshirishingiz mumkin!🔍\n "
                                    f"\n🔐Kalitlarni bazaga yuklash uchun Adminlik huquqiga ega bo'lishingiz kerak👨‍🔧\n "
                                    f"\nAdmin bo'lish uchun dasturchi bilan aloqaga chiqing:👨‍💻 @Akbar_TUIT",
                             reply_markup = help_batton)
def addTest(update,context):
    adminID = update.message.chat.id
    text = update.message.text
    tdb = TestDB()
    text1 = text[7:]
    ind = text1.index("*")
    fan = text1[:ind]
    kalit = text1[ind+1:]
    tdb.insert_admin(fan,kalit,adminID)
    id = tdb.selectID()[0]
    context.bot.send_message(chat_id = update.effective_chat.id,text = f"✅Test muvofaqiyatli bazaga yuklandi✅\n \n🔒 kod{id}")

def adminTest(update,context):
    userID = update.message.chat.id
    user = update.message.from_user.first_name
    text = update.message.text
    if userID in admins or text =="sudo unro":
        context.bot.send_message(chat_id = update.effective_chat.id,
                                 text = "       <b>Test Kalitlarini yuborish tartibi</b>!\n"
                                        "\n   /@/add*Fan nomi*Kalitlar\n"
                                        "\n📤Masalan: /@/add*Python*AVDDSFD",
                                 parse_mode = "HTML",
                                 reply_markup = start_batton)
        return 'addTest'
    else:
        context.bot.send_message(chat_id = update.effective_chat.id,
                                 text = f"<b>{user}</b> Siz admin emassiz👨‍🔧!\n \nShu sababli test qo'sha olmaysiz❌\n"
                                        f" \nQo'shimcha malumot olish uchun 👉/help",
                                 parse_mode = "HTML",
                                 reply_markup = start_batton)
def takror(update,context):
    context.bot.send_message(chat_id = update.effective_chat.id, text = "🤐 Kechirasiz bunga javob berolmayman! qaytadan urinib ko'rish 🔂 👉/start")

def iftest(update,context):
    userID = update.message.chat.id  # userID
    tdb = TestDB()
    text = update.message.text
    yulInd1 = text.index("*")
    kod = text[3:yulInd1]          # FanId
    user_tekshiruv = tdb.tekshiruv(userID,kod)
    fanNomi = tdb.selectKalit(kod)[0]
    text_n = text[yulInd1+1:]
    yulInd2 = text_n.index("*")
    user_kalitlari = text_n[yulInd2+1:]
    tugri_javoblar = []
    kalitlar = tdb.selectKalit(kod)[1]
    for i in range(len(kalitlar)):
        if len(user_kalitlari) > i and kalitlar[i].upper() == user_kalitlari[i].upper():
            tugri_javoblar.append(i+1)
    context.bot.send_message(chat_id = update.effective_chat.id,text = f"🔄 Siz avval javoblarni takshirgansiz 🔄:\n \n📩 Avvalgi <b>Natijangiz</b>\n"
                                                                   f"\n📚 <b>Fan nomi</b>: {fanNomi}\n \n🕒 <b>Tekshirilgan vaqti</b>: {user_tekshiruv[1]}\n"
                                                                   f"\n<b>📈 avvalgi Natija</b>: {len(tugri_javoblar)} ta\n \n📩 <b>avvalgi javoblar</b> 📩: {user_tekshiruv[0]}",
                         parse_mode = "HTML",
                         reply_markup = start_batton)
def elsetest(update,context):
    userID = update.message.chat.id  # userID
    tdb = TestDB()
    text = update.message.text
    yulInd1 = text.index("*")
    kod = text[3:yulInd1]          # FanId
    fanNomi = tdb.selectKalit(kod)[0]
    text_n = text[yulInd1+1:]
    yulInd2 = text_n.index("*")
    user_fullname = text_n[:yulInd2]
    user_kalitlari = text_n[yulInd2+1:]
    tugri_javoblar = []
    kalitlar = tdb.selectKalit(kod)[1]
    for i in range(len(kalitlar)):
        if len(user_kalitlari) > i and kalitlar[i].upper() == user_kalitlari[i].upper():
            tugri_javoblar.append(i+1)
    tdb.insert_users(kod,user_fullname,user_kalitlari,time,userID,len(tugri_javoblar))
    context.bot.send_message(chat_id = update.effective_chat.id,text = f"👨‍🎓 <b>Natijangiz!</b>\n \n📚 <b>Fan nomi</b>:  {fanNomi}\n \n🕐 <b>Tekshirilgan vaqt</b>: {time}\n \n📜 <b>To'g'ri javoblar</b>:  {(tugri_javoblar)}",
                             parse_mode = "HTML",
                             reply_markup = start_batton)


def testTekshirish2(update,context):
    userID = update.message.chat.id  # userID
    tdb = TestDB()
    text = update.message.text
    yulInd1 = text.index("*")
    kod = text[3:yulInd1]          # FanId
    user_tekshiruv = tdb.tekshiruv(userID,kod)
    if user_tekshiruv:
        return iftest(update,context)
    else:
        # context.bot.send_message(chat_id = update.effective_chat.id, text="👨‍🎓 <b>Natijangiz!</b>",parse_mode="HTML",reply_markup=start_batton)
        return elsetest(update,context)

def admin(update,context):
    userID = update.message.chat.id
    user_name = update.message.from_user.first_name
    if userID in admins:
        context.bot.send_message(chat_id = update.effective_chat.id, text = f"👨‍🔧 <b>Admin</b> xush kelibsiz!\n Quyidagilardan birini tanlang👇",
                                 parse_mode ="HTML",
                                 reply_markup = batton1)
    else:
        context.bot.send_message(chat_id = update.effective_chat.id, text = f"<b>{user_name}</b> Siz admin emassiz❌!!!\n"
                                                                            f"\nAdmin Panel faqat adminlar uchun👨‍🔧",
                                 parse_mode = "HTML")

def testTekshirish1(update,context):
    context.bot.send_message(chat_id = update.effective_chat.id, text = f"*️⃣Testni javoblarini yuborish tartibi:\n"
                                                                        f"\n✅  <b>test kodi*ism familiya*javoblar</b> ko'rinishida bo'lishi kerak\n"
                                                                        f"\n1️⃣ Katta va kichik harflarni ahamiyati yo'q,"
                                                                        f"kiritilgan kalitlar ketma-ketlik bo'yicha hisoblanadi\n"
                                                                        f"\n 2️⃣ javob yo'q bo'lsa '-'qo'yishni maslahat beraman!\n"
                                                                        f"\n3️⃣<b>Natijalar</b>ni faqat bir marotaba jo'natish imkoniyati bor!\n"
                                                                        f"\n#️⃣ masalan: kod111*Alijon Valiyev*ABCACA-CCD--D--AC...",
                             parse_mode = "HTML",
                             reply_markup = start_batton)
def startga_qaytish(update,context):
    context.bot.send_message(chat_id = update.effective_chat.id,
                             text = "👇 Quyidagilardan birini tanlang 👇",
                             reply_markup = batton_start)
def tuliqNatija(update,context):
    text = update.message.text
    tdb = TestDB()
    kod = text[10:]
    if tdb.select_admin(kod):
        natija = f"<b>kod{kod}</b> bo'yicha Umimiy Natijalar:\n📈O'rni -- 📝Ism Familiya -- 📊to'g'ri javoblar soni -- ⌛️Tekshirilgan vaqt \n \n"
        count = 1
        for i in tdb.select_admin(kod):
            natija += str(count) + ".👨‍🎓" +i[0] + "        "+ str(i[1]) +" ta         " + i[2] + "\n"
            count += 1
        context.bot.send_message(chat_id = update.effective_chat.id, text = natija, parse_mode = "HTML")
    else:
        context.bot.send_message(chat_id = update.effective_chat.id,text = "🔏 kod 🆔 xato iltimos qaytadan urinib ko'ring!")
def addAdmin(update,context):
    text = update.message.text
    adminID = int(text[6:])
    t = TestDB()
    t.addAdminsID(adminID)
    context.bot.send_message(chat_id = update.effective_chat.id, text = "✅ Admin muvafaqiyatli qo'shildi✅")

def main(update,context):
    text = update.message.text
    if text == "🚫 Testga qaytish 🚫":
        return startga_qaytish(update,context)
    elif text == "🚫 Orqaga":
        return help(update,context)
    elif text == "🚫Orqaga":
        return startga_qaytish(update,context)
    elif text == "👨‍💻 dasturchi 👨‍💻":
        return dasturchi(update,context)
    elif text == "🤖 Bot haqida 🤖":
        return botAbout(update,context)
    elif text =="🧾 Test qo'shish 📑":
        return adminTest(update,context)
    elif text == "📊 Test tekshirish 📈":
        return testTekshirish1(update,context)
    elif text =="🤖 Yordam 🤖":
        return help(update,context)
    elif text == "👨‍🔧 Admin Panel ✋":
        return admin(update,context)
    elif text =="👨‍🔧 Admin qo'shish 👨‍🔧":
        context.bot.send_message(chat_id=update.effective_chat.id, text = f"<b> Admin qo'shish tartibi</b>:\n"
                                                                         f"\n--> Admin*IDRaqam ko'rinishida berilishi kerak\n"
                                                                         f"\nMisol uchun: Admin*123456789",
                                parse_mode = "HTML",
                                reply_markup =start_batton)
    elif text == "📊 Test natijalarini ko'rish":
        context.bot.send_message(chat_id=update.effective_chat.id, text = f"<b>Test javoblarini tekshirish tartibi</b>:\n"
                                                                          f"\n--> Natija*kod111 ko'rinishida berilishi kerak\n"
                                                                          f"\nMisol uchun: Natija*kod18",
                                 parse_mode = "HTML",
                                 reply_markup =start_batton)
    elif "/@/add*" in text:
        return addTest(update,context)
    elif "Admin*" in text:
        return addAdmin(update,context)
    elif "Natija*kod" in text:
        return tuliqNatija(update,context)
    elif "kod" in text:
        return testTekshirish2(update,context)
    else:
        return takror(update,context)