import json
import xlwt

# region 获取数据
with open('/Users/mingnaichao/Developer/GitHub/tools/文件解析/JSON源文件/import_file.json', 'r') as jsonfile:
    file_data = json.load(jsonfile)
# endregion

# region 处理数据
insert_data = []  # [[第一列, 第二列], [第一列, 第二列], 第三行, ...]
for x in file_data.get('data'):
    insert_data.append([x.get('resource_title'), file_data.get('url').get(x.get('resource_id'))])
else:
    for i in file_data.get('file'):
        insert_data.append([i.get('title'), i.get('url')])

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
col = ('课程', '下载地址')
for i in range(0, len(col)):
    sheet.write(0, i, col[i], style())
# endregion

# region 写数据
for i in range(0, len(insert_data)):
    data = insert_data[i]  # 行数据
    for j in range(0, len(col)):
        sheet.write(i + 1, j, data[j])
# endregion

book.save('/Users/mingnaichao/Developer/GitHub/tools/文件解析/export_file.xls')
