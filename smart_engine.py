import os
import subprocess
import ctypes
import sys

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def apply_critical_updates():
    try:
        print("Checking for updates...")
        subprocess.run(["powershell", "Install-WindowsUpdate", "-AcceptAll", "-AutoReboot"], check=True)
        print("Updates applied successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to apply updates: {e}")

def set_power_management():
    try:
        print("Applying power management tweaks...")
        # Set power plan to 'Balanced'
        subprocess.run(["powercfg", "/setactive", "381b4222-f694-41f0-9685-ff5bb260df2e"], check=True)
        
        # Enable hibernation
        subprocess.run(["powercfg", "/hibernate", "on"], check=True)
        
        print("Power management tweaks applied successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to apply power management tweaks: {e}")

def main():
    if not is_admin():
        print("This program requires administrative privileges.")
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
        sys.exit()

    print("Welcome to SmartEngine!")
    apply_critical_updates()
    set_power_management()
    print("SmartEngine has successfully optimized your device.")

if __name__ == "__main__":
    main()