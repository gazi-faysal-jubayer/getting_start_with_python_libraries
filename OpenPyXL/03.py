import openpyxl
from openpyxl.comments import Comment

# add comments
file = "OpenPyXL/mydata.xlsx"
workbook = openpyxl.load_workbook(file)
sheet = workbook.active

cell = sheet['C7']
comment_obj = Comment("I'm not sure where Sourav lives in.", "Gazi Faysal Jubayer")

cell.comment = comment_obj
workbook.save(file)