def validate_pattern(crafts, pattern_rules, card_stack_size):
    sum_of_crafts = 0

    for craft in crafts:
        sum_of_crafts += craft - card_stack_size / 2
    return {
        "threshold_reached": sum_of_crafts > pattern_rules["threshold"],
        "max_burn_reached": sum_of_crafts < pattern_rules["max_burn"],
    }
