#Version: 1.0.0
#Date: 23.11.2023
#Author: Sowtyy


#ALPHABET = "abcdefghijklmnopqrstuvwxyz"
#ALPHABET = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
ALPHABET = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
ALPHABET_LEN = len(ALPHABET)
AVAILABLE_MODES = ["encode", "decode"]
DEFAULT_OFFSET = 0


def askInput(output : str = "", *, required : list = [], allowEmpty : bool = False):
  inp = ""
  
  while True:
    inp = input(output)
    
    if not allowEmpty and not inp:
      continue

    if not required:
      break
    if inp in required:
      break

  return inp

def askInputSelect(output : str = "", *, required : list):
  inp = ""

  requiredNumsStr = [str(i + 1) for i in range(len(required))]

  while inp not in requiredNumsStr:
    inp = askInput(output)
  
  return required[int(inp) - 1]

def askInputInt(output : str = "", *, allowEmpty : bool = False):
  inp = ""
  inpInt = 0

  while True:
    inp = askInput(output, allowEmpty = allowEmpty)

    if not allowEmpty:
      try:
        inpInt = int(inp)
      except TypeError:
        continue

    break

  return inpInt

def translateMessage(key : str, message : str, mode : str, offset : int = 0):
  translated = []
  keyIndex = 0
  key = key.upper()

  for symbol in message:
    num = ALPHABET.find(symbol.upper())

    if num == -1:
      translated.append(symbol)
      continue

    if mode == "encode":
      num += ALPHABET.find(key[keyIndex]) + offset
    elif mode == "decode":
      num -= ALPHABET.find(key[keyIndex]) - offset
    
    num %= ALPHABET_LEN

    if symbol.isupper():
      translated.append(ALPHABET[num].upper())
    elif symbol.islower():
      translated.append(ALPHABET[num].lower())
    
    keyIndex += 1
    if keyIndex == len(key):
      keyIndex = 0
  
  return "".join(translated)

def main():
  mode = askInputSelect(f"Выберете режим ({' / '.join(f'{i + 1} - {mode}' for i, mode in enumerate(AVAILABLE_MODES))}): ", required = AVAILABLE_MODES) # encode | decode
  text = askInput("Введите текст: ")
  key = askInput("Введите ключ: ")
  offset = askInputInt(f"Введите смещение (по умолчанию {DEFAULT_OFFSET}): ", allowEmpty = True)

  result = translateMessage(key, text, mode, offset)
  
  print(f"Результат: {result}")

  return

if __name__ == "__main__":
  main()
