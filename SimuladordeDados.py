import random

def lancar_dados():
   cont = 0  
   while True:
      dado1 = [random.randint(1,6)]
      dado2 = [random.randint(1,6)]
      cont += 1
      if dado1 == dado2:
          return cont

if __name__ == "__main__":
   print(lancar_dados())