with open('FTP_results.txt', 'r') as f:
     ftp_links = f.read().split()
     for link in ftp_links:
         parts = link.split("//")[1].split("@")
         user_pass = parts[0].split(":")
         host = parts[1]
         print(f"{host}:{user_pass[0]}:{user_pass[1]}")
