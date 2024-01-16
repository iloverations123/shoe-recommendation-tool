from scipy.spatial import cKDTree
from colourconverter import ColorConverter, File_ColorConverter
from nike_dict import color_dict




all_rgb_values = [items[1] for dict_items in color_dict for i in color_dict[dict_items]['Colour'] for items in i]



# Create a KD-tree for all RGB values -> basically plots points on the trees
kdtree_all = cKDTree(all_rgb_values)



def similiar_shoes(user_rgb_values):


# find the neighbors, k determines the number of tuples that is closest to the user_rgb_values
# .query() returns an array of distances from query points to neighbor + array of indices to the positions of the nearest rgb values
# the [1] accesses the indices in the tuple

    k_nearest_neighbors_indices = kdtree_all.query(user_rgb_values, k=2)[1]
    print(k_nearest_neighbors_indices)
# Match each user choice with its nearest neighbor in the dictionary

    matches = []

    for i, indices in enumerate(k_nearest_neighbors_indices):
        matches.extend(all_rgb_values[j] for j in indices)

    group1 = matches[1::2] # slicing starts from index 1 and skips every 2 elements
# create another code block that checks for overall similarity

    yes =  ColorConverter(group1)
    new_list = [yes.get_individual_colour(items)[0] for items in group1]
    unique_shoes_set = set()
   



    print(new_list)

 # this checks for individual colour matches and works fine
    for i in color_dict:
        for index, shoe_colours in enumerate(color_dict[i]["Colour"]): # using enumerate here so i can reference the url link order4
            current_colours = {colours[0] for colours in shoe_colours}
        
            for colour_name, rgb_value_pair in shoe_colours:
                if colour_name in new_list : # i need a function that swaps group1 out wiht group 2 / change this list to a list of colours name.
                    if color_dict[i]["Shoe Name"] not in unique_shoes_set:
                        tuples = (color_dict[i]['Shoe Name'], color_dict[i]['Shoe Urls'][index])
                        unique_shoes_set.add(tuples)
                              
                    

   
    return unique_shoes_set
        # this is fine for singling out the exact / near same colour that my shoe has, but it only takes into consideration 1 colour
        # plus i need to add a range of rgb values that can be considered red,blue,yellow -> how to do this






# today's objectives:


# linking the image of the recommended shoe with that colour scheme in the recommendations output (visual representation)


# there is repetition in the code, redo the dictionary again

