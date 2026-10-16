import dateutil

def format_date(date):
    """
    Format a date string to be standardised

    Args:
        date (string): A string that is a date

    Returns:
        String: The date given formated to day month year
    """
    formated_date = parse(date)
    if formated_date is None:
        return None

    return formated_date.strftime("%d %b %Y")


def parse(date_string):
    """
    Format a string to be a date

    Args:
        date_string (string): A string that is a date

    Returns:
        Date: The date given formated to day month year
    """
    try:
        converted_date = dateutil.parser.parse(date_string, dayfirst=True)
        return converted_date.date()

    except dateutil.parser._parser.ParserError:
        print("Failed to format date")
        return None



def before_today(date_string, today_date = dateutil.utils.today()):
    """
    Compares a given date to today

    Args:
        date_string (string): A string that is a date
        today_date (Datetime): Date that would be considered today

    Returns:
        Bool: True or False
    """
    today_int = int(today_date.strftime("%Y%m%d"))
    date = parse(date_string)
    if date is None:
        return None
    else :
        date_int = int(date.strftime("%Y%m%d"))

    if date_int < today_int:
        return True
    else:
        return False