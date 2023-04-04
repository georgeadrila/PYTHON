import csv
import os

# Change the current working directory to the directory containing the CSV file
os.chdir('Day10')

# Open the CSV file
with open('contacts.csv', mode='r', encoding='utf-8-sig') as infile:
    reader = csv.reader(infile)
    header = next(reader)  # skip the header row

    # Loop through each row in the file
    updated_rows = []  # initialize an empty list to store the updated rows
    for row in reader:
        name = row[0] # Get the name column
        if "cr" in name:
            # Remove the current number after "cr"
            name_without_number = "cr " + " ".join(name.split(" ")[2:])
            
            # Join the name without the number with the last string in the name
            name_parts = name_without_number.split()
            name_parts[-1] += " " + name.split()[-1]
            new_name = " ".join(name_parts)
            
            row[0] = new_name  # Update the name
            
            # Print the updated row
            print(row)
        
        # Add the updated row to the list
        updated_rows.append(row)
    
    # Save the updated CSV file to a new file
    with open('output.csv', mode='w', encoding='utf-8', newline='') as outfile:
        writer = csv.writer(outfile)
        writer.writerow(header)  # write the header row
        writer.writerows(updated_rows)  # write the remaining rows
