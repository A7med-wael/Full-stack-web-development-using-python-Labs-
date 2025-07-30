import re
import random
def generat_array(len,start):
    arr = []
    for i in range(len):
        arr.append(start+i)
    return arr
print(generat_array(5,3))


def check_num(num):
    if num%3==0 and num%5==0:
        return "FizzBuzz"
    elif num%3==0:
        return "Fizz"
    elif num%5==0:
        return "buzz"
num = int(input("enter num: "))
print(check_num(num))


def reversed_text(txt):
    Rtxt = ""
    for i in range(len(txt)):
        Rtxt += txt[len(txt)-i-1] 
    return Rtxt
txt = input("Enter text: ")
print(reversed_text(txt))


def get_name():
    while True:
        name = input("Enter your name: ")
        if not name:
            print("name can not be empty")
        elif name.isdigit():
            print("name can not be digit")
        else:
            return name
        
def is_email(email):
    pattern = '^[a-zA-Z][a-zA-Z0-9._]*@[a-zA-Z]+\.(com|net|org|eg)$'
    return re.match(pattern, email) is not None

def get_email():
    while True:
        email = input("Enter your email: ")
        if is_email(email):
            return email
        else:
            print("invalid email")

def get_data():
    name = get_name()
    email = get_email()
    print("your name: ",name)
    print("your email: ",email)

get_data()



def long_substr(txt):
    cntr=0
    mx=0
    str=""
    arr = []
    for i in range(len(txt)-1):  # 4 abced
        if (txt[i]<txt[i+1]):
            cntr+=1
            str+=txt[i]
            # print(str)
        else:
            cntr+=1
            mx = max(mx,cntr)
            # print(mx)
            cntr=0
            str+=txt[i]
            arr.append(str)
            str=""
    print(arr)        
    for i in arr:
        if len(i) == mx:
            return i
        
print(long_substr("abcd"))



def avg_num():
    avg = 0
    cntr = 0
    while True:
        num = input("Enter number: ")
        if not num.isdigit():
            if num == "done":
                break
        else:
            cntr+=1
            avg+=int(num)
    avg /=cntr
    return avg
print(avg_num())


def guess_game():
    words = ['ahmed', 'wael', 'sports', 'teams', 'computer']
    word = random.choice(words)
    temp = ""
    for i in range(len(word)):
        temp += '-'
    name = input("Enter your name: ")
    print(f"Hello {name}, in our game you have 7 turns only")
    for i in range(7):
        ch = input("guess letter: ")
        if ch in word:
           temp = temp[:word.find(ch)] + ch + temp[word.find(ch)+1:]
           word = word[:word.find(ch)] + '#' + word[word.find(ch)+1:] 
           print(f"good choice, your word now is: {temp}")
        else:
            print("Not found, try again")
    if '-' not in temp:
        print(f"you guessed the word successfuly, and the word is {temp}\nthanks {name}")
    else:
        print(f"your guess is not correct and the final result is: {temp}, you can try the game again\nthanks {name}")

guess_game()
