import ftplib
import os

def download_ftp_directory(ftp_host, ftp_user, ftp_pass):
    os.system(f'mkdir -p dump && wget -P dump/ -r ftp://{ftp_user}:{ftp_pass}@{ftp_host}')
def main():
    with open('ftps.txt', 'r') as f:
         text = f.read().split()
         for txt in text:
             ftp_host = txt.split(':')[0]
             ftp_user = txt.split(':')[1]  # Замените на ваше имя пользователя
             ftp_pass = txt.split(':')[2]  # Замените на ваш пароль
             download_ftp_directory(ftp_host, ftp_user, ftp_pass)  # Загружаем директорию



if __name__ == '__main__':
    main()

