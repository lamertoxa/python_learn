def figure_perimetr(quad):
    import re
    def length(a,b):
        formul = ( ((b[0]-a[0])**2)+(b[1]-a[1])**2 )**(1/2)
        return formul
    left_top = [int(i) for i
                    in re.search(r'LT.:.',quad).group(0).replace("LT","").split(":")]
    left_bottom = [int(i) for i
                    in re.search(r'LB.:.',quad).group(0).replace("LB","").split(":")]
    right_top = [int(i) for i
                    in re.search(r'RT.:.',quad).group(0).replace("RT","").split(":")]
    right_bottom = [int(i) for i
                    in re.search(r'RB.:.',quad).group(0).replace("RB","").split(":")]

    return length(left_bottom, right_bottom) +\
        length(left_top, left_bottom) +\
        length(right_top, left_top) +\
        length(right_bottom, right_top)

# test1 = "LB1:1#RB4:1#LT1:3#RT4:3"
# print(figure_perimetr(test1))

test2 = "#LB0:1#RB5:1#LT4:5#RT8:3"
print(figure_perimetr(test2))