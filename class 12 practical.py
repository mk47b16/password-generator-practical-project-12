'''import random
import string

def generate_password(length=12, uppercase=True, digits=True, symbols=True):
    characters = string.ascii_letters if uppercase else string.ascii_lowercase
    characters += string.digits if digits else ''
    characters += string.punctuation if symbols else ''

    if not any((uppercase, digits, symbols)):
        print("Please enable at least one of uppercase, digits, or symbols.")
        return None

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def save_to_file(passwords, filename="passwords.txt"):
    with open(filename, "w") as file:
        for password in passwords:
            file.write(password + "\n")

def main():
    num_passwords = int(input("Enter the number of passwords to generate: "))

    if num_passwords < 1:
        print("Please enter a valid number of passwords.")
        return

    password_length = int(input("Enter the length of the passwords: "))
    include_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    include_digits = input("Include digits? (y/n): ").lower() == 'y'
    include_symbols = input("Include symbols? (y/n): ").lower() == 'y'

    passwords = []
    for _ in range(num_passwords):
        generated_password = generate_password(
            length=password_length,
            uppercase=include_uppercase,
            digits=include_digits,
            symbols=include_symbols
        )
        if generated_password:
            passwords.append(generated_password)

    print("\nGenerated Passwords:")
    for password in passwords:
        print(password)

    save_to_file(passwords)

if __name__ == "__main__":
    main()'''
"""import csv

with open("profile.csv","w",newline="")as file:
    writer=csv.writer(file)
    employee=["name","age","salary"]
    
    writer.writerow(employee)
    writer.writerow(["anya","17","900"])
    
print("csv file created")

file=open("profile.csv","r")
reader=csv.reader(file)
    
print(reader)"""

"""import random
import string
import mysql.connector

# Function to generate a password
def generate_password(length=12, uppercase=True, digits=True, symbols=True):
    characters = string.ascii_letters if uppercase else string.ascii_lowercase
    characters += string.digits if digits else ''
    characters += string.punctuation if symbols else ''

    if not any((uppercase, digits, symbols)):
        print("Please enable at least one of uppercase, digits, or symbols.")
        return None

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Function to save passwords to MySQL database
def save_to_database(username, email, password):
    try:
        connection = mysql.connector.connect(
            host="your_mysql_host",
            user="your_mysql_user",
            password="your_mysql_password",
            database="your_database_name"
        )

        cursor = connection.cursor()

        # Insert data into the 'passwords' table
        insert_query = "INSERT INTO passwords (username, email, password) VALUES (%s, %s, %s)"
        data = (username, email, password)
        cursor.execute(insert_query, data)

        connection.commit()
        print("Password saved to the database.")

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

# Main function
def main():
    print("Password Generator and Saver Application")
    print("=======================================")

    # Get user input
    username = input("Enter your username: ")
    email = input("Enter your email: ")

    num_passwords = int(input("Enter the number of passwords to generate: "))
    if num_passwords < 1:
        print("Please enter a valid number of passwords.")
        return

    password_length = int(input("Enter the length of the passwords: "))
    include_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    include_digits = input("Include digits? (y/n): ").lower() == 'y'
    include_symbols = input("Include symbols? (y/n): ").lower() == 'y'

    # Generate passwords and save to the database
    for _ in range(num_passwords):
        generated_password = generate_password(
            length=password_length,
            uppercase=include_uppercase,
            digits=include_digits,
            symbols=include_symbols
        )
        if generated_password:
            save_to_database(username, email, generated_password)

# Execute the main function
if __name__ == "__main__":
    main()
"""


"""data=["l",20,"M",40,"N",60]
time=0
alpha=""
add=0
for c in range(1,6,2):
    time=time+c
    alpha=alpha+data[c-1]+"@"
    add=add+data[c]
    print(time,add,alpha)"""

"""L=[1,2,3,4,5]
lst=[]
for i in range(len(L)):
    if i%2==1:
        t=(L[i],L[i]**2)
        lst.append(t)
print(lst)"""

'''import random
M=[5,10,15,20,25,30]
for i in range(1,3):
    first=random.randint(2,5,–1)
    sec=random.randint(3,6,–2)
    third=random.randint(1,4)
print(M[first], M[sec], M[third],sep="#")'''

###############################################################################################

"""def read():
    f=open("marmik.txt","r")
    lines=f.readlines()
    for i in lines:
        w=i.split()
        if w[0]=='i':
            print(w,end='\n')
            
        
read()"""
"""
def uvl():
    f=open("marmik.txt","r")
    line=f.readline()
    u=v=l=c=0
    for i in line:
        if i.isalpha():
            if i.isupper():
                u+=1
            if i.islower():
                l+=1
            if i in 'aeiou':
                v+=1
            else:
                c+=1
    print("vo=",v)
    print("up=",u)
    print("lo=",l)
    print("co=",c)
    
uvl()"""
    
        
                    
"""def remove():
    f1=open("marmik.txt",'r')
    line=f1.readlines()
    f2=open("marmik.txt","w")
    for i in line:
        w=i.split()
        if w[0]=='i':
            f2.write(i)
        
    print("new file is updated")
        
    
remove()"""

"""import pickle

def write():
    f=open("stud.dat","wb")
    while True:
        r=int(input("enter roll no of student:"))
        n=input("enter the name of the student:")
        data=[r,n]
        pickle.dump(data,f)
        ch=input("more records? (y/n)")
        if ch in 'Nn':
            break
    f.close()
    
def read():
    f=open("stud.dat","rb")
    try:
        while True:
            rec=pickle.load(f)
            print(rec)
            
    except EOFError:
        f.close()

def search():
    found=0
    r1=int(input("enter roll no which name want to display:"))
    f=open("stud.dat","rb")
    try:
        while True:
            rec=pickle.load(f)
            if rec[0]==r1:
                print(rec[1])
                found=1
    except EOFError:
        f.close()
    if found==0:
        print("the given record is not present in the file please check....")
        

write()
read()
search()
   """         
    
###############################################################################################


"""import pickle

def write():
    f=open("stud.dat","wb")
    while True:
        r=int(input("enter the rollno:"))
        n=input("enter the name of the student:")
        m=int(input("enter the marks of the student:"))
        rec=[r,n,m]
        pickle.dump(rec,f)
        ch=input("more rec?(y/n):")
        if ch=='n':
            break
    f.close
    
def read():
    f=open("stud.dat","rb")
    try:
        while True:
            rec=pickle.load(f)
            print(rec)
        f.close
            
            
write()
read()
"""




########################################rolling a dice#############################################################

"""import random

while True:
    num=random.randint(1,6)
    print(num)
    ch=input("roll again?(y\n)")
    if ch in 'nN':
        break

print("thank ou***************************")"""








"""n=int(input("enter the number to check:"))
rev=0
x=n
while (n>0):
    rev=(rev*10)+n%10
    n=n//10
if(x==rev):
    print("the number is a pelindrom ")
    print(rev)
else:
    print("the number is not a pelindrom")
    print(rev)"""







"""import csv

def write():
    f1=open("details.csv","w",newline='')
    w=csv.writer(f1)
    w.writerow(["user_id","name"])
    while True:
        id=int(input("enter the user_id of the person:"))
        n=input("enter the name of the person")
        data=[id,n]
        w.writerow(data)
        ch=input("enter more details?(y/n):")
        if ch in "nN":
            break
    f1.close()

write()"""

"""def read():
    f1=open("details.csv","r")
    r=csv.reader(f1)
    for i in r:
        print(i)
    f1.close()
        
    
        


def search():
    f1=open("details.csv","r")
    n=input("enter the user_id to search:")
    f=0
    r=csv.reader(f1)
    for i in r:
        if i[0]==n:
            print(i[1])
            f+=1
        
        
    f1.close()
    if f==0:
            print("sorry... no id found")
            

read()
search()"""
##############################################################################################################  
'''def isempty(stk):
    if stk==[]:
        return True
    else:
        return False
    
    

def push(stk,elt):
    stk.append(elt)
    print("element inserted.......")
    print(stk)
    
def pop(stk):
    if isempty(stk):
        print("stack is empty")
    else:
        print("deleted element",stk.pop())
def peek(stk):
    if isempty(stk):
        print("stack is empty........")
    else:
        print("stack at the top ",stk[-1])

def display(stk):
    if isempty(stk):
        print("stack is empty...........")
    else:
        for i in range(len(stk)-1,-1,-1):
            print(stk[i])
    
stack=[]
while True:
    print("......................stack fuctions..........................")
    print("1, push")
    print("2, pop")
    print("3, peek")
    print("4, display")
    print("5, exit")
    ch=int(input("enter the no from 1-5 which you want to do with stack"))
    if ch==1:
        element=int(input("enter the element which you want to add"))
        push(stack,element)
    if ch==2:
        pop(stack)
    if ch==3:
        peek(stack)
    if ch==4:
        display(stack)
        
    elif ch==5:
        break'''



####################################################################################################################3
"""import csv

def mk(file1):
    f2=open("profile2.csv","w",newline='')
    s=csv.writer(f2,delimiter="#")
    data=csv.reader(file1)
    
    for i in data:
        if i[0][:5]!= "check":
            s.writerow(i)
    f2.close()
    
f1=open("details.csv","r")
mk(f1)
print("another file is created of the same content")"""
        
        



