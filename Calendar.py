import calendar

class tkinter_calendar():
    def __init__(self):

        c = calendar.TextCalendar()
        m = c.prmonth(2021, 2)
        print(m)


    def print_year(self):
        print(calendar.calendar(2021))



if __name__ == '__main__':

    print(1234)