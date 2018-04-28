import pandas as pd
from pandas.tseries.offsets import *
from pandas.tseries.offsets import CustomBusinessDay



class Calendar(object):

    def __init__(self,start_date,end_date):
        self.start_date = start_date
        self.end_date = end_date

    def calculateworkingdaysISO(self):
        holidays = ['2018-01-01','2018-04-23','2018-05-01','2018-05-19','2018-06-14','2018-06-15','2018-06-16','2018-06-17',
                    '2018-07-15','2018-07-20','2018-07-21','2018-07-22','2018-07-23','2018-07-24','2018-07-30','2018-10-29','2018-12-31']
        customdays = CustomBusinessDay(holidays=holidays)
        calculated_ISO = pd.date_range(self.start_date, self.end_date,freq=customdays)
        print("**********ISO Calendar************")
        print(calculated_ISO)
        print("Workdays in ISO Calendar:", calculated_ISO.size)

    def countworkingdaysISO(self):
        count = pd.Series(index=pd.date_range(self.start_date, self.end_date,freq=BDay()))

        count_month = count.resample('M').size().rename_axis('Month').reset_index(name='NumDays')
        count_year = count.resample('Y').size().rename_axis('Month').reset_index(name='NumDays')
        count_month['Month'] = count_month['Month'].dt.to_period('m')
        #count_month['Month'] = count_month['Month'].dt.month
        count_year['Month'] = count_year['Month'].dt.to_period('M')
        print(count_month)
        print(count_year)

    def countcustomworkingdays(self):
        half_day=0.5
        holidays = ['2018-01-01','2018-04-23','2018-05-01','2018-05-19','2018-06-14','2018-06-15','2018-06-16','2018-06-17',
                    '2018-07-15','2018-07-20','2018-07-21','2018-07-22','2018-07-23','2018-07-24','2018-07-30','2018-10-29','2018-12-31']

        customdays = CustomBusinessDay(holidays=holidays)

        count_customdays = pd.Series(index=pd.date_range(self.start_date, self.end_date, freq=customdays))
        count_month_custom = count_customdays.resample('M').size().rename_axis('Month').reset_index(name='NumDays')
        count_year_custom = count_customdays.resample('Y').size().rename_axis('Month').reset_index(name='NumDays')
        count_month_custom['Month'] = count_month_custom['Month'].dt.to_period('m')
        #count_month['Month'] = count_month['Month'].dt.month
        count_year_custom['Month'] = count_year_custom['Month'].dt.to_period('M')

        print("**********Custom Calendar************")
        print(count_month_custom)
        print(count_year_custom)

    def calculatedworkingdaysArabic(self):
        self.custom_workdays = "Sun Mon Tue Wed Thu"
        calculated_arabic = pd.bdate_range(self.start_date, self.end_date, freq='C', weekmask=self.custom_workdays)
        print("**********Arabic Calendar************")
        print(calculated_arabic)
        print("Workdays in Arabic Calendar:", calculated_arabic.size)


def main():
    result_ISO = Calendar('2018-01-01','2018-12-31')
    result_ISO.calculateworkingdaysISO()

    result_countworkingdaysISO = Calendar('2018-01-01','2019-12-31')
    result_countworkingdaysISO.countworkingdaysISO()

    result_count_customdays = Calendar('2018-01-01','2019-12-31')
    result_count_customdays.countcustomworkingdays()

    result_Arabic = Calendar('2018-02-01','2019-03-31')
    result_Arabic.calculatedworkingdaysArabic()


if __name__ == "__main__":
    main()