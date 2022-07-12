import datetime

date = datetime.date(2022, 7, 12)
def get_day(date):
    return {
        'Monday': '월요일',
        'Tuesday': '화요일',
        'Wednesday': '수요일',
        'Thursday': '목요일',
        'Friday': '금요일',
        'Saturday': '토요일',
        'Sunday': '일요일'
    }[date.strftime('%A')]

print(get_day(date))

to_control_key_error_use_get_method = {
        'Monday': '월요일',
        'Tuesday': '화요일',
        'Wednesday': '수요일',
        'Thursday': '목요일',
        'Friday': '금요일',
        'Saturday': '토요일',
        'Sunday': '일요일'
    }.get(date.strftime('%A'), 'UNKNOWN')