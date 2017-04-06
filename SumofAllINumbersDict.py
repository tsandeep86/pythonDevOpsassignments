"""04/04/2017
Print addition of all the integers from the following dict(), make sure you don't miss any integer value.
dict = {'first':'apple','second':'100','third':16,4:42,'six':(5,12,8),'ten':['aaa','ball',34,01],'seven':'555','100':{1:10,2:20,'pop':5},'float':10.5}"""

d= {'first':'apple','second':'100','third':16,4:42,'six':(5,12,8),'ten':['aaa','ball',34,01],'seven':'555','100':{1:10,2:20,'pop':5},'float':10.5}
lk=d.keys()
lv=d.values()

#sum of numbers only
print lk[2]+lv[1]+lv[2]+lv[3][2]+lv[3][3]+lv[4]+lv[5].keys()[0]+lv[5].keys()[1]+sum(lv[5].values())+sum(lv[6])

#sum of numers after converting few stings into numbers( Just in case :-))
print lk[2]+lv[1]+lv[2]+lv[3][2]+lv[3][3]+lv[4]+lv[5].keys()[0]+lv[5].keys()[1]+sum(lv[5].values())+sum(lv[6])+int(lk[5])+int(lv[0])+int(d['seven'])