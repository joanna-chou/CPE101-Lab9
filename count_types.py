#Lab 9 – File I/O and Exceptions
#Name: Joanna Chou
#Instructor: Dr. S. Einakian
#Section: 07

#Function 1: This function reads the file and splits the data into a list.
def read_file(file_name: str) -> list:
    lst = []
    try:
        file = open(file_name, "r")
    except FileNotFoundError:
        exit("Unable to open "+ file_name)
    except PermissionError:
        exit("Unable to open "+ file_name)
    for line in file:
        line = line.strip()
        line = line.split()
        for l in line:
            lst.append(l)
    file.close()
    return lst

#Function 2: This function returns the number of integers, floats, and other types of data given a list.
def count_things(lst: list) -> str:
    num_of_int = 0
    num_of_float = 0
    num_of_other = 0
    for element in lst:
        try:
            int(element)
            num_of_int += 1
        except:
            try:
                float(element)
                num_of_float += 1
            except:
                num_of_other += 1
    return (num_of_int, num_of_float, num_of_other)

#This runs the functions.
def main():
    info = count_things(read_file('infile'))
    print("Ints: " + str(info[0]))
    print("Floats: " + str(info[1]))
    print("Other: " + str(info[2]))

if __name__ == "__main__":
    main()
