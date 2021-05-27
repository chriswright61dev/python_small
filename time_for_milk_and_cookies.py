import datetime
def time_for_milk_and_cookies(date):
    if date.month == 12 and date.day == 24:
        return True
    else:
        return False

# return (date.day==24 and date.month==11)

time_for_milk_and_cookies(datetime.date(2013, 12, 24))
