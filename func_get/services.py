import re

from .functions import *

CHAR_FUNCTIONS = [
    ("a", fun_a),
    ("b", fun_b),
    ("c", fun_c),
    ("d", fun_d),
    ("e", fun_e),
    ("f", fun_f),
]


class Functions:
    data = []
    rule = []
    result = []

    def __init__(self, data: list, rule: list):
        self._make_data(data[0])
        self._make_rules(rule[0])
        self._make_result()

    def _make_data(self, data):
        self.data = []
        if data:
            self.data = [float(i) for i in data[1:-1].split(",")]

    def _make_rules(self, rule):
        self.rule = []
        true_rule = re.findall(r'[a-z]', rule)
        for r in true_rule:
            for f in CHAR_FUNCTIONS:
                if r == f[0]:
                    self.rule.append(f[1])

    def _make_result(self):
        self.result = []
        for i in range(len(self.data)):
            try:
                self.result.append(self.rule[i](self.data[i]))
            except IndexError:
                self.result.append(self.data[i])

# data = {'data': [1, 2, 3, 4, 5], 'rule': ['a', 'b', 'c', 'd', 'e', 'f']}
# f = Functions(**data)
# print(f.result)
