import pandas as pd


def get_df_from_url(url):
    # TODO add checking and fallback to ./data
    df = pd.read_csv(url)
    df = df.replace('1 to 4', 3)
    return df.fillna(method='ffill')


def get_totals_from_df(df):
    totals = {}
    for i in range(len(df)):
        totals[i] = Total(date=df.loc[i, "Date"],
                          tests=df.loc[i, "Tests"],
                          confirmed_cases=df.loc[i, "ConfirmedCases"],
                          deaths=df.loc[i, "Deaths"])
    return totals


def get_cases_from_df(df):
    cases = {}
    for i in range(len(df)):
        cases[i] = Case(date=df.loc[i, "Date"],
                        country=df.loc[i, "Country"],
                        area_code=df.loc[i, "AreaCode"],
                        area=df.loc[i, "Area"],
                        total_cases=df.loc[i, "TotalCases"])
    return cases


def get_total_instance_by_date(date_str, df):
    instance_df = df[df['Date'] == date_str].to_numpy()
    if len(instance_df) == 0:
        raise ValueError
    return Total(date=instance_df[0][0],
                 tests=instance_df[0][1],
                 confirmed_cases=instance_df[0][2],
                 deaths=instance_df[0][3])


def get_case_instances_by_date(date_str, df):
    instances_df = df[df['Date'] == date_str]
    if len(instances_df) == 0:
        raise ValueError
    cases = {}
    for i in range(len(instances_df)):
        cases[i] = Case(date=instances_df.loc[i, "Date"],
                        country=instances_df.loc[i, "Country"],
                        area_code=instances_df.loc[i, "AreaCode"],
                        area=instances_df.loc[i, "Area"],
                        total_cases=instances_df.loc[i, "TotalCases"])
    return cases


class Total(object):
    def __init__(self, **kwargs):
        for field in ('date', 'tests', 'confirmed_cases', 'deaths'):
            setattr(self, field, kwargs.get(field, None))


class Case(object):
    def __init__(self, **kwargs):
        for field in ('date', 'country', 'area_code', 'area', 'total_cases'):
            setattr(self, field, kwargs.get(field, None))
