import xlsxwriter

 

book = xlsxwriter.Workbook('777.xlsx')

sheet = book.add_worksheet('demo')

sheet.insert_image('D4','0.jpg')

book.close()