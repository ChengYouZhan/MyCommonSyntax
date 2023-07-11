## 建立python虛擬環境


### 建立專屬虛擬環境，linux指定service需要指定虛擬路徑。
```sh
python3 -m venv ftp-env
source py-ftp-env/bin/activate
```
### 安裝pyftpdlib
```sh
pip install pyftpdlib
```

### 寫入Systemd
```sh
sudo nano /etc/systemd/system/pyftpserver.service
```

```s
[Unit]
Description=PyFtpServer
After=network.target

[Service]
ExecStart=/home/dennis/py-ftp-env/bin/python3 /home/dennis/PyFtpSever.py
WorkingDirectory=/home/dennis/py-ftp-env/bin
User=dennis
Restart=always
StandardOutput=journal
StandardError=journal

[Install]
WantedBy=multi-user.target
```

### 重啟systemd

```sh
sudo systemctl daemon-reload
#啟動時自動運行
sudo systemctl enable pyftpserver.service
#啟動服務
sudo systemctl start pyftpserver.service
```

你可以使用以下命令来管理PyFtpServer服务：
```
启动服务：sudo systemctl start pyftpserver.service
停止服务：sudo systemctl stop pyftpserver.service
重启服务：sudo systemctl restart pyftpserver.service
检查服务状态：sudo systemctl status pyftpserver.service
```
