
class Rectange:
	def __init__(self,length ,width):
		self.length=length
		self.width=width		
	def set_l(self, length):
		self.length =length
	def set_w(self, width):
		self.width =width
	def get_l(self):	                           
		return self.length 
	def get_w(self):                        
		return self.width
	def area(self):	   
    		  p= self.get_w()*self.get_l()
    		  return p
     
   
    		
       
   	   
    		        
		

print("-------------------------------------------")
r=Rectange(2,2)


print ("AREA ")
print("The value of the rectangle area is %d"%(r.area()))



