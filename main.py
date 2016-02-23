print('Hello Python')

height = 10
base = 2
area = height*base/2
print "Area is", area

def calculate_triangle(height,base):
    return height*base/2
result1=calculate_triangle(10,2)
result2=calculate_triangle(30,5)
result3=calculate_triangle(15,2)
print"Result 1 = ", result1
print"Result 2 = ", result2
print"Result 3 = ", result3

class Math:
   def calculate_triangle(self, height, base):
      return height * base / 2
triangle1 = Math()
triangle2 = Math()
triangle3 = Math()
result1 = triangle1.calculate_triangle(10,2)
result2 = triangle2.calculate_triangle(30,5)
result3 = triangle3.calculate_triangle(15,2)
print "Triangle 1 = ", result1
print "Triangle 2 = ", result2
print "Triangle 3 = ", result3


