from prettytable import PrettyTable

#Specify the Column Names while initializing the table
myTable = PrettyTable(["Student Name","Class","Section","Percentage"])

#Add rows

myTable.add_row(["Leo","J","A","90%"])
myTable.add_row(["Howard","J","78%"])
myTable.add_row(["Alice","J","60%"])
myTable.add_row(["Mozart","J","99%"])

print(myTable)