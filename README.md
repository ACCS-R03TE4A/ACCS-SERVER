# ACCS
## インストール
- プロキシを使用する場合
  - echo 'export HTTP_PROXY=http://172.17.0.2:80' >> ~/.bashrc # ユーザーごとに
  - echo 'export HTTPS_PROXY=http://172.17.0.2:80' >> ~/.bashrc # ユーザーごとに
  - source ~/.bashrc # ユーザーごとに
  - echo 'Acquire::http::Proxy "http://172.17.0.2:80";' >> /etc/apt/apt.conf # 要root
  - echo 'Acquire::https::Proxy "http://172.17.0.2:80";' >> /etc/apt/apt.conf # 要root
  - echo 'http_proxy=http://172.17.0.2:80/' >> /etc/wgetrc # 要root
  - echo 'https_proxy=http://172.17.0.2:80/' >> /etc/wgetrc # 要root
  - echo 'ftp_proxy=http://172.17.0.2:80/' >> /etc/wgetrc # 要root
1. git clone https://github.com/ACCS-R03TE4A/ACCS-SERVER.git # 一般ユーザで
2. cd ACCS-SERVER
3. chmod +x ./scripts/*
4. ./scripts/deploywithroot.sh # 要root
5. ./scripts/deploy.sh

## サーバ起動
1. source env/bin/activate
2. export FLASK_APP=flaskr
3. export FLASK_ENV=development
4. flask run -h 0.0.0.0
