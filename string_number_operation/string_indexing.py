county = "Bangladesh" #posite indexing
print(county[0])


county = "Bangladesh"
print(county[- 1]) #Nagative indexing

#------------strint splicing---------

county = "Ashik Ikbal Akash"
print(county [2:8])
print(county[2:])

country = "Bangladeshi"
print(country[2:4])

#------------String concanation-----------

firstName = "Ashik"
lastName  = "Akash"
fullName  = firstName +" "+ lastName
print(fullName)

#-----------string repitation--------

fullName = fullName *100
print(fullName)


#---------string formation---------
fname = "Ashik"
lname = "Akash"
age = 27
fullName = "My name is {} {} and my age is {}. I am a python developer" .format(fname,lname,age)
print(fullName)


#----------Another way for formateing and smart way
fname = "Ashik"
lname = "Akash"
age = 27
fullName = f"My name is {fname} {lname} and my age is {age}. I am a python developer" # f means formating.
print(fullName)