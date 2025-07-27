stock_prices=[('apple',200),('goog',400),('msft',100)]
for item in stock_prices:
    print(item)

for ticker,price in stock_prices:
    print(price+(0.1*price))

work_hours=[('abby',1000),('billy',400),('cassie',800)]
def employee_check(work_hours):
    current_max=0
    employee_of_month=''
    for employee,hours in work_hours:
        if hours>current_max:
            current_max=hours
            employee_of_month=employee
        else:
            pass
    return(employee_of_month,current_max)
print(employee_check(work_hours))


work_hours=[('Rohan',30000),('pratik',400),('yash',500),('omkar',2000)]
def work(work_hours):
    currentmax=0
    employeename=''

    for employee,hours in work_hours:
        if hours>currentmax:
            currentmax=hours
            employeename=employee
        else:
            pass

    return (employeename,currentmax)
print(work(work_hours))





























































































































































































































