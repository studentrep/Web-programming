#File reading
#Reading celsius temperatures from a CSV file, converting them to
#fahrenheit, and writing them to another CSV file

#the file that is going to be read
r = open("celsius.csv","r")
#the file that is going to be written to
w = open("fahrenheit.csv","w")

#grab the column headers and write them to the fahrenheit file
headers = r.readline() #headers will contain the trailing \n
w.write(headers)

#when this for loop starts, the first line has already been read
#because of this, the for loop starts reading at the second line
for line in r:
    #account for the new line character on each line (we don't want an extra
    #space to be printed
    line = line.replace("\n","")

    #create a list from each line (using comma as a divider)
    line_list = line.split(",")

    #if we know for sure our list contains three elements, we can assign
    #the list items to three variables as follows
    town, min_c, max_c = line_list
    min_f = 32 + float(min_c) / 5 * 9
    max_f = 32 + float(max_c) / 5 * 9
    
    #makes a list from the specified variables
    #list_out = [town, str(min_f), str(max_f)]

    #converts list to a string and writes it to the fahrenheit.csv file
    #w.write(",".join(list_out) + "\n")

    #another way of writing to the fahrenheit file
    w.write("{town},{min_f},{max_f}\n".format(town = town,min_f = min_f,max_f = max_f))

    #prints each line as a list
    #print(line_list)

r.close()
