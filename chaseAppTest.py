FILE_NAME = "C:/CodingProjects/Chase Activity/LastChases.CSV"

# I envision that this could become accounting software where the user inserts a CSV file and 
# then the user selects what types of values in the dataset they want to be tracked

# Convert CSV file to 2d array
# We convert to 2d array so we can work with the file.
def array2D(file_name):
    # data gets empty list
    data = []
    # open the file_name (its an argument) in read mode.
    with open(file_name, "r") as file:
        # For every line in file
        for line in file:
            # varible temparray gets strip and split ()
            # Strip removes any white/leading spaces and split divides string into substrings.
            # Substrings are when every character in the string has an index.
            temparray = line.strip().split(',')
            # append the temporary array to data.
            data.append(temparray)
    # return data
    return data

# Calculate the sum of the last column
def calculate_total(data):
    try:
        header = data[0]
        number_index = header.index("Amount")
        categroy_index = header.index("Category")
        store_index = header.index("Description")
        total = 0
        for row in data[1:]:
            if len(row) > number_index and row[number_index]:  # Check if row has enough elements and not empty
                if row[categroy_index] in ["Groceries", "Gas", "Automotive"] or "Great Clips" in row[store_index]:
                    total += float(row[number_index])
        return total
    except ValueError:
        print("Column 'Amount' not found in the header.")
        return None

data = array2D(FILE_NAME)
total = calculate_total(data)

if total is not None:
    print("Total amount in the 'Amount' column:", total)

