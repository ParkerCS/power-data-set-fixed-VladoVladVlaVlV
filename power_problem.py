'''
Use the power_data.csv file AND the zipcode database
to answer the questions below.  Make sure all answers
are printed in a readable format. (i.e. "The city with the highest electricity cost in Illinois is XXXXX."

The power_data dataset, compiled by NREL using data from ABB,
the Velocity Suite and the U.S. Energy Information
Administration dataset 861, provides average residential,
commercial and industrial electricity rates by zip code for
both investor owned utilities (IOU) and non-investor owned
utilities. Note: the file includes average rates for each
utility, but not the detailed rate structure data found in the
OpenEI U.S. Utility Rate Database.

This is a big dataset.
Below are some questions that you likely would not be able
to answer without some help from a programming language.
It's good geeky fun.  Enjoy

FOR ALL THE RATES, ONLY USE THE BUNDLED VALUES (NOT DELIVERY).  This rate includes transmission fees and grid fees that are part of the true rate.
'''

def insertion_sort(my_list):
    for pos in range(1, len(my_list)):
        key_pos = pos
        scan_pos = key_pos - 1
        key_val = my_list[key_pos]
        while scan_pos >= 0 and my_list[scan_pos] > key_val:
            my_list[scan_pos + 1] = my_list[scan_pos]
            scan_pos -= 1
        my_list[scan_pos + 1] = key_val

    return my_list


#1  What is the average residential rate for YOUR zipcode? You will need to read the power_data into your program to answer this.  (7pts)
import csv
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches


file=open("power_data.csv","r")
reader = csv.reader(file, delimiter=",")  # give instructions for splitting the text
new_list=[]
for row in reader:  # split the text up
    new_list.append(row)


key="60614" #define the thing we are searching for
key_list=[]
for i in range(len(new_list)):
    if str(new_list[i][0])==key: #compare list item to key
        key_list.append(new_list[i])
print("Your zip code's average residential rate is",key_list[0][8])
#2 What is the MEDIAN rate for all BUNDLED RESIDENTIAL rates in Illinois? Use the data you extracted to check all "IL" zipcodes to answer this. (10pts)
key2="IL"
key2_list=[]
suma=0
illinois_list=[]
full_illinois_list=[]
for i in range(len(new_list)):
    if str(new_list[i][3])==key2 and str(new_list[i][4])=="Bundled": #same as #1 just has two keys. "bundled" and "IL"
       illinois_list.append(float(new_list[i][-1]))
       full_illinois_list.append(new_list[i])


print(insertion_sort(illinois_list))
kek=int(len(illinois_list)/2) # we find the middle position in the entire list

print("The Median rate for all bundled residential rates is",insertion_sort(illinois_list)[kek]) # we find the value of the middle position in the list





#3 What city in Illinois has the lowest residential rate?  Which has the highest?  You will need to go through the database and compare each value for this one. Then you will need to reference the zipcode dataset to get the city.  (15pts)
def sorting(my_list): #sort the list so we can find the lowest residential rate
    for pos in range(len(my_list)):
        min_pos = pos
        for scan_pos in range(min_pos, len(my_list)):
            if my_list[scan_pos][-1] > my_list[min_pos][-1]:
                min_pos = scan_pos
        temp = my_list[pos]
        my_list[pos] = my_list[min_pos]
        my_list[min_pos] = temp

    print(my_list)

sorting(full_illinois_list) #use the function for sorting

file2=open("free-zipcode-database-Primary.csv","r")
reader = csv.reader(file2, delimiter=",")  # give instructions for splitting the text
second_file_list=[]
for row in reader:  # split the text up
    second_file_list.append(row)

key_highest=full_illinois_list[0][0] #define what we are searching for
key_lowest=full_illinois_list[-1][0]
answer=None #blank variables
answer2=None

for i in range(len(new_list)):
    if str(second_file_list[i][0])==key_highest:
        answer=second_file_list[i][2]
    if str(second_file_list[i][0])==key_lowest:
        answer2=second_file_list[i][2]

print(answer,"has the highest residential rate in Illinois while",answer2,"has the lowest residential rate")


#FOR #4  CHOOSE ONE OF THE FOLLOWING TWO PROBLEMS. The first one is easier than the second.
#4  (Easier) USING ONLY THE ZIP CODE DATA... Make a scatterplot of all the zip codes in Illinois according to their Lat/Long.  Make the marker size vary depending on the population contained in that zip code.  Add an alpha value to the marker so that you can see overlapping markers.

xval=[]
yval=[]
color_list=[]
size_list=[]

for i in range(1,len(second_file_list)):
    try:
        xval.append(float(second_file_list[i][5])) #add the longitude and latitude
        yval.append(float(second_file_list[i][6]))
    except:
        xval.append(None)
        yval.append(None)
    try:
        if float(second_file_list[i][10])>20000: #determine color based on number of citizens
            color="red"
        elif float(second_file_list[i][10])>10000:
            color="yellow"
        else:
            color="green"
    except:
        color="black"
    color_list.append(color)
    try:
        size=int(second_file_list[i][10])/200 #determine size
    except:
        size=50
    size_list.append(size)

my_scatterplot=plt.scatter(xval,yval,color=color_list,s=size_list,alpha=0.1) #add item to plot

plt.show() #show the plot
#4 (Harder) USING BOTH THE ZIP CODE DATA AND THE POWER DATA... Make a scatterplot of all zip codes in Illinois according to their Lat/Long.  Make the marker red for the top 25% in residential power rate.  Make the marker yellow for the middle 25 to 50 percentile. Make the marker green if customers pay a rate in the bottom 50% of residential power cost.  This one is very challenging.  You are using data from two different datasets and merging them into one.  There are many ways to solve. (20pts)

