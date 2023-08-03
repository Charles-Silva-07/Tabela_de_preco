import xlrd

arq = xlrd.open_workbook('produtos.xlsx')
minhaplan = arq.sheet_by_name('valor_unitario')

produto = minhaplan.col_values(0)

print(produto)
