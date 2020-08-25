class Solution:
    def dayOfYear(self, date: str) -> int:
        day_of_month = [31,28,31,30,31,30,31,31,30,31,30,31]
        (year,month,day) = date.split("-")
        year = int(year)
        month = int(month)
        day = int(day)
        if month == 1:
            day_of_year = day

        if month == 2:
            day_of_year = 31 + day

        elif month > 2:
            day_of_year = sum(x for x in day_of_month[:month-1]) + day
            if ((year%4 == 0 and year%100 != 0) or year%400 == 0):
                day_of_year += 1
        return day_of_year