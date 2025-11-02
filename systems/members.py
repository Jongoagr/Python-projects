class Member:

    def __init__(self,ID,Name,Age):
        self.ID = ID
        self.Age = Age
        self.Name = Name

class Memberships:

    def __init__(self):
        self.members = []
        self.ID = 1

    def addMember(self):
        Name = str(input("Enter Name of member to be added: "))
        Age = int(input("Enter age of new member: "))
        self.ID =+ 1
        member = Member(self.ID,Name,Age)
        self.members.append(member)
        print("Member added successfully")

    def rmMember(self):
        if self.members == []:
            print("No members currently")
        else:
            rm = int(input("Enter ID of member to remove: "))
            self.members.pop(rm - 1)
            print("Member removed successfully")
    def search(self):
        if self.members == []:
            print("No members to search")
        else:
            n = int(input("Enter ID no. of member to search for: "))
            for i in self.members:
                if i.ID == n:
                    print("The requested members info is: ", self.members[i])

sys = Memberships()
while(True):    
    print("1.Add Member to system")
    print("2.Remove member from system")
    print("3.Search up an already existing member")
    x = int(input("What Would you like to do? 1,2 or 3"))
    if x == 1:
        sys.addMember()
    elif x == 2:
        sys.rmMember()
    elif x == 1:
        sys.search()
    ch = input("do you wish to do more? y/n")
    if ch == "n" :
        break 
