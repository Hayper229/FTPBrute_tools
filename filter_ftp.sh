grep -oP 'addr="(\d+\.\d+\.\d+\.\d+)"' recon.txt | sed 's/addr="//g; s/"//g' > targets.txt
