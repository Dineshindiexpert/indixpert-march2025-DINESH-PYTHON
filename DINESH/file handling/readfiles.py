filepath = r"C:\Users\jai seya ram\OneDrive\Documents\project indiexpert\readfile.txt"
filepath2 = r""



with open(filepath,"rb") as file:
    data = file.read()
    
    print(data)


with open(filepath2,"wb") as file: 
     file.write(data)