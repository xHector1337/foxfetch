import os
import platform
import subprocess
sysName = platform.uname()
print("This script installs dependencies and adds foxfetch alias to .bashrc file.")
print("\nInstalling dependencies...")
os.system("python3 -m pip install -r ./requirements.txt")
if 'indows' in sysName:
    print("Done!")
    exit()
print("Done!\n Adding alias for foxfetch...")
path = os.getcwd()
user = os.getlogin()
os.chdir(f'/home/{user}')
with open("./.bashrc",'a') as f:
    f.write(f"alias foxfetch='python3 {path}/foxfetch.py'")
print("\nPlease use 'source ~/.bashrc' to use the alias 'foxfetch'")
