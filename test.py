
#Here is a little ugly way to achieve what you want.

#code:

users = [
        (0, "Bob", "Paris", "password"),
        (1, "Jack", "Berlin", "python"),
        (2, "Jenna", "London" ,"overflow"),
        (3, "Eva", "Stockholm" ,"1234")
    ]
office_employees = ["id","Name","key"]
ans = {}
for user in users:
    ans[user[2]]={office_employees[0]:user[0],office_employees[1]:user[1],office_employees[2]:user[3]}
print(ans)
