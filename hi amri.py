class CalUtils :
   def __init__(self):
       self.names = []
       self.heights = []
       self.totalstudentcount = 0
       self.totalstudentheight = 0

   def new_line(self):
       with open ("text.txt","r") as f:
           for line in f:
               f = line.split("\t")
               nameofppl = f[0]
               heightofppl = f[1]
               self.names.append(nameofppl)
               self.heights.append(float(heightofppl))
           print(self.names)
           self.adding()

   def list(self):
       print(self.names)
       print(self.heights)
       print(self.totalstudentcount)
       print(self.totalstudentheight)

   def calAvgHeight(self):
       self.totalstudentcount = (len(self.names))
       self.totalstudentheight = (sum(self.heights))
       average = round((self.totalstudentheight/self.totalstudentcount),2)
       print(f"Student average height is {average}m for {self.totalstudentcount} students.")
   def clear(self):
       self.names.clear()
       self.heights.clear()
       self.totalstudentcount = 0
       self.totalstudentheight = 0

   def adding(self):
        A = str(input("Add in a new student? (y/n):"))
        if A == "y":
            New_name = input("Enter the new student's name:").upper()
            New_height = input("Enter the new Student's height in meters:")
            float(New_height)
            with open("text.txt", 'a') as f:
                f.write(f"\n{New_name}\t{New_height}")
            self.clear()
            self.new_line()
            self.calAvgHeight()
            self.adding()

        elif A == 'n':
            self.list()
            self.calAvgHeight()
            exit()


        else:
            print("Please Enter Either (y/n)")


x = CalUtils()
x.new_line()



