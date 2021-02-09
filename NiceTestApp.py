import platform
import sys

my_system = platform.uname()

def log_info():
    f = open("NiceTestApp.log", "a")
    f.write(f"SYSTEM: {my_system.system}\n")
    f.write(f"Node Name: {my_system.node}\n")
    f.write(f"Release: {my_system.release}\n")
    f.write(f"Version: {my_system.version}\n")
    f.write(f"Machine: {my_system.machine}\n")
    f.write(f"Processor: {my_system.processor}\n")
    f.close()

def log_info_console():
    print(f"System: {my_system.system}")
    print(f"Node Name: {my_system.node}")
    print(f"Release: {my_system.release}")
    print(f"Version: {my_system.version}")
    print(f"Machine: {my_system.machine}")
    print(f"Processor: {my_system.processor}")

if sys.argv[-1]=="NiceTestApp.py":
    log_info_console()

elif sys.argv[1]=="-logInfo":
    log_info()
    log_info_console()

elif sys.argv[1]=="-help":
    print("This is Helping Text")
