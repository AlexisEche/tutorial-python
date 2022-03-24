def divisors(num):
    divisors = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisors.append(i)
    return divisors


def main():
  while True: 
      num=input("Introduce un número: ")
      
      assert num.isnumeric() and (int(num) > 0) , "No se puede introducir un char or negative"

      print(divisors(int(num))) 
      return divisors(int(num))
 
if __name__ == '__main__':
  main()