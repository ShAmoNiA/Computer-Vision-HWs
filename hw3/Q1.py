
import matplotlib.pyplot as plt
import numpy

def stem(pxl,arg,color):
    x=numpy.array(pxl)
    for i in numpy.unique(x):
        counter = 0
        for item in pxl:
            if item == i:
                counter +=1
        plt.stem(i, counter,arg ,markerfmt=color)

# pxl = [7,7,8,8,8,8,2,1,4,4,4,8,7,0,5,5,2,8,8,0,6,9,9,7,8,7,6,6,7,7]
# pxl = [9,9,9,9,7.5,7.5,9,3,3,3,0,0,9,0,4.5,4.5,0,7.5,7.5,9,9,6,0,9,7.5,7.5,6,6,7.5,9]


arg = 'g'
color = 'go'

plt.stem(0, 5,arg ,markerfmt=color)
plt.stem(3, 3,arg ,markerfmt=color)
plt.stem(4.5, 2,arg ,markerfmt=color)
plt.stem(6, 3,arg ,markerfmt=color)
plt.stem(7.5, 7,arg ,markerfmt=color)
plt.stem(9, 10,arg ,markerfmt=color)



# stem(pxl,'b','bo')


# pxl.sort()
# del pxl [len(pxl)-int(len(pxl)*(1/10)):len(pxl)]
# del pxl [0:int(len(pxl)*(1/10))+1]

# stem(pxl,'g','go')
plt.show()
# pxl.sort()
# print(pxl)
