st=[]



def push():
    i=int(input("enter the value to be added:"))
    st.append(i)
    

def pull():
    if len(st)>0:
        st.pop()
        print("Value popped")
    else:
        print("Stack is empty!!")

def show():
    j=len(st)-1
    while j>=0:
        print("|",end="")
        print(st[j], end="|")
        print()
        print(" ---")
        j-=1

def choose(ch):
    if ch==1:
        push()
    if ch==2:
        pull()
    if ch==3:
        show()
    if ch==4:
        print("Good Bye !!")
        exit()

print("*****Stack Implementation*****")

while True:

    ch=int(input("Enter the choice please: push:1, pull:2, show:3, exit:4 -  "))
    choose(ch)

