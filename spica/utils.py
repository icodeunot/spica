import calendar

DAYS = ["M", "T", "W", "Th", "F", "Sa", "Su"]
MONTHS = ["JAN", "FEB", "MAR", "APR", "MAY", "JUN", 
          "JUL", "AUG", "SEP", "OCT", "NOV", "DEC"]

def date_days_mapping(year, month_num):
    """
    Returns a list of (day_number, weekday_abbr) for the given month.
    e.g.: [(1, "Th"), (2, "F")... (31, "Sa")]
    """
    first_day, num_days = calendar.monthrange(year, month_num) 
    # monthrange() returns 1st day of month (m-su as 0-6) and # of days in the month
    return [(day, DAYS[(first_day + day -1) % 7]) for day in range(1, num_days + 1)]

def month_mapping(year):
    """
    Returns a list of (month_abbr, list_of_day_mappings) for the full year
    e.g.: [("JAN", [(1, "M"), ...]), ("FEB", [...]), ...]
    """
    return [(MONTHS[i], date_days_mapping(year, i + 1)) for i in range(12)]