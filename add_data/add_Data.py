from pymongo import MongoClient
 
# connect to the MongoDB on MongoLab
# to learn more about MongoLab visit http://www.mongolab.com
# replace the "" in the line below with your MongoLab connection string
# you can also use a local MongoDB instance
connection = MongoClient("mongodb://localhost/indian_banks")
 
# connect to the students database and the ctec121 collection
db = connection.indian_banks.banks
 



import csv
with open('bank_branches.csv', 'rb') as csvfile:
   bankreader = csv.reader(csvfile, delimiter=',')
   count  = 0 
   bank_record = {}
   bank_record_name = {}
   for row in bankreader:
      #print row[1]
      bank_record = {
         'ifsc' : row[0],
         'bank_id' : row[1],
         'branch' : row[2],
         'address' : row[3],
         'city' : row[4],
         'district' : row[5],
         'state' : row[6],
         'bank_name' : row[7]
      }
      #bank_record_name[row[5]] = 1
      db.insert(bank_record)
      #print row[7]
      # if count == 25:
      #    break
      count = count+1
      print count
   #print bank_record_name
   print len(bank_record_name.keys())






# create a dictionary to hold student documents
 
# # create dictionary
# student_record = {}
 
# # set flag variable
# flag = True
 
# # loop for data input


# while (flag):
#    # ask for input
#    student_name,student_grade = input("Enter student name and grade: ").split(',')
#    # place values in dictionary
#    student_record = {'name':student_name,'grade':student_grade}
#    # insert the record
#    db.insert(student_record)
#    # should we continue?
#    flag = input('Enter another record? ')
#    if (flag[0].upper() == 'N'):
#       flag = False
 
# # find all documents
# results = db.find()
 
# print()
# print('+-+-+-+-+-+-+-+-+-+-+-+-+-+-')
 
# # display documents from collection
# for record in results:
# # print out the document
# print(record['name'] + ',',record['grade'])
 
# print()
 
# close the connection to MongoDB
connection.close()