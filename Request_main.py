import requests
import json
id=[]
name=[]
slug_data=[]
input_slug=0
def api():
    api1="http://saral.navgurukul.org/api/courses"
    a=requests.get(api1)
    b=a.json()
    with open("saral_course.json","w")as f:
        json.dump(b,f,indent=4)
        data=(b["availableCourses"])
    count=1
    for i in range(0,len(data)):
        course_name=data[i]["name"]
        course_id=data[i]["id"]
        name.append(data[i]["name"])
        id.append(data[i]["id"])
        print(count,course_name,course_id)
        count+=1
    return data

    
# second_round_______
def calling_api():
    # call=api()
    user_id = call[user-1]["id"]
    api2="https://saral.navgurukul.org/api/courses/"+str(user_id)+"/exercises"
    x=requests.get(api2)
    y=x.json()
    with open("exercise.json","w")as fp:
        json.dump(y,fp,indent=4)
    my_data=y["data"]
    i=0
    while i<len(my_data):
        print(i+1,my_data[i]["name"])
        child = my_data[i]["childExercises"]
        slug = my_data[i]["slug"]
        slug_data.append(my_data[i]["slug"])
        if child ==[]:
            print("   ",slug)
        else:
            j=0
            while j<len(child):
                print("  ",j+1,child[j]["name"])
                j+=1
        i+=1
    return my_data
call=api()
print("*******************Course List*******************")
user = int(input("enter any Course number="))
print(calling_api())


slug_input = int(input("Do you want slug:1.yes or 2.no:="))
def getslug():
    data_info=calling_api()
    print("*****************************Parent********************************")
    global child_input
    user1=int(input("enter parent:-"))
    user1 = user1-1
    print(data_info[user1]["name"])
    slug = data_info[user1]["slug"]
    if data_info[user1]["childExercises"]==[]:
        print(slug)
        slug_api = requests.get("https://saral.navgurukul.org/api/courses/"+str(user)+"/exercise/getBySlug?slug="+data_info[user1]["slug"])
        slug_data = slug_api.json()
        with open("slug_id.json","w") as f:
            json.dump(slug_data,f,indent=4)
        print("**********************Slug aya*********************************")
        # slug_input = int(input("Do you want slug:1.yes or 2.no:="))
        if slug_input==1:
            print(slug_data["content"])
    else:
        i=0
        while i<len(data_info[user1]["childExercises"]):
            print(i+1,data_info[user1]["childExercises"][i]["name"])
            i+=1
        print("*********************Child*****************")
        child_input = int(input("Enter Child number"))
        child_api = requests.get("https://saral.navgurukul.org/api/courses/"+str(user)+"/exercise/getBySlug?slug="+data_info[user1]["childExercises"][child_input-1]["slug"])
        child_data = child_api.json()
        with open("child_id.json","w") as f:
            json.dump(child_data,f,indent=4)
        print(child_data)
        # return child_input
    return user1
    
print(getslug())

choice=int(input("enter 1. up, 2.next,3.pre,4.stop="))
while True:
    if choice==1:
        api()
    elif choice==2:
        slug_input+=1
        getslug()
    elif choice==3:
        slug_input-=1
        getslug()
    else:
        break




            



