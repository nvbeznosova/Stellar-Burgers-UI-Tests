types = {
    1: 'Блокирующий',
    2: 'Критический',
    3: 'Значительный',
    4: 'Незначительный',
    5: 'Тривиальный'
}

tickets = {
    1: ['API_45', 'API_76', 'E2E_4'],
    2: ['UI_19', 'API_65', 'E2E_45'],
    3: ['E2E_2'],
    4: ['E2E_9'],
    5: ['API_61']
}

def unique_list(lst):
    return list(dict.fromkeys(lst))

def map_tickets(types, tickets):
    seen = set()
    result = {}
    for level in sorted(types.keys()):
        unique_tickets = unique_list(tickets.get(level, []))
        filtered = [t for t in unique_tickets if t not in seen]
        result[types[level]] = filtered
        seen.update(filtered)
    return result

tickets_by_type = map_tickets(types, tickets)

print(tickets_by_type)