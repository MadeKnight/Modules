year = 0

def _is_not_leap(yera: int) -> bool:
  return not (year % 400 == 0 or year % 100 != 0 and year % 4 == 0)


def check_date(full_date: str) -> bool:
  year, month, day = (int(item) for item in full_date.split("-"))
  print(f"День: {day}, Месяц: {month}, Год: {year}")
  if year < 1 or year > 9999 or month < 1 or month > 12 or day < 1 or day > 31:
    return False
  if month in (4, 6, 9, 11) and day > 30:
    return False
  elif month == 2 and day > 29:
    return False
  elif month == 2 and day > 28 and _is_not_leap(year):
    return False
  else:
    return True
