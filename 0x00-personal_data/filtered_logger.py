#!/usr/bin/env python3
"""defines a function filter_datum"""
import re
from typing import List

patterns = {
    'extract': lambda x, y: r'(?P<field>{})=[^{}]*'.format('|'.join(map(re.escape, x)), re.escape(y)),
    'replace': lambda x: r'\g<field>={}'.format(re.escape(x)),
        }


def filter_datum(fields: List[str], redaction: str, messages: str, separator: str):
    """Filters a log message using regex"""
    extract, replace = (patterns["extract"], patterns["replace"])
    return re.sub(extract(fields, separator), replace(redaction), messages)
