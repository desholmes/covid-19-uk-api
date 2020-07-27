import pandas as pd
from django.core.cache import caches


def url_to_key(url):
    key = url.replace('https://raw.githubusercontent.com/', '')
    return key.replace('/', '_')


def get_df_from_url(url):
    cache_key = url_to_key(url)
    cached_df = caches['default'].get(cache_key)
    cached_df = None

    if cached_df is None:
        df = pd.read_csv(url)
        # 'Clean' data
        df = df.replace('1 to 4', 3)
        df['Deaths_Daily'] = df['Deaths'].diff()
        df['Deaths_Daily_SMA_7'] = df.iloc[:, 4].rolling(window=8).mean()
        caches['default'].set(cache_key, df, 3600)  # 1hr
        df = df.fillna(-1)
        cached_df = df
    return cached_df


def get_totals_from_df(df):
    totals = {}
    i = 0
    for index, row in df.iterrows():
        totals[i] = Total(date=row["Date"],
                          tests=row["Tests"],
                          confirmed_cases=row["ConfirmedCases"],
                          deaths=row["Deaths"],
                          deaths_daily_sma_7=row["Deaths_Daily_SMA_7"],
                          deaths_daily=row["Deaths_Daily"])
        i += 1
    return totals


def get_totals_by_date(date_str, df):
    totals_by_date = df[df.Date.eq(date_str)]
    if len(totals_by_date) == 0:
        raise ValueError
    return get_totals_from_df(totals_by_date)


def get_cases_from_df(df):
    cases = {}
    i = 0
    for index, row in df.iterrows():
        cases[i] = Case(date=row["Date"],
                        country=row["Country"],
                        area_code=row["AreaCode"],
                        area=row["Area"],
                        total_cases=row["TotalCases"])
        i += 1
    return cases


def get_cases_by_date(date_str, df):
    cases_by_date = df[df.Date.eq(date_str)]
    if len(cases_by_date) == 0:
        raise ValueError
    return get_cases_from_df(cases_by_date)


class Total(object):
    def __init__(self, **kwargs):
        for field in ('date', 'tests', 'confirmed_cases',
                      'deaths', 'deaths_daily', 'deaths_daily_sma_7'):
            setattr(self, field, kwargs.get(field, None))


class Case(object):
    def __init__(self, **kwargs):
        for field in ('date', 'country', 'area_code', 'area', 'total_cases'):
            setattr(self, field, kwargs.get(field, None))
