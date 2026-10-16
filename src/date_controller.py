import dateutil

class DateController:

    @staticmethod
    def format_date(date):
        """
        Format a date string to be standardised

        Args:
            date (string): A string that is a date

        Returns:
            String: The date given formated to day month year
        """
        try:
            formated_date = dateutil.parser.parse(date, dayfirst=True)

        except dateutil.parser._parser.ParserError:
            print(dateutil.parser._parser.ParserError())
            return None

        return formated_date.strftime("%d %b %Y")

    @staticmethod
    def parse(date_string):
        """
        Format a string to be a date

        Args:
            date_string (string): A string that is a date

        Returns:
            Date: The date given formated to day month year
        """
        converted_date = dateutil.parser.parse(date_string, dayfirst=True)
        return converted_date.date()