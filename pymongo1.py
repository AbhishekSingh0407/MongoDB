import pymongo
# from pymongo import MongoClient

client = pymongo.MongoClient("mongodb://localhost:27017")

#protocol #ip add #portnumber

mydb = client['Employee']  #check whether db created or not in MongoCompass, not reflected until  a collection is created

information = mydb.employeeinformation

# record = {"fname": "Abhishek",
#            "lname":"Singh",
#              "department" :"informatik",
#               "degree":"masters"}

# information.insert_one(record)

# record = [
#             {
#                 "fname": "Abhishek",
#                 "lname":"Singh",
#                 "department" :"informatik",
#                 "degree":"masters"
#             },
#             {
#                 "fname": "Vikrant",
#                 "lname":"Agaskar",
#                 "department" :"informatik",
#                 "degree":"masters",
#             },
#             {
#                  "fname": "Shilpa",
#                 "lname":"Wade",
#                 "department" :"informatik",
#                 "degree":"masters"
#             }]
# information.insert_many(record)

# # select * from employeeinformation
# for record in information.find():
#     print(record)

# # where condition
# for record in information.find({'fname':'Abhishek'}):
#     print(record)

# # query documents using operators ($in, $lt,$gt)
# for record in information.find({'degree':{'$in':['phd','masters']}}):
#     print(record)

#below not working ??
# for record in information.find({'degree':{'$in':['phd','masters']},'age':{'$lt':32}}):
#     print(record)   

# # OR operation
# for record in information.find({'$or':[{'fname':'Shilpa'},{'degree':'phd'}]}):
#     print(record)

