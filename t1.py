
from main import check_date
import datetime

current_date = str(datetime.date.today())

if __name__ == "__main__":
    print(check_date(current_date))
    