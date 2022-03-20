counties_tuples = ["Arapahoe","Denver","Jefferson"]

for i in range(len(counties_tuples)):

      print(counties_tuples[i])

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:

# Write some data to the file.
     txt_file.write('Counties in the election \n__________________________\n')
     txt_file.write("\nArapahoe, \n")
     txt_file.write("Denver, \n")
     txt_file.write("Jefferson, ")