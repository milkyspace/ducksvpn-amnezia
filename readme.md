# DUCKS VPN
## _The Best Telegram Vpn Service, Ever_

[![Telegram](https://img.shields.io/badge/Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white)](https://t.me/vladimir_kvms)

DucksVPN is a telegram bot with AmneziaVPN server for sales vpn subscribes.

- 🌍 VPN works only for YouTube, Instagram and Twitter (we will add the necessary services upon your request)
- 🔥 Now you don't need to disable VPN, all Russian services will work even with VPN enabled
- 🚀 Unlimited speed, no ads, can be installed on a smart TV or router
- ⚡️ 24/7 operational support will answer your questions and help you connect

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

DUCKS VPN requires Docker and Python3 to run.
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

Now you can open admin panel http://{$IP}:51821/
And start the telegram bot
```sh
sudo systemctl start ducksVpnTelegram
sudo systemctl status ducksVpnTelegram
```


## License

MIT

**Free Software**
