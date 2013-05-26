"""
Project Eurler Problem 19
http://projecteuler.net/problem=19

Solving this the hard way (not using date/datetime from the standard library)
"""

MONTH_DAYS = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
DAY_NAMES = {1: 'Monday', 2: 'Tuesday', 3: 'Wednesday', 4: 'Thursday', 5: 'Friday', 6: 'Saturday', 7: 'Sunday'}


def is_leap_year(year):
    """
    Determines if a year is a leap year.
    A year is a leap year if it is divisible by 4,
    unless it is a century - then it is a leap year if divisible by 400
    """
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False


def days_in_month(month, year):
    """
    Determines the number of days in a month.
    Needs the year to figure out the number of days in February due to leap years.
    """
    if month == 2: # February needs leap year logic
        if is_leap_year(year):
            return 29
        else:
            return 28
    else:
        return MONTH_DAYS[month]


def days_delta(start_date, end_date):
    """
    Finds the number of days between two dates
    :rtype : int
    """
    number_days = 0
    for year in xrange(start_date.year, end_date.year + 1):
        end_month = 13
        if end_date.year == year:
            end_month = end_date.month + 1
        for month in xrange(1, end_month):
            if end_date.year == year and end_date.month == month and end_date.day:
                if end_date.day == start_date.day:
                    pass # Don't add any days
                else:
                    number_days += end_date.day
            else:
                number_days += days_in_month(month, year)
    return number_days


class Date(object):
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def day_of_week(self):
        #TODO: Is calculating the number of days since 1900-01-01 the best approach?
        return DAY_NAMES[(days_delta(Date(01, 01, 1900), self) % 7) + 1]

    def __repr__(self):
        return '{0:d}-{1:d}-{2:d}'.format(self.year, self.month, self.day)


def solve():
    number_sundays = 0
    for year in xrange(1901, 2001):
        for month in xrange(1, 13):
            date = Date(1, month, year) # First day of every month
            if 'Sunday' == date.day_of_week():
                number_sundays += 1
    return number_sundays


if __name__ == '__main__':
    print solve()
