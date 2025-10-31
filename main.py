import random


print("Hi there!")
print("I've generated a random 4 digit number for you.")
print("No one number starts with zero.")
print("There are no duplicities in the secret number.")
print("BUll/Bulls: There is correct number on correct possition.")
print("Cow/Cows: There is correct number on incorrect possition.")
print("Let's play a bulls and cows game.")

def generate_secret_number() -> str:
  # vygeneruje náhodné tajné čtyř-místné číslo
  while True:
    digits = list(range(10))
    random.shuffle(digits)
    # zvolíme první čtyři náhodné číslice
    secret_list =[str(d) for d in digits[:4]]

    # provedeme kontrolu, že číslo nemá 0 na začátku
    if secret_list[0] != '0':
      return "".join(secret_list)

def validate_guess(guess: str) -> tuple[bool, str]:
  # provedeme kontrolu, že číslo hráče splňuje pravdila
  if len(guess) != 4:
    return False, "The tip must consist of only four numbers."
  if not guess.isdigit():
    return False, "The tip must contain only numbers."
  if guess[0] == '0':
    return False, "The tip cannot start with zero"
  if len(set(guess)) != 4:
    return False, "The tip must not repeat any of the digits."
  return True, ""

def get_correct_form(count: int, single: str, plural: str) -> str:
  # bude vrácen korektní tvar ('bull', 'bulls', 'cow', 'cows')
  return f"{count} {single if count == 1 else plural}"

def get_bulls_and_cows(secret: str, guess: str) -> tuple[int,  int]:
  # provede výpočet bulls a cows pro dané číslo
  bulls = 0
  cows = 0

  for index in range(4):
    if guess[index] == secret[index]:
      bulls += 1
    elif guess[index] in secret:
      cows += 1

  return bulls, cows

def maine_game_circle(secret_number: str) -> int:
  attempts = 0

  while True:
      guess = input("Put your own tip(4 numbers):")
      is_valid, message = validate_guess(guess)
      if not is_valid:
        print(f"Incorrect tip! Try it again!")
        continue

      attempts += 1

      if guess == secret_number:
        return attempts

      bulls, cows = get_bulls_and_cows(secret_number, guess)

      bulls_out = get_correct_form(bulls, "bull", "bulls")
      cows_out = get_correct_form(cows, "cow", "cows")

      print(f"Result: {bulls_out} and {cows_out}.")
      print("-")

def main() -> None:
  # print_intro()
  secret = generate_secret_number()

  final_attempts = maine_game_circle(secret)

  print("Congratulations!!!")
  print(f"You guessed the secret number. {secret}!")
  print(f"It took you {final_attempts} attempts to do it..")

if __name__ == "__main__":
    main()
