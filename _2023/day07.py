from collections import Counter
import sys
import time
from typing import List, Union

JOKER = 'J'

class HandType:
    KIND = "{}_of_a_kind"
    FIVE_OF_A_KIND = KIND.format('five')
    FOUR_OF_A_KIND = KIND.format('four')
    FULL_HOUSE = 'full_house'
    THREE_OF_A_KIND = KIND.format('three')
    PAIR = '{}_pair'
    TWO_PAIR = PAIR.format('two')
    ONE_PAIR = PAIR.format('one')
    HIGH_CARD = 'high_card'
    
    ORDER = [
        FIVE_OF_A_KIND,
        FOUR_OF_A_KIND,
        FULL_HOUSE,
        THREE_OF_A_KIND,
        TWO_PAIR,
        ONE_PAIR,
        HIGH_CARD
    ]
    
    @staticmethod
    def _find(hand: 'Hand') -> str:
        hand_counter = hand.counter
        
        hand_contains_joker = hand.is_j_joker and JOKER in hand.cards
                
        if all(v == 1 for v in hand_counter.values()):
            if not hand_contains_joker:
                return HandType.HIGH_CARD
            return HandType.ONE_PAIR
        
        if all(v == 5 for v in hand_counter.values()):
            return HandType.FIVE_OF_A_KIND
        
        if any(v == 4 for v in hand_counter.values()):
            if not hand_contains_joker:
                return HandType.FOUR_OF_A_KIND
            return HandType.FIVE_OF_A_KIND
        
        number_of_pairs = len([v for v in hand_counter.values() if v == 2])
        if number_of_pairs == 2:
            if not hand_contains_joker:
                return HandType.TWO_PAIR
            
            if hand.counter[JOKER] == 1:
                return HandType.FULL_HOUSE
            
            return HandType.FOUR_OF_A_KIND
        
        number_of_triplets = len([v for v in hand_counter.values() if v == 3])
        if number_of_triplets == 1 and number_of_pairs == 1:
            if not hand_contains_joker:
                return HandType.FULL_HOUSE
            return HandType.FIVE_OF_A_KIND
        
        if number_of_triplets == 1 and number_of_pairs == 0:
            if not hand_contains_joker:
                return HandType.THREE_OF_A_KIND
            return HandType.FOUR_OF_A_KIND
        
        if not hand_contains_joker:
            return HandType.ONE_PAIR
        return HandType.THREE_OF_A_KIND
        
    
    @staticmethod
    def rank(hand: 'Hand') -> int:
        hand_type = HandType._find(hand)
        rank = len(HandType.ORDER) - HandType.ORDER.index(hand_type)
        return rank


class Hand:
    LABELS = '23456789TJQKA'
    
    def __init__(self, cards: str, bid: int) -> None:
        self.cards: str = cards
        self.bid: int = bid
        self.counter: Counter = Counter(cards) 
        self._type_rank: Union[None, int] = None
    
    @property
    def is_j_joker(self) -> bool:
        return False
    
    def __gt__(self, other: 'Hand') -> bool:
        if self.type_rank > other.type_rank:
            return True
        if self.type_rank < other.type_rank:
            return False
        cards_paired = zip(self.cards, other.cards)
        for left_card, right_card in cards_paired:
            if left_card == right_card:
                continue
            assert self.cards != other.cards, 'Two hands cannot be the identical'
            return self.LABELS.index(left_card) > other.LABELS.index(right_card)
    
    def __lt__(self, other: 'Hand') -> bool:
        return not(self > other)
    
    def __eq__(self, _: 'Hand') ->bool:
        raise Exception('Two hands cannot be equal. Why are you checking they are?')

    @property
    def type_rank(self) -> int:
        if self._type_rank is not None:
            return self._type_rank
        
        type_rank = HandType.rank(self)
        self._type_rank = type_rank
        return type_rank

class Hand2(Hand):
    LABELS = 'J23456789TQKA'
    
    @property
    def is_j_joker(self) -> bool:
        return True
    
def get_hands(lines: List[str], hand_ojc: Hand = Hand) -> List[Hand]:
    hands = []
    for line in lines:
        cards, bid = line.strip().split(' ')
        hand = hand_ojc(cards, int(bid))
        hands.append(hand)
    return hands

def get_winnings_from_sorted_hands(sorted_hands: List[Hand]) -> List[int]:
    all_winnings = []
    for hand_rank, hand in enumerate(sorted_hands, 1):
        winnings = hand_rank * hand.bid
        all_winnings.append(winnings)
    return all_winnings
    
def pt1(lines):
    hands = get_hands(lines)
    sorted_hands = sorted(hands)
    winnings = get_winnings_from_sorted_hands(sorted_hands)
    return sum(winnings)

def pt2(lines):
    hands = get_hands(lines, Hand2)
    sorted_hands = sorted(hands)
    winnings = get_winnings_from_sorted_hands(sorted_hands)
    return sum(winnings)
        

if __name__ == '__main__':
    file_path = sys.argv[1]
    with open(file_path, 'r') as file:
        lines = file.read().strip().split('\n')

    start = time.time()
    print('=' * 10)
    print(f'Part 1: {pt1(lines)}')
    end = time.time()
    print('.' * 10)
    print(f'Part 1 took {end - start}')
    print('=' * 10)
    start = time.time()
    print(f'Part 2: {pt2(lines)}')
    end = time.time()
    print('.' * 10)
    print(f'Part 2 took {end - start}')
    print('=' * 10)