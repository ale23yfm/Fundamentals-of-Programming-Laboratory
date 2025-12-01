#
# User interface section
#

from functions import add_phone, find_by_manufacturer, increase_price, increase_by_percent

def menu(phones):
  print("Welcome to the menu!")
  while True:
      print("\nChoose one option:")
      print("1. Add a phone")
      print("2. Find all phones from a given manufacturer")
      print("3. Increase the price of a phone")
      print("4. Increase the price of all phones")
      print("5. Exit")

      try:
          o=int(input("Your choice from 1-5:"))
      except ValueError:
          print("You should choose a number between 1-5. Try again.")
          continue

      if o == 1:
          try:
              manufacturer = input("Type the manufacturer:")
              model = input("Type the model:")
              price = int(input("Type the price:"))
              add_phone(phones, manufacturer, model, price)
          except Exception as e:
              print("\nError:", e)

          print("\nThose are the phones:")
          for p in phones:
              print (p)

      if o == 2:
          manufacturer = input("Type the manufacturer:")
          result, cnt = find_by_manufacturer(phones, manufacturer, 0)

          if cnt == 0:
              print("\nThere are no phones to display.")
          else:
              print("\nThose are the phones:")
              for p in result:
                  print(p)

      if o == 3:
          print ("Please complete the details to increase the price of a phone:")
          manufacturer = input("Type the manufacturer:")
          model = input("Type the model:")
          amount = int(input("Type the amount to be added to the price:"))
          phones, cnt = increase_price(phones, manufacturer, model, amount, 0)

          if cnt == 0:
              print("\nThere is no phone with the given details.")
          else:
              print("\nThose are the phones:")
              for p in phones:
                  print(p)

      if o == 4:
          percent = int(input("Type the amount to be added to the price:"))
          if percent < -50 or percent > 100:
              print("\nThe percent should be between -50 and 100. Please try again.")
              continue

          phones = increase_by_percent(phones, percent)

          print("\nThose are the phones:")
          for p in phones:
              print(p)

      if o == 5:
          print("Thanks for playing!")
          exit()

if __name__ == "__main__":
    #hard coded
    phones = [{"manufacturer": "Samsung", "model": "Galaxy S25", "price": 3000},
              {"manufacturer": "IPhone", "model": "14 Pro", "price": 4500},
              {"manufacturer": "Huawei", "model": "Nova9", "price": 2500},
              {"manufacturer": "Iphone", "model": "15 Pro Max", "price": 3000},]
    menu(phones)