import subprocess
import re
import requests



def formating(val):
    pos = val.find(":")
    value = val[pos + 1:]
    return value


def run_command():
    command = "WMIC BIOS GET SERIALNUMBER"
    # command="sudo dmidecode -t system | grep Serial"
    # command =serial_number = "show version | grep SN:"
    output = subprocess.run(command, shell=True, capture_output=True)
    serial_number = output.stdout.decode("utf-8").strip()
    return serial_number

def get_serial_number():
    serial = run_command()
    print("The value of Serial Number is: ", serial)
    if serial is None:
        print("-1")
    # val = vimal.find(":")
    val=serial.find("\n")
    serial = serial[val + 1:]
    return serial



def get_response():
    serialnumber=get_serial_number()
    payload={"SN": serialnumber}
    try:
        res=requests.get('http://127.0.0.1:5000/',params=payload)
        if res.status_code==200:
            data=res.json()
            return (data)
        else:
            return ({"error": "Failed to get data from API"})
    except requests.exceptions.RequestException as e:
        return ({"error": str(e)})



ans=get_response()
with open("bootflash.txt", "w") as bootflash:
    bootflash.write(str(ans))

