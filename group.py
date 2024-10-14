"""An example of how to represent a group of acquaintances in Python."""

# Your code to go here...

my_group ={'name':['Jill','Zalika','John','Nash'],
           'age':['26','28','27','34'],
           'job':['biologist','artist','writer','chef'],
           'relationship':{'Jill':[None,'friend','partner',None],
                           'Zalika':['friend',None,None,'tenant'],
                           'John':['partner',None,None,'cousin'],
                           'Nash':[None,'landlord','cousin',None]}}
print(my_group)
print(my_group['age'][1])
result=my_group['name'][0]+' is '+my_group['age'][0]+','+my_group['job'][0]
print(result)
for i in my_group['relationship']:
    
    for j in my_group['relationship'][i]:
        if j==None:
            print('They have no relationship')
        else:
            print(j)
        




