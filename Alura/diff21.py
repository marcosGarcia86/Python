def diff21():
    if n > 21:
        return 2 * (abs(21 - n))
    elif n <= 21:
        return abs(21 - n)

def sleep():
    if not week:
            return True
    elif week and not holiday:
        return False
    else:
        return True

def nao_string(str):
    if len(str) >= 3 and str[:3] == 'not':
        return str
    return 'not ' + str

def monkey_trouble(a_smile, b_smile):
  if a_smile and b_smile:
      return True
  elif not a_smile and not b_smile:
      return True
  else:
      return False


def near_hundred(n):
    if n in range(abs(10, 100)) or n in range(abs(10, 200)):
        return True
    else:
        return False