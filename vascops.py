files = ["1_tn.txt", "3_tn.txt"]

for filename in files:
    with open(filename, 'r') as f:
        csv_line = ""
        for line in f:
            index_of_equal = line.find("=")
            
            # Only treat lines with a "="-sign
            if index_of_equal != -1:
                idx = line.find("[")
                
                if idx == -1:
                    data = line[index_of_equal:]
                else:
                    data = line[index_of_equal:idx]
                    
                csv_line = csv_line + data + ","
                
        # Print the CSV-line
        print csv_line
