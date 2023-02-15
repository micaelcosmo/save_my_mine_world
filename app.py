import shutil
import os
import ctypes
import datetime
import sys

date = datetime.datetime.now().strftime("%Y-%m-%d_%Hh%Mm")
user = os.getlogin()
savedir = fr'C:\Users\{user}\AppData\Roaming\.minecraft\saves'
backupdir = fr'C:\Users\{user}\Documents\BackupSaves'


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


if is_admin():
    if not os.path.exists(backupdir):
        os.makedirs(backupdir)

    for filename in os.listdir(savedir):
        source = os.path.join(savedir, filename)
        destination = os.path.join(backupdir, filename)
    shutil.copytree(savedir, backupdir+fr'\{date}')
    print('Backup criado!')
else:
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
