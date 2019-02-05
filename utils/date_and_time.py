import datetime


class DateAndTime:

    @staticmethod
    def date_and_time():
        date_and_time = datetime.datetime.now()
        # formatted_date_and_time = date_and_time.strftime('%m/%d/%Y')

        return str(date_and_time)
