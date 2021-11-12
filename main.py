import colorgram

colors = colorgram.extract('truniokuva.jpg',6)
print(colors)
list_of_colors = []
for i in range(0, 6):
    color = colors[i]
    print(color.rgb)
    list_of_colors.append(color.rgb)

print(list_of_colors)