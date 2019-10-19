# -*- coding: utf-8 -*-
# @author : mingnaichao
# @date : 2019/10/17
# @time : 11:15
import calendar
import datetime


def get_month_begin(month, begin_day=1):
    """
    根据日期获取所在月的开始日期
    :param month: '2019-10'
    :param begin_day:
    :return:
    """
    return '{}-{}-{:0>2d}'.format(month[:4], month[-2:], begin_day)


def get_month_end(month, begin_day=1):
    """
    根据日期获取所在月的结束日期
    :param month: '2019-10'
    :param begin_day:
    :return:
    """
    _month_begin = datetime.datetime.strptime(get_month_begin(month, begin_day), '%Y-%m-%d')
    _, _month_day_count = calendar.monthrange(_month_begin.year, _month_begin.month)
    _month_end = _month_begin + datetime.timedelta(days=_month_day_count - 1)
    return _month_end.strftime('%Y-%m-%d')


def weekday_func(_date):
    """
    根据日期返回星期几
    :param _date: '2019-10-08'
    """
    date = datetime.date(int(_date[:4]), int(_date[5:7]), int(_date[8:10]))
    return date.weekday() + 1


def get_week_start_and_end_by_date(_date):
    """
    根据某个日期获取所在周的开始时间、结束时间
    :param _date:
    :return:
    """
    _week_day = weekday_func(_date)
    monday_day = int(_date[8:10]) - (_week_day - 1)
    if monday_day <= 0:
        up_month = int(_date[5:7]) - 1
        if up_month < 0:
            end_date = get_month_end(_date[:5] + '12')
        elif up_month == 0:
            end_date = get_month_end(str(int(_date[:4]) - 1) + '-12')
        else:
            if up_month > 10:
                end_date = get_month_end(_date[:5] + str(up_month))
            else:
                end_date = get_month_end(_date[:5] + '0' + str(up_month))

        if int(end_date[8:10]) + monday_day >= 10:
            _start_week_day = end_date[:8] + str(int(end_date[8:10]) + monday_day)
        else:
            _start_week_day = end_date[:8] + '0' + str(int(end_date[8:10]) + monday_day)
    else:
        if monday_day >= 10:
            _start_week_day = _date[:8] + str(monday_day)
        else:
            _start_week_day = _date[:8] + '0' + str(monday_day)

    week_month_end_date = get_month_end(_start_week_day[:7])
    day = int(week_month_end_date[8:10]) - (int(_start_week_day[8:10]) + 6)
    if day >= 0:
        if day >= 10:
            _end_week_day = _start_week_day[:8] + str(int(_start_week_day[8:10]) + 6)
        else:
            _end_week_day = _start_week_day[:8] + '0' + str(int(_start_week_day[8:10]) + 6)
    else:
        next_month = int(_start_week_day[5:7]) + 1
        if next_month == 13:
            next_month = 1
        if next_month > 10:
            _end_week_day = _start_week_day[:4] + '-' + str(next_month) + '-0' + str(-day)
        else:
            _end_week_day = _start_week_day[:4] + '-0' + str(next_month) + '-0' + str(-day)

    return _start_week_day, _end_week_day


get_week_start_and_end_by_date('2019-12-30')
