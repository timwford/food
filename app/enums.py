from enum import Enum, unique, auto


class AutoNameEnum(Enum):
    def _generate_next_value_(name, start, count, last_values):
        return name.lower()


#
# Recipe Attributes
#

Meal = AutoNameEnum('Meal', 'SNACK DESSERT BREAKFAST LUNCH DINNER')
Complexity = AutoNameEnum('Complexity', 'EASY MEDIUM HARD')
Time = AutoNameEnum('Time', 'SHORT MEDIUM LONG ALL_DAY')
Method = AutoNameEnum('Method', 'PRESSURE SLOW_COOK BAKE MICROWAVE')

#
# Definitions
#

Measurement = AutoNameEnum('Measurement', 'CUP TABLESPOON TEASPOON')

if __name__ == "__main__":
    print(list(Meal))
    print(list(Complexity))
