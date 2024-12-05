"""
Solution to day 05
"""
from dataclasses import dataclass
from collections import defaultdict
from copy import deepcopy
from typing import List, Dict

from pairing import pair

@dataclass
class Rule:
    first: int
    second: int

    def is_followed(self, update) -> bool:
        pass

    @property
    def pages(self) -> List[int]:
        return [self.first, self.second]
    
    def __hash__(self) -> int:
        return pair(self.first, self.second, safe=True)

@dataclass
class Update:
    pages: List[str]
    
    @property
    def middle_page(self) -> int:
        number_of_pages = len(self.pages)
        index_of_middle_page = int(number_of_pages/ 2)
        middle_page = int(self.pages[index_of_middle_page])
        return middle_page

    def __iter__(self) -> List[int]:
        return iter([int(page) for page in self.pages])
    
    def __len__(self) -> int:
        return len(self.pages)
    
    def __eq__(self, other: 'Update') -> bool:
        return isinstance(other, Update) and self.pages == other.pages

class Rules:

    def __init__(self, rules: List[Rule]):
        self._rules = rules
        self._map_for_first_pages = None
        self._map_for_second_pages = None
    
    @property
    def rules(self):
        return self._rules

    def make_maps_for_rules(self, updates: List[Update]) -> None:
        all_pages = set()
        for update in updates:
            for page in update:
                all_pages.add(page)

        map_for_first_pages = {page: set() for page in all_pages}
        map_for_second_pages = deepcopy(map_for_first_pages)
        for rule in self.rules:
            if rule.first in map_for_first_pages:
                map_for_first_pages[rule.first].add(rule)
            if rule.second in map_for_second_pages:
                map_for_second_pages[rule.second].add(rule)
        self._map_for_first_pages = map_for_first_pages
        self._map_for_second_pages = map_for_second_pages

    def with_first_page(self, page: int) -> list[Rule]:
        return self._map_for_first_pages[page]

    def with_second_page(self, page: int) -> list[Rule]:
        return self._map_for_second_pages[page]


def solution_part_01(input: str) -> str:
    raw_rules, updates = [line.strip() for line in input.split('\n\n') if line]

    rules = []
    for rule in raw_rules.split('\n'):
        if not rule:
            continue
        first, second = rule.strip().split('|')
        rules.append(Rule(int(first), int(second)))
    rules = Rules(rules)

    updates = [Update(update.strip().split(",")) for update in updates.split('\n') if update] 
    rules.make_maps_for_rules(updates)

    middle_pages = []
    for update in updates:
        if is_valid_update(update, rules):
            middle_pages.append(update.middle_page)
    
    return str(sum(middle_pages))

def is_valid_update(update: Update, rules: Rules) -> bool:
    rules_where_second_is_seen = []
    for page in update:
        rules_where_page_is_first = rules.with_first_page(page)
        for rule_where_page_is_first in rules_where_page_is_first:
            if rule_where_page_is_first in rules_where_second_is_seen:
                return False

        rules_where_page_is_second = rules.with_second_page(page)
        rules_where_second_is_seen.extend(rules_where_page_is_second)
    return True

def find_rules_where_page_is_second(page: int, first_pages_to_rules: Dict[int, List[Rule]]):
    return first_pages_to_rules[page]

def find_rules_where_page_is_first(page: int, second_pages_to_rules: Dict[int, List[Rule]]):
    return second_pages_to_rules[page]

def find_rules_for_page(page: int, rules: List[Rule]) -> List[Rule]:
    rules_for_page = []
    for rule in rules:
        if page in rule.pages:
            rules_for_page.append(rule)
    return rules_for_page

def solution_part_02(input: str) -> str:
    raw_rules, updates = [line.strip() for line in input.split('\n\n') if line]

    rules = []
    for rule in raw_rules.split('\n'):
        if not rule:
            continue
        first, second = rule.strip().split('|')
        rules.append(Rule(int(first), int(second)))
    rules = Rules(rules)

    updates = [Update(update.strip().split(",")) for update in updates.split('\n') if update] 
    rules.make_maps_for_rules(updates)

    middle_pages = []
    for update in updates:
        reordered_update = reorder(update, rules)
        if update == reordered_update:
            middle_pages(reordered_update.middlepage)
    return str(sum(middle_pages))

def reorder(update: Update, rules: Rules) -> Update:
    return