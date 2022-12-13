import keyboard
import os
import sys

def main():
    while(1): 
        print("========== Welcome to the Menu ==========\n")
        print("[1] Speech to Text application")
        print("[2] Gesture recognition application")
        print("[3] Exit application")
        mode = input("Wainting your input... ")
        if mode == "1":
            print("Lauching Speech to Text application...\n")
            print("On vous écoute: ")
            os.system('Stream_To_Text.py')
        if mode == "2":
            print("Lauching Gesture Reading application...")
            os.system('GestureReading.py')
        if mode == "3":
            print("Ending the application...")
            sys.exit()
        



if __name__ == "__main__":
    main()