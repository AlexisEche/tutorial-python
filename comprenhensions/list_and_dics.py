from functools import reduce

def main():
  my_list = [1,4,5,6,9,13,19,21]
  my_list_even = list(filter(lambda x: (x%2 != 0) ,my_list))
  my_list_square = list(map(lambda x: x**2 ,my_list))
  my_list_reduce = reduce(lambda x,y : x*y ,my_list)

  print(my_list_even)
  print(my_list_square)
  print(my_list_reduce)

  
if __name__ == '__main__':
  main()