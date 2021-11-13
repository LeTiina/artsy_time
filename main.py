import colorgram

colors = colorgram.extract('truniokuva.jpg',6)
list_of_colors = []
for i in range(0, 6):
    color = colors[i]
    rgb = color.rgb
    red = rgb[0]
    blue = rgb[1]
    yellow = rgb[2]
    tuple_for_the_list = (red, blue, yellow)
    list_of_colors.append(tuple_for_the_list)

print(list_of_colors)