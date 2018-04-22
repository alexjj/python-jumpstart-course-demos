import datetime


def print_header():
    print('-' * 32)
    print('    Birthday App')
    print('-' * 32)
    print()


def get_birthday_from_user():
    print('When were you born?')
    user_year = int(input('What year were you born [YYYY]? '))
    user_month = int(input("What month were you born [MM]? "))
    user_day = int(input('What day were you born [DD]? '))
    print()

    birthday = datetime.date(user_year, user_month, user_day)
    return birthday

def compute_days_between_two_dates(original_date, target_date):
    this_year = datetime.date(target_date.year, original_date.month, original_date.day)
    dt = this_year - target_date
    return dt.days

def print_birthday_information(days):
    if days < 0:
        print('You had your birthday {} days ago this year'.format(-days))
    elif days > 0:
        print('You birthday is in {} days time'.format(days))
    else:
        print('Today is your birthday!')


def main():
    print_header()
    bday = get_birthday_from_user()
    today = datetime.date.today()
    number_of_days = compute_days_between_two_dates(bday, today)
    print_birthday_information(number_of_days)

main()