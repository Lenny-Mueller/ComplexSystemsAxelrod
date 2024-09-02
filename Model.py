import numpy as np
import matplotlib
import matplotlib.pyplot as plt 

# This file demonstrates the implementation of Axelrod's model of the dissemination of culture into python
# For this only the simple case of a non-peridoic boundary and only interaction between the four nearest neighbors is used


#PARAMETERS -   -   -   -   -   -

grid_width = 10 # Gives the width of the grid. The total amount of agents on the grid is then given by grid_width^2.
features = 5 # How many entries does the cultural vector have.
traits = 12 # How many possible values per feature
timesteps = 1000 # How long to run the model

#INITIALIZATION -   -   -   -   -   -

mat = np.random.randint(0, traits, (grid_width, grid_width, features)) #Generation of the initial cultural vector of each agent
colormaplist = []
mat2 = np.zeros((grid_width, grid_width, features), dtype= str)
mat3 = np.zeros((grid_width, grid_width), dtype = int)
dicts = {}
#This part is solely for the visualization
for i in range(grid_width): #Iteration over each agent on the grid
    for j in range(grid_width):
        mat2[i, j] = [str(np.base_repr(k, traits)) for k in mat[i, j]] # Trait represented by number is transformed into system with the base given by total number of possible traits
        mat3[i, j] = int(''.join(mat2[i, j]), traits) # Vector is then transformed into a single number in decimal system
for val in np.unique(mat3): # For every vector on the grid that is not already in the dictionairy, a new entry is created where the number representing the vector is the key and the value is the current length of the dictionairy + 1
    if val not in dicts.keys():
        dicts[val] = len(dicts.keys()) + 1
        colormaplist.append([np.random.uniform(0, 1), np.random.uniform(0, 1), np.random.uniform(0, 1), 1]) # For every new value a new color (RGB) is added to the colormap list
cmap = matplotlib.colors.ListedColormap(colormaplist)
for i in range(grid_width):
    for j in range(grid_width):
        mat3[i, j] = dicts[mat3[i, j]]

fig, ax = plt.subplots(layout = 'constrained')

#ITERATION  -   -   -   -   -   -
for timestep in range(timesteps): #Iteration over the given amount of timesteps
    for iteration in range(grid_width**2): #One timestep is defined as iteration over all agents once (on average)
        pick = np.random.randint(0, grid_width, 2) #Pick random agent
        end = grid_width - 1
        neighbor = [[np.abs(pick[0]-1), pick[1]], [pick[0]+1, pick[1]], [pick[0], np.abs(pick[1]-1)], [pick[0], pick[1]+1]]
        neighbor = neighbor[np.random.randint(0, 4)] #Pick one of the four nearest neighbors to the agent
        if sum(np.array(neighbor) <= np.array([grid_width-1, grid_width-1])) == 2: #Compute how similar their cultural vectors are
            similarity = np.sum(np.where(mat[*pick] == mat[*neighbor], 1, 0))/features
            differences = np.where(mat[*pick] != mat[*neighbor])[0]
            chance = np.random.uniform(0, 1)
            if chance <= similarity and similarity < 1: #Given by similarity perform interaction
                dummy = np.array(mat[*neighbor])
                randdiff = np.random.randint(0, len(differences))
                mat[*pick][differences[randdiff]] = dummy[differences[randdiff]]
        else:
            None


#VISUALIZATION  -   -   -   -   -   -
    for i in range(grid_width): #Iteration over each agent on the grid
        for j in range(grid_width):
            mat2[i, j] = [str(np.base_repr(k, traits)) for k in mat[i, j]] # Trait represented by number is transformed into system with the base given by total number of possible traits
            mat3[i, j] = int(''.join(mat2[i, j]), traits) # Vector is then transformed into a single number in decimal system
    for val in np.unique(mat3): # For every vector on the grid that is not already in the dictionairy, a new entry is created where the number representing the vector is the key and the value is the current length of the dictionairy + 1
        if val not in dicts.keys():
            dicts[val] = len(dicts.keys()) + 1
            colormaplist.append([np.random.uniform(0, 1), np.random.uniform(0, 1), np.random.uniform(0, 1), 1]) # For every new value a new color (RGB) is added to the colormap list
    cmap = matplotlib.colors.ListedColormap(colormaplist)
    for i in range(grid_width):
        for j in range(grid_width):
            mat3[i, j] = dicts[mat3[i, j]]

    ax.cla()
    ax.matshow(mat3, cmap = cmap, vmin = 1, vmax = len(dicts.keys()))
    ax.set_title(f"t = {timestep}")
    ax.set_xticks([])
    ax.set_yticks([])
    plt.pause(0.001) #Adjust pause length for slower run 