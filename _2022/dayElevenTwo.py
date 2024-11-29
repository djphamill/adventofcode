import sys

def solution(input_text):

    lines = input_text.split('\n')

    number_of_monkeys = int((len(lines) + 1) / 7)
    monkey_lines = [lines[i * 7:i * 7 + 6] for i in range(number_of_monkeys)]

    monkeys = {}
    for monkey in monkey_lines:
        monkey_number = int(monkey[0][:-1].split(' ')[-1])
        starting_items = [int(i) for i in monkey[1][monkey[1].find(':')+1:].split(', ')]
        operation = monkey[2][monkey[2].find('old ')+4:].split(' ')
        divisibility_test = int(monkey[3].split(' ')[-1])
        throw_to = {
            'true': int(monkey[4].split(' ')[-1]),
            'false': int(monkey[5].split(' ')[-1]),
        }
        monkeys[monkey_number] = {
            'starting_items': starting_items,
            'operation': {
                'operator': operation[0],
                'operand': operation[1],
            },
            'divisibility_test': divisibility_test,
            'throw_to': throw_to,
            'number_of_handled_items': 0
        }

    divisibility_tests = [monkeys[monkey]['divisibility_test'] for monkey in range(number_of_monkeys)]

    # Rewrite starting items so each item is a list, each element of which is an equivalent value for the monkey of that index
    for monkey in monkeys:
        items = []
        for starting_item in monkeys[monkey]['starting_items']:
            items.append([starting_item % d for d in divisibility_tests])

        monkeys[monkey]['starting_items'] = items
    
    for turn in range(1, 10001):
        for monkey_number in range(number_of_monkeys):
            i = len(monkeys[monkey_number]['starting_items'])
            for _ in range(i):
                monkeys[monkey_number]['number_of_handled_items'] += 1

                current_item_list = monkeys[monkey_number]['starting_items'][0]
                monkeys[monkey_number]['starting_items'] = monkeys[monkey_number]['starting_items'][1:]

                if monkeys[monkey_number]['operation']['operand'] == 'old':
                    operands = current_item_list
                else:
                    operands = [monkeys[monkey_number]['operation']['operand'] for i in range(len(divisibility_tests))]

                new_value_list = []
                for monkey in range(number_of_monkeys):
                    new_value_list.append(eval(f"({current_item_list[monkey]}{monkeys[monkey_number]['operation']['operator']}{operands[monkey]}) % {divisibility_tests[monkey]}"))

                if new_value_list[monkey_number] % monkeys[monkey_number]['divisibility_test'] == 0:
                    monkey_to_pass_to = monkeys[monkey_number]['throw_to']['true']
                else:
                    monkey_to_pass_to = monkeys[monkey_number]['throw_to']['false']
                
                # check if passing to a monkey that squares
                monkeys[monkey_to_pass_to]['starting_items'].append(new_value_list)
        
        if turn % 1000 == 0: 
            print(f'turn: {turn}')
            for monkey in monkeys:
                print(f"Monkey {monkey} inspected items {monkeys[monkey]['number_of_handled_items']} times")
                
                

    all_totals_sorted = sorted([monkeys[i]['number_of_handled_items'] for i in range(number_of_monkeys)], reverse=True)
    
    return all_totals_sorted[0] * all_totals_sorted[1]

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit('Provide some an input file.')
    
    input_file_path = sys.argv[1]

    with open(input_file_path, 'r') as f:
        input_text = f.read()

    print(f'Solution is: {solution(input_text)}')



    