class Test(object):
    def __init__(self, **kwargs):
        for field in ('date', 'tests', 'confirmed_cases', 'deaths'):
            setattr(self, field, kwargs.get(field, None))
