#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


pokemon_data = pd.read_csv('PokemonStats.csv', index_col = 0)


# In[3]:


pokemon_data.head()


# In[4]:


def type_sorting(pokedex_number_start, ID):
    while pokedex_number_start <= ID:
        if pokemon_data[(pokemon_data['Type1'] == 'Normal') | (pokemon_data['Type2'] == 'Normal')].any:
            normal = normal.append()
        pokedex_number_start += 1


# In[5]:


def type_sorting2(pokedex_number_start, index):
    while pokedex_number_start <= index:
        for pokemon, row in pokemon_data.iterrows():
            if row['Type1'] == 'Normal' or row['Type2'] == 'Normal':
                normal[pokemon] = row['Name']
            elif row['Type1'] == 'Fire' or row['Type2'] == 'Fire':
                fire[pokemon] = row['Name']
            elif row['Type1'] == 'Water' or row['Type2'] == 'Water':
                water[pokemon] = row['Name']
            elif row['Type1'] == 'Grass' or row['Type2'] == 'Grass':
                grass[pokemon] = row['Name']
            elif row['Type1'] == 'Flying' or row['Type2'] == 'Flying':
                flying[pokemon] = row['Name']
            elif row['Type1'] == 'Fighting' or row['Type2'] == 'Fighting':
                fighting[pokemon] = row['Name']
            elif row['Type1'] == 'Poison' or row['Type2'] == 'Poison':
                poison[pokemon] = row['Name']
            elif row['Type1'] == 'Electric' or row['Type2'] == 'Electric':
                electric[pokemon] = row['Name']
            elif row['Type1'] == 'Ground' or row['Type2'] == 'Ground':
                ground[pokemon] = row['Name']
            elif row['Type1'] == 'Rock' or row['Type2'] == 'Rock':
                rock[pokemon] = row['Name']
            elif row['Type1'] == 'Psychic' or row['Type2'] == 'Psychic':
                psychic[pokemon] = row['Name']
            elif row['Type1'] == 'Ice' or row['Type2'] == 'Ice':
                ice[pokemon] = row['Name']
            elif row['Type1'] == 'Bug' or row['Type2'] == 'Bug':
                bug[pokemon] = row['Name']
            elif row['Type1'] == 'Ghost' or row['Type2'] == 'Ghost':
                ghost[pokemon] = row['Name']
            elif row['Type1'] == 'Steel' or row['Type2'] == 'Steel':
                steel[pokemon] = row['Name']
            elif row['Type1'] == 'Dragon' or row['Type2'] == 'Dragon':
                dragon[pokemon] = row['Name']
            elif row['Type1'] == 'Dark' or row['Type2'] == 'Dark':
                dark[pokemon] = row['Name']
            elif row['Type1'] == 'Fairy' or row['Type2'] == 'Fairy':
                fairy[pokemon] = row['Name']
            pokedex_number_start += 1


# In[6]:


pokemon_data['Type2'] = pokemon_data['Type2'].apply(lambda x: 2*[x] if (x != 'Nan') else x)

pokemon_data.explode('Type2', ignore_index=True)


# In[7]:


normal = {}
fire = {}
water = {}
grass = {}
flying = {}
fighting = {}
poison = {}
electric = {}
ground = {}
rock = {}
psychic = {}
ice = {}
bug = {}
ghost = {}
steel = {}
dragon = {}
dark = {}
fairy = {}


# In[8]:


type_sorting2(1, 41)
print(ice)
print('break for easier reading')
print(fairy)
print('another break')
print(flying)
print('final break for now')
print('')
print(dragon)
print('')
print('')
print(water)
print('')
print('')
print(ground)


# In[9]:


print(len(fairy))

