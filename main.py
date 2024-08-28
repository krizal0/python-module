# # thisdict = {
# #   "brand": "Ford",
# #   "model": "Mustang",
# #   "year": 1964
# # }
# # thisdict.pop("model")
# # print(thisdict)

# # mylist=["a","b","c","d"]
# # otherlist=["f","g","h"]
# # mylist.append("e")
# # otherlist.insert(3,"i")
# # x=slice(1,3)
# # mylist.extend(otherlist)
# # print(mylist[x])

# # for i in range(0, 11):
# #     if i==0: pass
# #     print(i)

# # import datetime

# # x = datetime.datetime.now()
# # print(x)

# # all even numbers

# for x in intList:
#     if(x%2 == 0 ):
#         list.append(x)   
# print(list)
# list.clear()


# # all odd numbers

# for x in intList:
#     if(x%2 != 0 ):
#         list.append(x)   
# print(list)
# list.clear()\

# # all prime numbers

# for x in intList:
#     sum = 0
#     for n in range(1,x+1):
#         if(x%n == 0):
#             sum+=1
#     if(sum==2):
#         list.append(x)
# print(list)
# list.clear()

# f = open("myfile.txt", "r+")

# f.write("Hello everyone. My name is krijal dhakal.\n")
# f.write("Now the file has more content!")

# print(f.readline())
# print(f.readline())

# f.close()

# f = open("notmyfile.txt", "w")
# f.close()

# import os
# os.remove("notmyfile.txt")

# class filehandling:
#     def __init__(self, write, read, delete):
#         self.write = write
#         self.read = read
#         self.delete = delete

# f = filehandling("krijal", 20)

# print(f.write)
# print(f.read)
# print(f.delete)

# import csv
# with open('myfile.csv', 'w', newline='') as file:
#     csv_writer = csv.writer(file)

#     csv_writer.writerow(["Header1", "Header2"])
#     csv_writer.writerow(["1", "4"])
#     csv_writer.writerow(["2", "5"])
#     csv_writer.writerow(["3", "6"])

# import csv

# with open('myfile.tsv', 'wt') as out_file:
#     tsv_writer = csv.writer(out_file, delimiter='\t')
#     tsv_writer.writerow(["Header1", "Header2"])
#     tsv_writer.writerow(["1", "4"])
#     tsv_writer.writerow(["2", "5"])
#     tsv_writer.writerow(["3", "6"])

# class A:
  
#   def __init__(self, name, id):
#     self.name = name
#     self.id = id

#   def Display(self):
#     print(self.name, self.id)

# class B:
  
#   def __init__(self, name, id):
#     self.name = name
#     self.id = id

# def Display(self):
#     print(self.name, self.id)




    
    