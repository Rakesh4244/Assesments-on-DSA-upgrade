def fun():
    print("hello")
    return
fun()
def fun(a):
    print("hello",a)
    return
fun('king')

def fun(a,b):
    return a + b
print(fun(3,5))
#when func declared in class it be a method ---method cant call like a func we have to create a obj to it
class Test:
    
    def show(self):
        
        print("Method")
ob = Test()
ob.show()

class Test:
    def __init__(self,value):   #constructor to create data members
        self.a = value
    def display(self):
        print("Method value",self.a)
obj = Test(input("Enter value:"))
obj.display()
#in python no pointers---we use concept in linket list by method and classes
        
class MovieNode:
    def __init__(self,moviename,releaseDate):
        self.moviename = moviename
        self.releaseDate = releaseDate
        self.next = None
        return
class NetflixMovieList:
     
    def __init__(self):   #head data memeber which is null initial
        self.head = None

        
    def addmoviename(self,moviename,releaseDate):   # we are appending the movies
        new_movie = MovieNode(moviename,releaseDate)
        
        if self.head == None:
             self.head = new_movie   # making the new movie at begining at head
             return
          

        
          
          new_movie.next = self.head  
          self.head = new_movie
          return
     
    
          
     def display(self):
          if self.head == None:
               print("No movies ")
               return
          temp = self.head

          while(temp != None):
               print(temp.movname,temp.releaseDate)
               temp=temp.next

     def delete(self):
          temp = self.head
          while(temp.next == None):
               temp.remove()
movieobj = MovieNode          
movieobj = NetflixMovieList()
movieobj.addmoviename('kingsMen','20-12-2222')
movieobj.addmoviename('Kingsmen2','23-3-2223')
movieobj.display()
          
          
          
        
