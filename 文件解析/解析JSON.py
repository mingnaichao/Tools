import json
import xlwt

# region 获取数据
with open('JSON源文件/import_file.json', 'r') as jsonfile:
    file_data = json.load(jsonfile)

parse_data = {}  # { index: [data] }
for i in range(0, len(file_data)):
    _data = []
    for j in range(0, len(file_data.get('data' + str(i)))):
        _data.extend(file_data['data' + str(i)]['data' + str(i) + str(j)])
    else:
        parse_data[i] = _data
# endregion

# region 处理数据
insert_data = []  # [[第一列, 第二列], [第一列, 第二列], 第三行, ...]
category = ["HRBP学院", "OD学院", "TD学院", "薪酬学院", "绩效学院", "招聘学院", "劳动法学院", "HR数据学院", "管理学院", "学习发展学院"]
for _k, _v in parse_data.items():
    for x in _v:
        insert_data.append([
            category[_k],
            x['title'],
            x['line_price'],
            x['resource_count'],
            x['summary']
        ])

    # endregion

book = xlwt.Workbook(encoding='utf-8', style_compression=0)  # 不压缩
sheet = book.add_sheet('export_data', cell_overwrite_ok=True)


def style():
    _style = xlwt.XFStyle()
    pattern = xlwt.Pattern()
    pattern.pattern = xlwt.Pattern.SOLID_PATTERN
    pattern.pattern_fore_colour = xlwt.Style.colour_map['sky_blue']
    _style.pattern = pattern
    return _style


#  region 表头
col = ('类别', '课程标题', '课程价格', '课程数量', '课程描述')
for i in range(0, len(col)):
    sheet.write(0, i, col[i], style())
# endregion

# region 写数据
for i in range(0, len(insert_data)):
    data = insert_data[i]  # 行数据
    for j in range(0, len(col)):
        sheet.write(i + 1, j, data[j])
# endregion

book.save('export_file.xlsx')
