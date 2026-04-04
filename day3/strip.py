#1. rstrip() ===> to remove spaces at right hand side 
#2. lstrip() ===> to remove spaces at left hand side 
#3. strip () ==> to remove spaces both side 

programming = input("enter ypur programming name :")
p_name = programming.rstrip()
if p_name=='python' :
    print(p_name)
elif p_name=='java' :
    print(p_name)
elif p_name =='Cpp' :
    print(p_name)
else:
    print("Wrong programming name")