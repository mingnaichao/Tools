import xlrd
import pythonMySQL


def read_file(file_url):
    '''读取文件路径'''
    try:
        data = xlrd.open_workbook(file_url)
        return data
    except Exception as e:
        print("读取文件失败!")


def filter_excel(data, column_name=0, by_name='Sheet1'):
    """
    :param workbook:
    :param column_name:
    :param by_name: 对应的Sheet页
    :return:
    """
    table = data.sheet_by_name(by_name)  # 获得表格
    total_rows = table.nrows  # 拿到总共行数
    columns = table.row_values(column_name)  # 某一行数据 ['姓名', '用户名', '联系方式', '密码']
    excel_list = []
    for one_row in range(1, total_rows):  # 也就是从Excel第二行开始，第一行表头不算

        row = table.row_values(one_row)
        if row:
            row_object = {}
            for i in range(0, len(columns)):
                row_object[columns[i]] = row[i]  # 表头与数据对应

            excel_list.append(row_object)

    return excel_list


def main():
    file_name = input("请输入您要导入的文件:")
    file_name = r'%s' % file_name
    data = read_file(file_name)
    tables = filter_excel(data)
    for row in tables:
        print(row)
if __name__ == '__main__':
    main()
