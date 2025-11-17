with open('FTP_results.txt', 'r') as f:
    ftp_links = f.read().splitlines()
    for link in ftp_links:
        if "[FTP]:" in link:
            parts = link.split("ftp://")[1].split("@")
            user_pass = parts[0].split(":")
            host = parts[1]
            print(f"{host}:{user_pass[0]}:{user_pass[1]}")


#with open('FTP_results.txt', 'r') as f:
  #   ftp_links = f.read().split()
   #  for link in ftp_links:
    #     parts = link.split("//")[1].split("@")
     #    user_pass = parts[0].split(":")
      #   host = parts[1]
       #  print(f"{host}:{user_pass[0]}:{user_pass[1]}")
