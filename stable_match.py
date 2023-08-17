men_preferences = {
 'A': ['V', 'W', 'X'],
 'B': ['W', 'V', 'X'],
 'C': ['V', 'W', 'X']
}
# Women's preference list
women_preferences = {
 'V': ['A', 'B', 'C'],
 'W': ['B', 'C', 'A'],
 'X': ['C', 'A', 'B']
}

def stable_match(men_preferences,women_preferences):

    free_men = list(men_preferences.keys())
    engaged = {}

    while free_men:
        man = free_men[0]
        woman = men_preferences[man][0]

        if woman not in engaged:
            engaged[woman]=man
            free_men.remove(man)
        else:
            men1 = engaged[woman]
            if(women_preferences[woman].index(man)<women_preferences[woman].index(men1)):
                engaged[woman] = man
                free_men.append(men1)
            else:
                men_preferences[man].remove(woman)
    
    return engaged

couple = stable_match(men_preferences,women_preferences)

for x,y in couple.items():
    print(f"{x} women with {y} men")

