import os
from colorama import init
from termcolor import colored
from terminaltables import AsciiTable
import pathlib
os.system("cls")
current_path=pathlib.Path().absolute()
init()

First_Logo = '''
 █████╗ ██████╗ ██████╗       ██╗  ██╗██████╗ ██╗      ██████╗ ██╗████████╗███████╗██████╗ 
██╔══██╗██╔══██╗██╔══██╗      ╚██╗██╔╝██╔══██╗██║     ██╔═══██╗██║╚══██╔══╝██╔════╝██╔══██╗
███████║██║  ██║██████╔╝█████╗ ╚███╔╝ ██████╔╝██║     ██║   ██║██║   ██║   █████╗  ██████╔╝
██╔══██║██║  ██║██╔══██╗╚════╝ ██╔██╗ ██╔═══╝ ██║     ██║   ██║██║   ██║   ██╔══╝  ██╔══██╗
██║  ██║██████╔╝██████╔╝      ██╔╝ ██╗██║     ███████╗╚██████╔╝██║   ██║   ███████╗██║  ██║
╚═╝  ╚═╝╚═════╝ ╚═════╝       ╚═╝  ╚═╝╚═╝     ╚══════╝ ╚═════╝ ╚═╝   ╚═╝   ╚══════╝╚═╝  ╚═╝
                                                                                           
'''
print(colored(First_Logo,"yellow"))
print(colored("Developed By Henry Richard J","magenta"))
print()


Commands_Table = [["Command","Operation"],
                  ["list_devices","Show list of connected devices"],
                  ["connect","To connect a android device with given IP"],
                  ["disconnect_all","To disconnect all connected devices"],
                  ["get_shell","To get shell for the given device"],
                  ["install_apk","To install the APK to device"],
                  ["uninstall_apk","To uninstall app from the device"],
                  ["list_all_apps","To list all apk installed in the device"],
                  ["hardware_info","Show hardware info as thermal stuff for cpu, gpu and battery"],
                  ["open_website","Open a given website with default browser"],
                  ["factory_reset","To perform Factory Reset!"],
                  ["add_contact","To add a new Contact"],
                  ["simulate_swipe_notifications","To bring down notification"],
                  ["screen_record","To record Screen for 3m"],
                  ["screen_shot","To take Screenshot of the device."],
                  ["get_contacts","To get all the contact list from the device"],
                  ["turn_off_wifi","To turn of wifi"],
                  ["get_device_ip","To get local IP of the device"],
                  ["dump_gps","To get all gps logs like last known location, etc.."],
                  ["run_apk","To run the given app in the device"]]

table = AsciiTable(Commands_Table)

print(colored(table.table,"blue"))

class ADB:

    def help(self):
        print(colored(table.table,"blue"))

    def list_devices(self):
        os.system("adb devices")

    def connect(self):
        ip = input(colored("Enter Mobile IP> ","red"))
        os.system(f"adb connect {ip}:5555")

    def disconnect_all(self):
        os.system("adb disconnect")

    def get_shell(self):
        ip = input(colored("Enter Device NameP> ","red"))
        os.system(f"adb -s {ip} shell")

    def install_apk(self):
        device = input("Enter Name Device> ")
        path = input(f"({device})->Path of the file> ")
        os.system(f"adb -s {device} install {path}")

    def uninstall_apk(self):
        device = input("Enter Name Device> ")
        package_name = input(f"({device})->Path of the file> ")
        os.system(f"adb -s {device} uninstall {package_name}")

    def list_all_apps(self):
        device = input("Enter Device Name> ")
        os.system(f"adb -s {device} shell pm list packages")

    def pull_file(self):
        pass

    def pull_folder(self):
        pass

    def push_folder(self):
        pass

    def push_file(self):
        pass

    def hardware_info(self):
        device = input("Enter Device Name> ")
        os.system(f"adb -s {device} shell dumpsys hardware_properties")

    def open_website(self):
        device = input("Enter Device Name> ")
        website = input("Enter the website to open with protocol eg:('http:// or https://')> ")
        os.system(f"adb -s {device} shell am start -a android.intent.action.VIEW -d {website}")

    def factory_reset(self):
        device = input("Enter Device Name> ")
        os.system(f"adb -s {device} shell am broadcast -a android.intent.action.MASTER_CLEAR")

    def add_contact(self):
        device = input("Enter Device Name> ")
        name = input("Enter Contact Name> ")
        number = input("Enter Contact Number> ")
        os.system(f"adb -s {device} shell am start -a android.intent.action.INSERT -t vnd.android.cursor.dir/contact -e name '{name}' -e phone {number}")

    def Simulate_swipe_notifications(self):
        device = input("Enter Device Name> ")
        os.system(f"adb -s {device} shell input swipe 0 0 0 300")

    def screen_record(self):
        device = input("Enter Device Name> ")
        print("[*] Please Wait for 3 minutes recording..........")
        os.system(f"adb -s {device} shell screenrecord /sdcard/demo.mp4")
        save_path = input("Enter name for the file> ")
        os.system(f'adb -s {device} pull /sdcard/demo.mp4 "{current_path}\\{save_path}".mp4')

    def screen_shot(self):
        device = input("Enter Device Name> ")
        print(colored("[*] Please Wait taking screenshot..........","cyan"))
        os.system(f"adb -s {device} shell screencap /sdcard/screen.png")
        print("[*] Success!")
        save_path = input("Enter a name for the file> ")
        os.system(f'adb -s {device} pull /sdcard/screen.png "{current_path}\\{save_path}".png')

    def get_contacts(self):
        device = input("Enter Device Name> ")
        print(colored("[*] Getting all contacts list..........","cyan"))
        os.system(f"adb -s {device} shell content query --uri content://contacts/phones/")

    def turn_off_wifi(self):
        device = input("Enter Device Name> ")
        print("[*] Turning off wifi......")
        os.system(f"adb -s {device} shell svc wifi disable")
        print(colored("[*] Success!","green"))

    def get_device_ip(self):
        device = input("Enter Device Name> ")
        print("[*] Getting local ip of the device.........")
        os.system(f"adb -s {device} shell ip address show wlan0")

    def dump_gps(self):
        device = input("Enter Device Name> ")
        print("[*] Getting location of the device.........")
        os.system(f"adb -s {device} shell dumpsys location")

    def run_apk(self):
        device = input("Enter Device Name> ")
        package_name = input("Enter Package name eg:(com.example.names)>")
        os.system(f"adb -s {device} shell monkey -p {package_name} -v 500")


while True:
    choice = input(colored("ADB-Hacker> ","red")).lower()

    if choice == "help":
        ADB().help()

    elif choice == "exit":
        print("[*] Exiting.........")
        print("Thank you for using ADB-HACKER if you liked this Please give a star in github repo! ")
        break

    elif choice == "list_devices":
        ADB().list_devices()

    elif choice == "connect":
        ADB().connect()

    elif choice == "disconnect_all":
        ADB().disconnect_all()

    elif choice == "get_shell":
        ADB().get_shell()

    elif choice == "install_apk":
        ADB().install_apk()

    elif choice == "uninstall_apk":
        ADB().uninstall_apk()

    elif choice == "list_all_apps":
        ADB().list_all_apps()

    elif choice == "hardware_info":
        ADB().hardware_info()

    elif choice == "open_website":
        ADB().open_website()

    elif choice == "factory_reset":
        ADB().factory_reset()

    elif choice == "add_contact":
        ADB().add_contact()

    elif choice == "simulate_swipe_notifications":
        ADB().Simulate_swipe_notifications()

    elif choice == "screen_record":
        ADB().screen_record()

    elif choice == "screen_shot":
        ADB().screen_shot()

    elif choice == "get_contacts":
        ADB().get_contacts()

    elif choice == "turn_off_wifi":
        ADB().turn_off_wifi()

    elif choice == "get_device_ip":
        ADB().get_device_ip()

    elif choice == "dump_gps":
        ADB().dump_gps()

    elif choice == "run_apk":
        ADB().run_apk()




