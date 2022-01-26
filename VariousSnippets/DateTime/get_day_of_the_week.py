import datetime

x = datetime.datetime.now()

print(x.strftime("%A"))
print(x.strftime("%a"))

if x.strftime("%a") == 'SAT':
    #do something.
    print('It''s Saturday')
else:
    #do something else
    print('it is not Saturday')
          
