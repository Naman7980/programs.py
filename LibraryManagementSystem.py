class library:

   def __init__(self):
     
      self.books = []
      self.no_of_books = 0
    
   def Display_books(self):
      if not self.books:
        print("No books are currently avalable")
    
      else:
        print(f"The library has {self.no_of_books} books. The books are:")     
        for idx, book in enumerate(self.books, start=1):
                print(f"{idx}. {book}")
                
   def Add_Books(self, book):
      self.books.append(book) 
      self.no_of_books = len(self.books)
      print(f"✔️'{book}' has been added to the library.")             
       
my_library = library()       
                
my_library.Add_Books("ganga") 
my_library.Add_Books("mahabharat")
my_library.Add_Books("ramayan")  

my_library.Display_books()               
   
   