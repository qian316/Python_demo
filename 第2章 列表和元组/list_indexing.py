# _*_ coding:utf-8
# indexing 索引学习demo
months = [
    'January',
    'February',
    'March',
    'April',
    'May',
    'June',
    'July',
    'August',
    'September',
    'October',
    'November',
    'December'
]

# 一个列表，多个列表组合，其中包含数1~31对应的结尾
endings = ['st','nd','rd'] + 17 * ['th'] \
    + ['st','nd','rd'] + 7 * ['th'] \
    + ['st']

year = input('Year: ')
month = input('Month（1-12）: ')
day = input('Day（1-31）: ')

mouth_number = int(month)
day_number = int(day)

# 正确索引
month_name = months[mouth_number - 1]
ordinal = day + endings[day_number - 1]

print( month_name + ' ' + ordinal + ',' + year)


