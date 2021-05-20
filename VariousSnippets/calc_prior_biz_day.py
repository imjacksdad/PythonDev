import datetime
# BDay is business day, not birthday...
from pandas.tseries.offsets import BDay

today = datetime.datetime.today()
print(today - BDay(3))
