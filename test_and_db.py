import sqlite3

class TestDB:
    def insert_admin(self,nomi,kalit,adminID):        #test kiritish funksiyasi
        try:
            connation = sqlite3.connect('test_db.db')
            cursor = connation.cursor()
            cursor.execute(f"INSERT INTO admin(fan_nomi,kalitlar,adminID) VALUES('{nomi}','{kalit}',{adminID})")
            connation.commit()
            connation.close()

        except Exception as e:
            print("Error",e)

    def selectID(self):       # Admin test kiritganda testni ID sini qaytaradigan funksiya
        try:
            connation = sqlite3.connect('test_db.db')
            cursor = connation.cursor()
            cursor.execute("SELECT test_id FROM admin ORDER BY test_id DESC LIMIT 1")
            return cursor.fetchone()

        except Exception as e:
            print("Error",e)
    def selectKalit(self,fanID):                 # Kalitlar olish uchun funksiya
        try:
            conn = sqlite3.connect("test_db.db")
            cursor = conn.cursor()
            cursor.execute(f"SELECT fan_nomi,kalitlar FROM admin WHERE test_id = {fanID}")
            return cursor.fetchone()
        except Exception as e:
            print("ERror",e)

    def insert_users(self,id,name,test,date,userID,soni):      # testni tekshirgach natijalarni bazaga yozadigan funkiya
        try:
            connation = sqlite3.connect("test_db.db")
            cursor = connation.cursor()
            cursor.execute(f"INSERT INTO users(fullname,natija,fanID,date,userID,tugrijavob) VALUES('{name}','{test}',{id},'{date}',{userID},{soni})")
            connation.commit()
            connation.close()

        except Exception as e:
            print("Error",e)

    def select_admin(self,id):    # Admin fanId si bo'yicha umumiy natijalarni chiqarishi mumkin
        try:
            conn = sqlite3.connect("test_db.db")
            cursor = conn.cursor()
            cursor.execute(f"SELECT fullname,tugrijavob,date FROM users "
                           f"WHERE fanID = {id} "
                           f"ORDER BY tugrijavob DESC")
            return cursor.fetchall()

        except Exception as e:
            print("Error",e)

    def tekshiruv(self,userID,kod):   # Agar foydalanuvchi bazada bulsa nechta ishlaganini aks holda None qaytaradi
        try:
            conn = sqlite3.connect("test_db.db")
            cursor = conn.cursor()
            cursor.execute(f"SELECT natija,date FROM users WHERE (fanID = {kod} AND userID = {userID})")
            return cursor.fetchone()

        except Exception as e:
            print("Xato bor",e)
    def selectAdmins(self):         # adminarni Id sini qaytaradi
        try:
            conn = sqlite3.connect("test_db.db")
            cursor = conn.cursor()
            cursor.execute(f"SELECT AdminID FROM admins")
            return cursor.fetchall()

        except Exception as e:
            print("Xato bor",e)
    def adminTest(self,ID):               # Adminni barcha kiritgan testlarini chiqaradigan funksiya
        try:
            conn = sqlite3.connect("test_db.db")
            cursor = conn.cursor()
            cursor.execute(f"SELECT * FROM admin WHERE adminID = {ID}")
            return cursor.fetchall()

        except Exception as e:
            print("Xato bor",e)
    def addAdminsID(self,ID):
        try:
            conn = sqlite3.connect("test_db.db")
            cursor =conn.cursor()
            cursor.execute(f"INSERT INTO admins(AdminID) VALUES({ID})")
            conn.commit()
            conn.close()
        except Exception as e:
            print("Error",e)
if __name__ == '__main__':
    t = TestDB()
    # t.insert_users(3,'Akbar',12,"12:00",123123)
    t.insert_admin("mat", "Ab",123)
    print(t.selectKalit(13))
    # print(t.selectID())
    # print(t.select_admin(12))
    # print(t.tekshiruv(1231231,3))