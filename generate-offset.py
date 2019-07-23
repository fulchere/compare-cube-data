import epics
import numpy as np
from matplotlib import pyplot as plt

### python3

ls = epics.caget("FS1_QUBE05:AIV_N0101_CH0:I_RD")
ls2 = epics.caget("BDS_NEWQUBE:AIV_N0102_CH0:I_RD")
#print(epics.cainfo('XXX:m1.VAL'))

length = len(ls)
print("the length of the first dataset is:  ", length)
array_2 = []
for i in range(length):
    array_2.append(i)

print("the length of the second dataset is: ", len(ls2))
array_1 = np.array(ls)
array_2 = np.array(ls2)
plt.title("Square wave") 
plt.xlabel("x axis") 
plt.ylabel("y axis") 
#plt.plot(array_2,array_1,"-c")
#plt.show()


# Works with python3 list and numpy array
def longest_streak(list_1, list_2):
    longest = 0
    return_str = "the longest streak(s) of matching numbers is(are): "
    for i in range(len(list_1)):
        for j in range(len(list_2)):
            if j < i:
                continue
            # end if
            if list_1[i] == list_2[j]:
                i_copy = i + 1
                j_copy = j + 1
                temp_longest = 1
                while i_copy < len(list_1) and j_copy < len(list_2) and list_1[i_copy] == list_2[j_copy]:
                    temp_longest += 1
                    i_copy += 1
                    j_copy += 1
                # end while
                if temp_longest > longest:
                    longest = temp_longest
                    return_str += str(longest)
                    return_str += ", "
                # end if
            # end if
        # end for
    # end for
    if return_str[-1] == " " and return_str[-2] == ",":
        return_str = return_str[:-2]
        return_str += "\nassuming same amount of points, this means the cubes differ by at most "
    # end if
    return_str += str(float((length-longest)/500))
    return_str += " seconds."
    return return_str
# end function

print(longest_streak(array_1, array_2))
