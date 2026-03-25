from copy import deepcopy
egg
class Grid:
    def __init__(self,width,height):
        """
        parameters: 
            width : int 
            height : int
        creates a grid object using the parameters: width, height
        Uses width and height to make an array, and stores it in 'array' attribute
        """
        self.width = width
        self.height = height
        self.array = [[None for x in range(width)] for y in range(height)]

    def in_bounds(self,x,y):
        """
        parameters: 
            x : int 
            y : int
        Checks to see if x and y are in bounds of the object's grid bounds
        return either true or false 
        handles negatives and out of range indexes
        """
        if x < self.width and y < self.height:
            if x >= 0 and y >= 0:
                return True
            else:
             
                return False
         
        else:
            return False
          
        
    def get(self,x,y):
        """
        parameters: 
            x : int 
            y : int
        checks if parameters x , y are in bounds (throws Index Error if False)
        gets the value at x , y of the object's array
        returns value at x , y
        """
        if(self.in_bounds(x,y)):
            return self.array[y][x]
        else:
            raise IndexError("Out of bounds")

    def set(self,x,y,val):
        """
        parameters: 
            x : int 
            y : int
            val : anyType (could be object, int, or string; depends on use)
        checks if parameters x , y are in bounds (throws Index Error if False)
        sets value at x , y = val (parameter)
        """
        if(self.in_bounds(x,y)):
            self.array[y][x] = val
        else:
            raise IndexError("Out of bounds")

    @staticmethod        
    def check_list_malformed(lst):
        """
        parameters: 
            lst : array
        Takes parameteer: lst and runs through 4 checks
            - is object a list -> if False, throws ValueError
            - is list empty -> if True, throws ValueError
            - is each item in list a list -> if False, throws ValueError
            - are all nested list lengths equal -> if False, throws ValueError

            if all True, function finishes and continues program
        """
        if(type(lst) != list):
            raise ValueError("Object is not a list!")
        try:
            if(lst[0] == None):
                raise ValueError("List is empty!")
        except:
            raise ValueError("List is empty!")
        
        validInList = 0
        for item in lst:
            if type(item) == list:
                validInList +=1
        if validInList != len(lst):
            raise ValueError("List is not full of lists!")
            
        lengthShouldBe = len(lst[0])
        validNestedLists = 0
        for item in lst:
            if(len(item) == lengthShouldBe):
                validNestedLists +=1
        if(validNestedLists != len(lst)):
            raise ValueError("Nested lists are not all the same size")
        
    @staticmethod        
    def build(lst):
        """
        parameters: 
            lst : array
        Takes lst parameter and runs check_list_malformed
        determines width and height from given lst
        creates new object using Grid class, using width and height
        copies list to object.array
        returns Grid object
        """
        Grid.check_list_malformed(lst)
        height = len(lst)
        width = len(lst[0])
        newGrid = Grid(width,height)
        newGrid.array = deepcopy(lst)
        return newGrid
        
    def copy(self):
        """
        returns a copy of object (self)
        """
        return deepcopy(self)
    
    def __eq__(self, other):
        """
        parameters: 
            other : list or object
        takes given object and 'other' parameter
        determines whether 'other' is list or object
        checks to see if self.list == other (or other.list)
        returns True or False
        """
        if(isinstance(other,Grid)):
            if(self.array == other.array):
                return self.array == other.array
        elif(type(other) == list):
            if(other == self.array):
                return True
        else:
            return False

    def __str__(self):
        """
        returns a string, containing object width, height, and array[0][0]
        ex "Grid(5, 5, first = None)"
        
        """
        return f"Grid({self.width}, {self.height}, first = {self.array[0][0]})"
    
    def __repr__(self):
        """
        returns a string, containing the array of object
        ex "Grid.build([[2,2][2,2]])
        """
        return f"Grid.build({self.array})"

    