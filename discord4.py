#make sure that when you define the function you state the same number of arguments when you return/call the function

def function(fruit):
  print(fruit + " juice")
function("orange", "apple")

#this will result in an error because we added 2 arguments when returning the function, however one argument when defining the function. To fix this, add another argumentin the defined function
