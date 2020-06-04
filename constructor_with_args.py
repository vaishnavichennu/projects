class Bank:
 def __init__(self,accNo,bal):
  self.accNo=accNo;
  self.bal=bal;
 def show(self):
  print("account no=",self.accNo);
  print("balnce=",self.bal);
vaishnavi=Bank(2345677788876,200000);
vaishnavi.show();
priya=Bank(1224557895,300000);
priya.show();