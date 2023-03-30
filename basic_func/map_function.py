def add_two(num):
    return num +2 

def sharmis_map(func,itrables): #add_two [5,7,2]
    #new_itrables = []
    # for itrable in itrables:
    #     new_itrables.append(func(itrable))
    # return new_itrables
    return list(func(itrable) for itrable in itrables) 

#map_func doesn't return a list,only return map object,so list(map_object)
    

print(sharmis_map(add_two,[5,7,2]))

