import openpyxl

# loading data
workbook = openpyxl.load_workbook("OpenPyXL/text.xlsx")
sheet = workbook.active
cell_value = sheet["A1"].value
print(cell_value)