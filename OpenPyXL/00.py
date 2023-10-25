import openpyxl

wb = openpyxl.Workbook()
sheet = wb.active
list = ["Gazi","Faysal","Jubayer"]
sheet.append(list)
sheet.append(list)
sheet.append(list)
sheet.append(list)

wb.save("OpenPyXL/text.xlsx")