import psutil


def is_davinci_open():
    for process in psutil.process_iter(['pid', 'name']):
        try:
            process_name = process.name()
            if 'Resolve.exe' in process_name or 'Davinci Resolve' in process_name:
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False


if is_davinci_open():
    print('DaVinci Resolve está aberto.')
