import os
import platform

def get_uptime():
    if platform.system() == "Windows":
        # On Windows, use 'net stats srv'
        output = os.popen("net stats srv").read()
        for line in output.split('\n'):
            if "Statistics since" in line:
                print(f"System uptime info: {line}")
                return
        print("Could not determine uptime on Windows.")
    else:
        # On Unix/Linux, use 'uptime -p'
        output = os.popen("uptime -p").read().strip()
        print(f"System uptime: {output}")

if __name__ == "__main__":
    get_uptime()
