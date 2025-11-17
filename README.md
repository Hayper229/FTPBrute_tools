





1. masscan 89.46.0.0/24 -p21  -oX recon.txt OR masscan 89.46.0.0-89.46.255.255 -p21  -oX recon.txt <- This recon 
2. bash filter_ftp.sh   OR    grep -oP 'addr="(\d+\.\d+\.\d+\.\d+)"' recon.txt | sed 's/addr="//g; s/"//g' > targets.txt.txt  <- This extract IPS from XML code
3. python3 FTP_Brute.py   <- This mass brute-force FTP servers | Resulsts saved in  FTP_results.txt
4. python3 FTP_format_convertor.py > ftps.txt <- convert in format host:user:passwd
5. python3 FTP_Grabber.py <- Start grabbing banners FTP servers 
6. python3 FTP_Dump_Report.py  <- Generate FTP report results in FTP_results.html
7. python3 FTPDumper.py <- This script for dumps files/directory from FTP servers
