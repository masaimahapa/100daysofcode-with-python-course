NAMES = ['arnold schwarzenegger', 'alec baldwin', 'bob belderbos',
         'julian sequeira', 'sandra bullock', 'keanu reeves',
         'julbob pybites', 'bob belderbos', 'julian sequeira',
         'al pacino', 'brad pitt', 'matt damon', 'brad pitt']


def dedup_and_title_case_names(names):
    """Should return a list of names, each name appears only once"""
    new_names=[]
    titled_names= [name.title() for name in names ]
    for each in titled_names:
        if each not in new_names:
            new_names.append(each)
    return new_names

def split_full_name(name):
    first, last= name.split()
    return last +' '+ first


def sort_by_surname_desc(names):
    """Returns names list sorted desc by surname"""
    names = dedup_and_title_case_names(names)
    surname_first= [split_full_name(name) for name in names]
    
    return sorted(surname_first, reverse= True)
  


def shortest_first_name(names):
    """Returns the shortest first name (str).
       You can assume there is only one shortest name.
    """
    names = dedup_and_title_case_names(names)
    names_only= [name.split()[0] for name in names]

    shortest=names_only[0]
    for each in names_only:
        if len(each)< len(shortest):
            shortest= each
    return shortest

    



print(shortest_first_name(NAMES))

print(sort_by_surname_desc(NAMES))