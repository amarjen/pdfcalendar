#!/usr/bin/env python
# -*- coding: utf-8 -*-

from jinja2 import Environment, FileSystemLoader
import calendar
import argparse

env = Environment(loader=FileSystemLoader('template'),
        block_start_string = '\BLOCK{',
        block_end_string = '}',
        variable_start_string = '\VAR{',
        variable_end_string = '}',
        comment_start_string = '\#{',
        comment_end_string = '}',
        line_statement_prefix = '%%',
        line_comment_prefix = '%#',
        trim_blocks = True,
        autoescape = False,
                  )
template = env.get_template("calendar.tex")

MONTHS = 'Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec'.split()

class Calendar(object):
    def __init__(self, year, month):
        self.year = year
        self.month = month
        self.starting_day, self.days_in_month = calendar.monthrange(year, month)
        self.to_reduce = False
        if self.starting_day >= 5 and self.days_in_month == 31 :
            self.to_reduce = True

    def render(self):
        return template.render(month = MONTHS[self.month - 1],
                               year = str(self.year),
                               blankdays = self.starting_day,
                               days_in_month = self.days_in_month,
                               to_reduce = self.to_reduce,
                               )


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--month", type=int, required = True )
    parser.add_argument("--year", type=int, required = True )
    args = parser.parse_args()
    c = Calendar(args.year, args.month)
    print(c.render())
