# -*- coding: utf-8 -*-
import xlrd


def read_excel():
    """
    读取excel
    :return:
    """
    excel_path = input('请输入文件路径：')
    # 打开文件
    workbook = xlrd.open_workbook(excel_path)
    # 获取所有sheet
    print(workbook.sheet_names())  # [u'Sheet1', u'Sheet2']
    sheet_index = input('请输入获取第几个Sheet：')
    sheet_name = workbook.sheet_names()[int(sheet_index)]
    print(sheet_name)

    # 根据sheet索引或者名称获取sheet内容
    sheet_info = workbook.sheet_by_name(sheet_name)
    # sheet的名称，行数，列数
    print(sheet_info.name, sheet_info.nrows, sheet_info.ncols)
    rows = sheet_info.row_values(3)  # 获取第4行内容
    print(rows)
    cols = sheet_info.col_values(0)  # 获取第1列内容
    print(cols)

    format_str = input('请输入格式化规则：')
    if format_str:
        print(eval(format_str))

    # 获取单元格内容的三种方法
    print(sheet_info.cell(1, 0).value.encode('utf-8'))
    print(sheet_info.cell_value(1, 0).encode('utf-8'))
    print(sheet_info.row(1)[0].value.encode('utf-8'))
    # 获取单元格内容的数据类型
    print(sheet_info.cell(1, 3).ctype)


if __name__ == '__main__':
    read_excel()
