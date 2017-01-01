import re

CAPS = re.compile(r'([),"]) ([A-Z])')
CAPS_LINE_REPLACEMENT = r'\1\n\2'

def queryset_sql(queryset, with_params=False):
    sql_plus = queryset.query.sql_with_params()
    sql_str = sql_plus[0]

    print(CAPS.sub(CAPS_LINE_REPLACEMENT, sql_str))

    if (with_params):
        print('({})'.format(r',\n'.join(
            [str(p) for p in sql_plus[1:]
             if p])))
