#Version: 1.1.0
#Date: 23.11.2023
#Author: Sowtyy


#ALPHABET = "abcdefghijklmnopqrstuvwxyz"
#ALPHABET = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
ALPHABET = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
ALPHABET_LEN = len(ALPHABET)
AVAILABLE_MODES = ["зашифровать", "расшифровать"]
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

    try:
      inpInt = int(inp)
    except Exception:
      if not allowEmpty:
        continue

    break

  return inpInt

def translateText(key : str, text : str, mode : str, offset : int = 0):
  translated = ""
  keyIndex = 0
  key = key.upper()

  for symbol in text:
    num = ALPHABET.find(symbol.upper())

    if num == -1:
      translated += symbol
      continue

    if mode == "зашифровать":
      num += ALPHABET.find(key[keyIndex])
      num += offset
    elif mode == "расшифровать":
      num -= ALPHABET.find(key[keyIndex])
      num -= offset
    
    num %= ALPHABET_LEN

    if symbol.isupper():
      translated += ALPHABET[num].upper()
    elif symbol.islower():
      translated += ALPHABET[num].lower()
    
    keyIndex += 1
    if keyIndex == len(key):
      keyIndex = 0
  
  return translated

def main():
  while True:
    mode = askInputSelect(f"Выберите режим ({' / '.join(f'[{i + 1}] - {mode}' for i, mode in enumerate(AVAILABLE_MODES))}): ", required = AVAILABLE_MODES) # encode | decode
    text = askInput("Введите текст: ")
    key = askInput("Введите ключ: ")
    offset = askInputInt(f"Введите смещение (по умолчанию {DEFAULT_OFFSET}): ", allowEmpty = True) or DEFAULT_OFFSET

    result = translateText(key, text, mode, offset)
    
    print(f"\nРезультат: {result}\n")

  return

if __name__ == "__main__":
  main()
  input("\nНажмите Enter чтобы выйти...")
