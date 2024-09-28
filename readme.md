# 🦆 DUCKS VPN
## _The Best Telegram Vpn Service, Ever_

[![Telegram](https://img.shields.io/badge/Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white)](https://t.me/vpnducks_support)

DucksVPN is a telegram bot with AmneziaVPN server for sales vpn subscribes.

- 🌍 VPN works only for YouTube, Instagram and Twitter as default
- 🔥 Now you don't need to disable VPN, all another services will work even with VPN enabled
- 🚀 Unlimited speed, no ads, can be installed on a smart TV or router
- ⚡️ Operational support fron telegram bot will answer your questions and help you connect

## Tech

DucksVPN uses technical solutions:
- NodeJS
- VueJs
- Python
- AmneziaVPN
- WireGuardVPN
- Docker

And of course DUCKS VPN itself is open source with a [public repository][dill] on GitHub.

## Installation

DUCKS VPN requires Docker and Python3 to run.\
You must create a bot in telegram via https://t.me/BotFather and create a store in YooKassa https://yookassa.ru/ to receive subscription payments

Install the dependencies and start the server.
You need to find out your ip address ($IP):
```sh
ip addr show
```

```sh
apt install sudo -y
apt-get install git -y
git clone https://github.com/milkyspace/ducksvpn.git
cd ducksvpn
chmod u+x install.sh
./install.sh "{$IP}" "{$PASSWORD_TO_ADMIN_PANEL}"
```

Change it .env: Enter your data using the example
```sh
mv .env.example .env
nano .env # or vim .env
```

**ADMIN_TG_ID_1** is tg id of first admin (go to @getmyid_bot)\
**ADMIN_TG_ID_2** is tg id of second admin  (go to @getmyid_bot)\
**ONE_MONTH_COST** is the price for 1 month\
**TRIAL_PERIOD** is days of trial period\
**COUNT_FREE_FROM_REFERRER** is count of months for referrer present\
**PERC_1** is calc price for 1 month\
**PERC_3** is calc price for 3 months\
**PERC_6** is calc price for 6 months\
**PERC_12** is calc price for 12 months\
**TG_TOKEN** is telegram bot token\
**TG_SHOP_TOKEN** is yookassa token\
**BASE_URL** is url for wg api (default http://0.0.0.0:51821/api)\
**PASSWORD_TO_AMNEZIA** is password to admin panel\
**BOT_NAME** is name of telegram bot

Now you can open admin panel http://{$IP}:51821/
And start the telegram bot

```sh
sudo systemctl start ducksVpnTelegram
sudo systemctl status ducksVpnTelegram
```


## License

MIT

**Free Software**
