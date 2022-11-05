

# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:
# Write some data to the file.
   # Write three counties to the file.
     txt_file.write("Arapahoe, ")
     txt_file.write("Denver, ")
     txt_file.write("Jefferson\n")  #or    txt_file.write("Arapahoe, Denver, Jefferson")

     txt_file.write("\nCounties in Election")
     txt_file.write("\n---------------------------------- ")
     # Write three counties to the file.
     txt_file.write("\nArapahoe\nDenver\nJefferson")