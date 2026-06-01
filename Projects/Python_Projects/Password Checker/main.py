import re
import time

from colorama import Fore, Back, Style, init


pass_score = 0
weak_pass = set()


#  LOADS WEAK PASSWORDS FILE INTO LIST

def load_file(filename):
    try:

        with open (filename, "r") as f:
              for line in f:

                    line = line.strip()
                    if line == "":
                        pass

                    else:
                        weak_pass.add(line)


        print(weak_pass)
        return weak_pass

    except FileNotFoundError as e:
        print(e)

#  CHECKS FOR PASSWORD SCORES

def check_score(pwd, pass_score = 0):
    length = False
    letter = False
    number = False
    symbol = False
    caps = False

    if pwd in weak_pass:
        print(Fore.RED + f"This Password is on a Weak Password List. Please Chose another one.\n" + Style.RESET_ALL)
        exit()

    if re.search("[a-z]", pwd):
        pass_score += 1
        letter = True

    if re.search("[A-Z]", pwd):
        pass_score += 1
        caps = True

    if re.search("[0-9]", pwd):
        pass_score += 1
        number = True

    if re.search("[!@#$%^&*()_+~/]", pwd):
        pass_score += 1
        symbol = True

    if len(pwd) > 8:
        pass_score += 1
        length = True


    return pass_score,letter,caps,number,symbol,length

#  PRINTS RECOMMENDATIONS TO IMPROVE PASSWORD

def recommendation(letter, caps, number, symbol, length):

    print(Fore.GREEN + f"[!] Recommendation for Password" + Style.RESET_ALL)

    if letter == False:
        print(f"Please add a lower case letter to your Password.")
    if caps == False:
        print(f"Please add a capital letter to your Password.")
    if number == False:
        print(f"Please add a Number to your Password.")
    if symbol == False:
        print(f"Please add a Symbol to your Password.")
    if length == False:
        print(f"Please make your password 8 characters or longer.")
    if letter == True and caps == True and number == True and symbol == True and length == True:
        print(f"No recommendations. Great Work!.\n")

#  MAIN FUNCTION

def main():

    load_file("weak_pass.txt")

    print(Fore.GREEN + f"WELCOME TO THE PASSWORD CHECKER APP.\n")

    time.sleep(1)

    pwd = input(Fore.GREEN + "Please enter your password:\n>>> "  + Style.RESET_ALL)

    pass_score,letter,caps,number,symbol,lenght = check_score(pwd)


    print(Fore.GREEN + f"[!] Checking Password Complexity and Length..."  + Style.RESET_ALL)

    time.sleep(3)

    print(Fore.GREEN + f"[!] PRINTING RESULTS.....\n")

    time.sleep(1)

    if pass_score == 0:
        print(Fore.RED + "[!] WEAK [!]"  + Style.RESET_ALL)
        print(Fore.RED + f"[!][!] Your password is too Weak.\n[!][!]Please Chose a more Secure Password.")

    if pass_score == 1:
        print(Fore.RED + "[!] WEAK [!]"  + Style.RESET_ALL)
        print(f"[!][!] Your password is Weak.\n[!][!]Please Chose a more Secure Password.")

    if pass_score == 2:
        print(Fore.BLUE + "[!] MODERATE [!]"  + Style.RESET_ALL)
        print(f"[!][!] Your password is  Moderate. \n[!][!]Please add more complexity to your Password.")

    if pass_score == 3:
        print(Fore.BLUE + "[!] MODERATE [!]"  + Style.RESET_ALL)
        print(f"[!][!] Your password is  Moderate. \n[!][!]Please add more complexity to your Password.")

    if pass_score == 4:
        print(Fore.GREEN + "[!] SECURE [!]"  + Style.RESET_ALL)
        print(f"[!][!] Your password is Secure. Congratulations.")

    if pass_score == 5:
        print(Fore.GREEN + "[!] SECURE [!]" + Style.RESET_ALL)
        print(f"[!][!] Your password is Secure. Congratulations.")

    time.sleep(1)

    print(Fore. BLUE + Style.BRIGHT + f"Your Password Score is {pass_score} \n" + Style.RESET_ALL)

    time.sleep(2)

    recommendation(letter, caps, number, symbol, lenght)


# RUN APP
if __name__ == "__main__":

    x = True

    while x:
        choice = input(Fore. GREEN + f"Password Checker\nWould you like to check your password? (y/n) \n>>> " + Style.RESET_ALL)
        if choice.lower() == "y" or choice.lower() == "yes":
            main()
        elif choice.lower() == "n" or choice.lower() == "no":
            exit()
        else:
            print(Fore.RED + f"Please enter y or n." + Style.RESET_ALL)
            continue
