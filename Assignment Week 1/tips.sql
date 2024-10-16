Q1: User activity past 30 days
hint 1: remember how we group the data of employee by their department during the demo?
hint 2: use one of the learnt aggregate function
hint 3: for example if you want to see if the data is before '2024-10-13' you can put it like this: `WHERE activity_date < '2024-10-13'`
hint 4: if looking for the date 30 days ago is too  much, just use hardcoded date like for example 'xxxx-xx-xx', otherwise, take a look at other syntax such as `DATE_SUB` and `INTERVAL`

Q2: Number of employees which report to the employee
hint 1: Join can be done to the same table as well
hint 2: you can use aggregate function on an aggregate function, for example round(avg(age))
hint 3: you can do multiple group by too

Q3: Monthly transactions
hint 1: remember how we group the data of employee by their department during the demo?, now you can group by the aggregate as well
hint 2: find out about if else condition in SQL
hint 3: find out about date_format syntax in SQL
