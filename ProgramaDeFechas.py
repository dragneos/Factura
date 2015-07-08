__author__ = 'max'

from datetime import date,datetime,timedelta
new_format = "%Y-%m-%d"
def fecha_actual():
    return date

z = datetime.now().strftime('%Y-%m-%d')
if z == '2014-02-21':
    print("todo es posible")
t =timedelta(days=-1)
ayer  = datetime.now() +t
ayer = ayer.strftime('%Y-%m-%d')
print( ayer)
print(z)