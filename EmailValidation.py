#Email Validation System in python using String functions
print("Email Validation System in python using String functions")
email = input("Enter your email : ")
d,k,j=0,0,0
if len(email) >= 6: #1
    if email[0].isalpha():#2
        if ("@"  in email) and (email.count("@")==1):#3
            if (email[-4]==".") ^ (email[-3]=="." ):#4
                for i in email:
                    if i == i.isspace(): #5
                        k=1
                    elif i.isalpha(): #5
                        if i==i.upper(): #w-> W==w  #W-> W==W
                            j=1
                    elif i.isdigit():#5
                        continue
                    elif i=="_" or i=="." or i=="@":
                        continue
                    else:
                        d=1 #for other special characters (!#$%&*)

                if k==1 or j==1 or d==1:
                    print("wrong Email 5")
                else: 
                    print("Right Email")
            else:
                print("wrong Email 4")
        else: 
            print("wrong Email 3")
    else:
        print("wrong Email 2")
else: 
    print("wrong Email 1")

