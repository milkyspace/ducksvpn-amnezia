import aiosqlite
import sqlite3
import time
import subprocess
import requests
import json
import logging
import os
from dotenv import load_dotenv, dotenv_values

load_dotenv()

CONFIG = {
    "admin_tg_id": [int(os.getenv("ADMIN_TG_ID_1")), int(os.getenv("ADMIN_TG_ID_2"))],
    "one_month_cost": float(os.getenv("ONE_MONTH_COST")),
    "trial_period": os.getenv("TRIAL_PERIOD"),
    "perc_1": float(os.getenv("PERC_1")),
    "perc_3": float(os.getenv("PERC_3")),
    "perc_6": float(os.getenv("PERC_6")),
    "UTC_time": int(os.getenv("UTC_TIME")),
    "tg_token": os.getenv("TG_TOKEN"),
    "tg_shop_token": os.getenv("TG_SHOP_TOKEN"),
    "base_url": os.getenv("BASE_URL"),
    "password_to_amnezia": os.getenv("PASSWORD_TO_AMNEZIA"),
}

BASE_URL = CONFIG["base_url"]
PASSWORD = CONFIG["password_to_amnezia"]

DBCONNECT="data.sqlite"

class User:
    def __init__(self):
        self.id = None
        self.tgid = None
        self.subscription = None
        self.trial_subscription = True
        self.registered = False
        self.username = None
        self.fullname = None

    @classmethod
    async def GetInfo(cls, tgid):
        self = User()
        self.tgid = tgid
        db = await aiosqlite.connect(DBCONNECT)
        db.row_factory = sqlite3.Row
        c = await db.execute(f"SELECT * FROM userss where tgid=?",(tgid,))
        log = await c.fetchone()
        await c.close()
        await db.close()
        if not log is None:
            self.id = log["id"]
            self.subscription = log["subscription"]
            self.trial_subscription = log["banned"]
            self.registered = True
            self.username = log["username"]
            self.fullname = log["fullname"]
            self.referrer_id = log["referrer_id"]
        else:
            self.registered = False

        return self

    async def PaymentInfo(self):
        db = await aiosqlite.connect(DBCONNECT)
        db.row_factory = sqlite3.Row
        c = await db.execute(f"SELECT * FROM payments where tgid=?", (self.tgid,))
        log = await c.fetchone()
        await c.close()
        await db.close()
        return log

    async def CancelPayment(self):
        db = await aiosqlite.connect(DBCONNECT)
        await db.execute(f"DELETE FROM payments where tgid=?",
                         (self.tgid,))
        await db.commit()

    async def NewPay(self,bill_id,summ,time_to_add,mesid):
        pay_info = await self.PaymentInfo()
        if pay_info is None:
            db = await aiosqlite.connect(DBCONNECT)
            await db.execute(f"INSERT INTO payments (tgid,bill_id,amount,time_to_add,mesid) values (?,?,?,?,?)",
                             (self.tgid, str(bill_id),summ,int(time_to_add),str(mesid)))
            await db.commit()

    async def GetAllPaymentsInWork(self):
        db = await aiosqlite.connect(DBCONNECT)
        db.row_factory = sqlite3.Row
        c = await db.execute(f"SELECT * FROM payments")
        log = await c.fetchall()
        await c.close()
        await db.close()
        return log

    async def Adduser(self, username, full_name, referrer_id):
        if self.registered == False:
            response = requests.post(f"{BASE_URL}/wireguard/client", data=json.dumps({"name": str(self.tgid)}), headers={"Content-Type": "application/json", "password": f"{PASSWORD}"})
            if response.status_code == 200:
                clients = requests.get(f"{BASE_URL}/wireguard/client", headers={"password": f"{PASSWORD}"})
                for client in clients.json():
                    if str(self.tgid) == client.get('name', 0):
                        db = await aiosqlite.connect(DBCONNECT)
                        await db.execute(f"INSERT INTO userss (tgid,subscription,username,fullname,wg_key,referrer_id) values (?,?,?,?,?,?)", (self.tgid,str(int(time.time())+int(CONFIG['trial_period']) * 86400),str(username),str(full_name),client.get('id', 0),referrer_id))
                        await db.commit()
            self.registered = True

    async def GetAllUsers(self):
        db = await aiosqlite.connect(DBCONNECT)
        db.row_factory = sqlite3.Row
        c = await db.execute(f"SELECT * FROM userss")
        log = await c.fetchall()
        await c.close()
        await db.close()
        return log

    async def GetAllUsersWithSub(self):
        db = await aiosqlite.connect(DBCONNECT)
        db.row_factory = sqlite3.Row
        c = await db.execute(f"SELECT * FROM userss where subscription > ?",(str(int(time.time())),))
        log = await c.fetchall()
        await c.close()
        await db.close()
        return log

    async def GetAllUsersWithoutSub(self):
        db = await aiosqlite.connect(DBCONNECT)
        db.row_factory = sqlite3.Row
        c = await db.execute(f"SELECT * FROM userss where banned = true")
        log = await c.fetchall()
        await c.close()
        await db.close()
        return log

    async def CheckNewNickname(self,message):
        try:
            username = "@" + str(message.from_user.username)
        except:
            username = str(message.from_user.id)

        if message.from_user.full_name!=self.fullname or username!=self.username:
            db = await aiosqlite.connect(DBCONNECT)
            db.row_factory = sqlite3.Row
            await db.execute(f"Update userss set username = ?, fullname = ? where id = ?", (username,message.from_user.full_name,self.id))
            await db.commit()

    async def countReferrerByUser(self):
        db = await aiosqlite.connect(DBCONNECT)
        c = await db.execute(f"select count(*) as count from userss where referrer_id=?",
                         (self.tgid,))
        log = await c.fetchone()
        await db.commit()
        return 0 if log[0] is None else log[0]