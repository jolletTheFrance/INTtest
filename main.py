import json
import requests

                                #### start of question one ####
postnum = input("enter number of post: ")
posturl = "http://jsonplaceholder.typicode.com/posts/" + postnum
mydict = requests.get(posturl)

while mydict.status_code >= 400 < 500:
    print("there was some kind of error, try another num")
    postnum = input("enter number of post: ")
    posturl = " http://jsonplaceholder.typicode.com/posts/" + postnum
    mydict = requests.get(posturl)

mydict = mydict.content
mydict = json.loads(mydict)


class poststock:
    def __init__(self, d):
        self.__dict__ = d
    def __str__(self):
        return self.__dict__

post1 = poststock(mydict)
print(post1.__str__())
print(type(post1))

                            ###### end of question one ######


                            #### start of question two ####
class Shape:
    def __init__(self, area1, hekef):
        self.__area1 = None
        self.__hekef = None
        self.area1 = area1
        self.hekef = hekef

    def __repr__(self):
        return f'Shape({self.area1}, {self.hekef})'

    def __str__(self):
        return f'each shape gets area and hekef: area = {self.area1} | hekef = {self.hekef}'

    @property
    def area1(self):
        return self.__area1

    @area1.setter
    def area1(self, newarea):
        if newarea != self.area1 and newarea > 0 :
            self.__area1 = newarea


    @property
    def hekef(self):
        return self.__hekef

    @hekef.setter
    def hekef(self, newhekef):
        if newhekef != self.hekef:
            self.__hekef = newhekef


shape1=Shape(324,10)
print(shape1.area1, shape1.hekef)
shape1.area1 = 25
shape1.hekef = 200
print(shape1.area1, shape1.hekef)
print(shape1)

                            #### end of question two ####

                            ####start of bouns question ####
# ליסט הוא אובייקט אשר אפשר לשנות ולבצע עליו פעולות וניתן להכניס לתוכו כל אובייקט אחר כולל כפילות
# סט היא סוג של רשימה אשר אינה מסודרת ולא מאפשרת כפילויות בתוכה כמו כן לא ניתן לערוך את הסט אך אפשר להוסיף ולהוריד ממנו איברים
# טאפל היא רשימה קבועה אותה לא ניתן לשנות אך כן ניתן לרוץ עליה, גם היא מקבלת כפילויות אך היא רשימה מסודרת והסדר שלה תמיד קבוע

numOfStars = int(input("please enter a number of stars (odd number only): "))


while numOfStars%2 == 0:
    numOfStars = int(input("please enter a number of stars (odd number only): "))

for star in range(1,numOfStars,2):
    print(" " * (20 - (star//2)), "*" * star)
for star in range(numOfStars, 0, -2):
    print(" " * (20 - (star // 2)), "*" * star)