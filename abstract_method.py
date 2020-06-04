from abc import *
class Apartment:
 def apartment_name(self):
  print("MY HOME apartment visitors details:")
 @abstractmethod
 def entry_time(self):pass
 @abstractmethod
 def exit_time(self):pass
 
class visitor1(Apartment):
 def entry_time(self):
  print("flat no:111")
  print("entered time is 10:05am")
 def exit_time(self):
  print("exit time is 3:44pm")
  
  
class visitor2(Apartment):
 def entry_time(self):
  print("flat no:131")
  print("entered time is 4:88pm")
 def exit_time(self):
  print("exit time is 9:44pm")
  
a=visitor1()
a.apartment_name()
a.entry_time()
a.exit_time()


b=visitor2()
b.entry_time()
b.exit_time()