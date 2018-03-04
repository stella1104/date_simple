from datetime import datetime

def get_date(date=datetime.today().__str__()[:10]):
    
    def has_letter(date):
        for c in date:
            if c.isalpha():
                return True
        return False
    if '-' in date:
        if has_letter(date):
            return datetime.strptime(date,'%d-%B-%y')
        else:
            return datetime.strptime(date,'%Y-%m-%d')
    elif '/' in date:
        return datetime.strptime(date,'%d/%m/%Y')
    else:
        raise ValueError('bad date format')
        
def add_day(dt, day = 1):
    from datetime import timedelta
    return (dt + timedelta(days=day) )

def add_week(dt, week = 1):
    from datetime import timedelta
    return (dt + timedelta(days=week*7) )

def format_date(dt = datetime.today(), format = '%Y-%m-%d'):
    from datetime import datetime 
    if type(dt) != datetime:
        raise TypeError("input type = {0} which should be datetime.datetime".format(type(dt)))
    if format == 'MM/DD/YYY':
        return dt.__format__('%m/%d/%Y')[:10]
    elif format == 'DD-Mon-YY':
        return dt.__format__('%d-%b-%y')
    elif format == '%Y-%m-%d':
        return dt.__format__(format)[:10]
    else:
        raise ValueError('Unrecognized format')
        

def add_month(dt):
    from datetime import datetime
    return datetime(dt.year,dt.month+1,dt.day)
def add_year(dt):
    from datetime import datetime
    return datetime(dt.year+1,dt.month,dt.day)



