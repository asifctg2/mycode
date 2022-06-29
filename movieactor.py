#!/usr/bin/env python3                                                       
def getList(Adam_Sandler):
    return [*Adam_Sandler]   
Adam_Sandler = {"Birth_Year": "1966", "Birth_city": "Brooklyn", "Alma Mater": "New_York_University", "Occupation": "Actor"}

new_key_values_dict = {'Spouse':'Jackie Titone'}
Adam_Sandler.update(new_key_values_dict)
print(Adam_Sandler)

print(getList(Adam_Sandler))
