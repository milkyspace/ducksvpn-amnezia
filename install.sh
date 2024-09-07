function installAmnezia() {
  curl -sSL https://get.docker.com | sh
  sudo usermod -aG docker $(whoami)
  docker pull vkolesnev/amneziavpn:latest
  docker run -d \
    --name=amnezia-wg-easy \
    -e LANG=en \
    -e WG_HOST=$1 \
    -e PASSWORD=$2 \
    -v ~/.amnezia-wg-easy:/etc/wireguard \
    -p 51820:51820/udp \
    -p 51821:51821/tcp \
    --cap-add=NET_ADMIN \
    --cap-add=SYS_MODULE \
    --sysctl="net.ipv4.conf.all.src_valid_mark=1" \
    --sysctl="net.ipv4.ip_forward=1" \
    --device=/dev/net/tun:/dev/net/tun \
    --restart unless-stopped \
    vkolesnev/amneziavpn:latest

  clear
  echo "Installed Amnezia"
  echo "Admin panel of Amnezia on http://$1:51821/"
}

function installTg() {
  apt-get install unzip
  apt-get install python3
  apt-get install python3-pip -y
  pip install -r "$(pwd)/requirements.txt"
  echo "[Unit]
        Description=Admin Bot for Wireguard
        After=multi-user.target

        [Service]
        Type=simple
        Restart=always
        RestartSec=15
        WorkingDirectory=$(pwd)
        ExecStart=/usr/bin/python3 $(pwd)/main.py
        User=root

        [Install]
        WantedBy=multi-user.target">"/etc/systemd/system/ducksVpnTelegram.service"
  systemctl daemon-reload
  sudo systemctl enable ducksVpnTelegram.service
  mkdir data
  clear
  rm ./install.sh
  rm ./requirements.txt
  echo "Installed TG"
  echo "Congratulations! Now you must configure the .env (copy .env.example to .env) configuration file at .env"
}

installAmnezia
installTg
