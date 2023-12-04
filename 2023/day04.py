import re
import sys
from math import pow
from dataclasses import dataclass
from typing import Set, Dict, List

def pt1(lines):
    total = 0
    game_pattern = r'Card\s+\d+:'
    games = [re.sub(game_pattern, '', line) for line in lines]
    for game in games:
        cards = game.split('|')
        winning_numbers, our_numbers = [set(re.findall(r'\d+', card)) for card in cards]
        
        card_points = 0
        overlap = len(winning_numbers.intersection(our_numbers))
        if overlap:
            card_points = int(pow(2, overlap - 1))
        total += card_points
        
    return total

@dataclass
class Card:
    id: int
    winning_numbers: Set[str]
    our_numbers: Set[str]
    copies: int = 1
    
    def add_copy(self) -> None:
        self.copies += 1
    
    def matching_numbers_count(self) -> int:
        return len(self.winning_numbers.intersection(self.our_numbers)) 

def add_copies_from_card(trigger_card: Card, number_of_cards_to_copy: int, cards: Dict[int, Card]):
    cards_to_copy = range(trigger_card.id + 1, trigger_card.id + number_of_cards_to_copy + 1)
    for card_id in cards_to_copy:
        card = cards.get(card_id)
        if not card:
            continue
        for _ in range(trigger_card.copies):
            card.add_copy()

def get_all_cards(lines: List[str]) -> Dict[int, Card]:
    cards = dict()
    for line in lines:
        card_id = int(line.split(':')[0].replace('Card', '').strip())
        
        winning_numbers, our_numbers = [set(re.findall(r'\d+', card.strip())) for card in line.split(':')[1].strip().split('|')]
        
        card = Card(card_id, winning_numbers, our_numbers)
        cards.update({card_id: card})
    
    return cards

def pt2(lines):
    cards = get_all_cards(lines)
    for card in cards.values():
        number_of_cards_to_copy = card.matching_numbers_count()
        add_copies_from_card(card, number_of_cards_to_copy, cards)
        
    return(sum([card.copies for card in cards.values()]))

if __name__ == '__main__':
    file_path = sys.argv[1]
    with open(file_path, 'r') as file:
        lines = file.read().strip().split('\n')
    print(f'Part 1: {pt1(lines)}')
    print(f'Part 2: {pt2(lines)}')