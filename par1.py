lst=[];
def get_string():
    str=input("Enter string:");
    return str;

def get_length():
    str=get_string();
    print("length of the string is: ",len(str));

def join_string():
    str1=get_string();
    str2=get_string();
    print("join string: ",(str1+str2));

def compare_string():
    str1=get_string();
    str2=get_string();
    if(str1==str2):
        print("Equal");
    else:
        print("Different");

def reverse_string():
    str=get_string();
    print("Reverse String: ",str[::-1]);

def check_palindrome():
    str=get_string();
    temp=str;
    print(str);
    print(temp);
    if(temp==str):
        print(str," is palindrome");
    else:
        print(str," is not palindrome");
def check_word():
    str=get_string();
    word=input("Enter word u want to check :");
    if word in str:
        print(word," is available in ",str);
    else:
         print(word," is not available in ",str);

def menu():
    while(1):
        print("Menu items:");
        print("\n 1.String length \n 2.Join String \n 3.Compare String \n 4.Reverse String \n 5.Check palindrome \n 6. check word in sentense \n 7.Exit");
        ch=int(input("Enter choice:"));
        if(ch == 1):
            get_length();
        elif(ch == 2):
            join_string();
        elif(ch == 3):
            compare_string();
        elif(ch == 4):
            reverse_string();
        elif(ch == 5):
            check_palindrome();
        elif(ch == 6):
            check_word();
        else:
            break;
menu();
        

        
