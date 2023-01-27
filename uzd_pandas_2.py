import pandas as pd
population_dict = {'California': 38332521,
                   'Texas': 26448193,
                   'New York': 19651127,
                   'Florida': 19552860,
                   'Illinois': 12882135}

area_dict = {'California': 423967,
             'Texas': 695662,
             'New York': 141297,
             'Florida': 170312,
             'Illinois': 149995}
population = pd.Series(population_dict)
area = pd.Series(area_dict)
states = pd.DataFrame({'population': population, 'area' : area})
print(population)
print(area)
print(states)
 
ind = states.index
#print(ind)
col = states.columns
#print(col)
pop = states['population']
#print(pop)
val = states['area']['Texas']
#print(val)

states['density'] = states['area'] / states['population']
print(states)