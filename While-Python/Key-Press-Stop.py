import msvcrt
import time

while True:
    print("Hello! IF YOU WANT TO STOP! Press C.")

    time.sleep(0.7)

    if msvcrt.kbhit():
        key = msvcrt.getch().decode("utf-8").lower()

        if key == "c":
            print("Program stopped. Bye!")
            break
