import ftplib

def main(host, user, passwd):
    try:
        ftp = ftplib.FTP(host)
        ftp.login(user=user, passwd=passwd)
        print(f'Grabbed banner: {ftp.welcome}')
    except Exception as e:
           pass #print(f'Error: {e}')

if __name__ == "__main__":
    infos = []
    with open('ftps.txt', 'r') as f:
        infos = f.read().split()
        for info in infos:
            host, user, passwd = info.split(':')
            main(host, user, passwd)
