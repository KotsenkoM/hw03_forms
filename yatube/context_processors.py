import datetime as dt


def year(request):
    year_now = str(dt.datetime.today().year)
    return {'year': year_now}
