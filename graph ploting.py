#To print a low end grapghs in terminal or txt file without using metapolide in python to strenght your computer- math logic.
def printing():
    x_axis=20
    y_axis=20
    with open("graph.txt","w") as file:
        for y in range(y_axis,0,-1):#range(start, stop, step)
            for x in range(0,x_axis+1): 
                if y==x:
                    file.write("*")
                    break
                else:
                    file.write(" ")
            file.write("\n")
printing()
