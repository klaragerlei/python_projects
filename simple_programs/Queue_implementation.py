class Queue:
    __st=[]
    def insertion(self):
        self.__st.insert(0,input("Enter the element to be added :"))
        print("Element  successfully inserted.")

    def deletion(self):
        if (self.__st==[]):
            print("Queue underflow")
        else:
            self.__st.pop()
            print("Element  successfully removed.")

    def Display(self):
        if (self.__st==[]):
            print("Queue is empty")
        else:
            print("Element  of queue are :",self.__st)
        
obj=Queue()
print("Enter 1 to push element .")
print("Enter 2 to pop element .")
print("Enter 3 to display element .")
print("Enter 4 to quit .")
while(1):
    print()
    ch=int(input("Enter your choice :"))
    if (ch==1):
        obj.insertion()
    elif (ch==2):
        obj.deletion()
    elif (ch==3):
        obj.Display()
    elif(ch==4):
        break
    else:
        print("Wrong input. Please re-enter")
