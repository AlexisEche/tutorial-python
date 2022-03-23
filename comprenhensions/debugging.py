def divisors(num):
    divisors = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisors.append(i)
    return divisors


def main():
  while True:
    try:
      num=int(input("Introduce un número: "))
      
      if(num < 0 ):
        raise ValueError
        break
      
      print(divisors(num))
      return divisors(num)

    except ValueError:
      print("No se puede introducir un numero negativo")

if __name__ == '__main__':
  main()