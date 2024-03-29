import errno
import os
import os.path
import pyperclip
import random
import shutil
import sys
import time


def check_directories():
    directories = ["data/reg", "data/backups"]
    for directory in directories:
        if not os.path.exists(directory):
            try:
                os.makedirs(directory)
            except OSError as e:
                print("Error creating directory:", directory)
                print("Error:", e)


def dots():
    time.sleep(1)


def clear():
    if sys.platform.startswith("win"):
        os.system("cls")
    else:
        os.system("clear")


def cont():
    input("Press Enter to continue.")
    clear()


def invalid():
    print("Invalid input.")
    cont()


def save(pwd):
    while True:
        title = input("Name your password: ")
        if not title.strip():
            print("Password name cannot be empty. Please enter a valid name.")
        elif check_file(title):
            print("Password name already in use, choose another.")
        else:
            break

    file = open("data/reg/" + title, "a")
    file.write(str(pwd))
    file.close()


def check_file(title):
    file_path = os.path.join("data/reg/", title)
    return os.path.exists(file_path)


def listar_archivos(directorio):
    check_directories()
    archivos = [os.path.splitext(x)[0] for x in os.listdir(directorio)]
    for line in archivos:
        line = line.strip().split("\t")
        print(line)
    return archivos


def backup(src, dest, restore=False):
    check_directories()
    try:
        if restore:
            shutil.copytree(src, dest)
            print("Restoring back up")
            dots()
            print("Back up restored.")
        else:
            shutil.copytree(src, dest)
            print("Creating back up")
            dots()
            print("Back up created.")
    except OSError as e:
        if e.errno == errno.ENOTDIR:
            shutil.copy(src, dest)
            if restore:
                print("File restored.")
            else:
                print("File copied.")
        else:
            print("Directory not copied. Error: %s" % e)


while True:  # MAIN MENU#
    check_directories()
    clear()
    print("\033[92m### MAIN MENU ###" "\x1b[0m")
    print("Select option:")
    print("1.Generate")
    print("2.Override")
    print("3.Retrive")
    print("4.Remove")
    print("5.Back Up")
    print("6.Exit")
    try:
        choose = int(input("Enter choice:"))
    except ValueError:
        invalid()
        continue

    if choose == 1:  # GENERATE#
        clear()
        print("\033[92m### GENERATE ###" "\x1b[0m")
        try:
            length = int(input("Set password length and press enter:"))
        except ValueError:
            invalid()
            continue
        chars = (
            "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*.()"
        )
        password = "".join(random.choice(chars) for r in range(length))
        dots()
        print("Password generated:", password)
        pyperclip.copy(password)
        print("Your password is", length, "characters long")
        save(password)
        print("You password has been stored and copied to clipboard.")
        cont()
        continue

    elif choose == 2:  # OVERRIDE#
        clear()
        print("\033[92m### OVERRIDE ###" "\x1b[0m")

        lst = listar_archivos("data/reg/")
        file = str(input("Type password name to Override:"))
        if file in lst:
            newpwd = input("Type new password:")
            with open("data/reg/" + file, "w") as f:
                f.write(str(newpwd))
                f.close()
                print("Password succesfully overrided")
                cont()
        else:
            invalid()
        continue

    elif choose == 3:  # RETRIVE#
        clear()
        print("\033[92m### RETRIVE ###" "\x1b[0m")
        lst = listar_archivos("data/reg/")
        file = input("Type password name to retrive:")
        if file in lst:
            clear()
            with open("data/reg/" + file, "r") as myfile:
                data = myfile.read()
                print("Your " + file + " password is:" + data)
                pyperclip.copy(data)
                print("Password copied to clipboard")
                input("Press Enter to Main Menu")
                continue
        else:
            print("Password not found")
            cont()
            continue

    elif choose == 4:  # REMOVE#
        clear()
        print("\033[92m### REMOVE ###" "\x1b[0m")

        lst = listar_archivos("data/reg/")
        rem = input("Type password name to REMOVE and press ENTER:")
        if rem in lst:
            a = input(
                " Are you sure to delete current Password?\n \
                      Please enter y/n:"
            )
            if a == "y":
                if os.path.exists("data/reg/" + rem):
                    os.remove("data/reg/" + rem)
                    print("Password: " + rem + " REMOVED")
                    cont()
                continue
            if a == "n":
                print("Password not removed")
                cont()
            else:
                print("Please enter either y/n:")
            continue
        else:
            invalid()
        continue

    elif choose == 5:  # BACK UP#
        clear()
        print("\033[92m### BACK-UP ###" "\x1b[0m")
        print("\n1.Write new Back Up.\n2.Restore previous Back Up.\n3.Cancel.")
        opt = input("Enter choice: ")
        if opt == "1":
            newbk = input("Name your new Back up: ")
            backup("data/reg/", "data/backups/" + newbk + "/")
            cont()
        elif opt == "2":
            clear()
            lst_backups = listar_archivos("data/backups/")
            bk = input("Select which copy do you want to restore: ")
            if bk in lst_backups:
                check = input(
                    "This action will remove all previously saved data. Do you\
                          wish to continue?\nPlease enter either y/n: "
                )
                if check == "y":
                    shutil.rmtree("data/reg/")
                    backup("data/backups/" + bk + "/", "data/reg/", restore=True)
                    cont()
                if check == "n":
                    print("Action CANCELED")
                    cont()
                else:
                    print("Please enter either y/n:")
                continue
        else:
            invalid()
        continue

    elif choose == 6:  # EXIT#
        clear()
        check = input("Are you sure you want to exit?\nPlease enter y/n: ").lower()
        if check == "y":
            sys.exit(0)
        elif check == "n":
            continue
        else:
            invalid()

    else:
        invalid()
        continue
