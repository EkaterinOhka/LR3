# TODO Напишите функцию find_common_participants
def find_common_participants(participants1, participants2, separator=','):
    splited_part1 = participants1.split(separator)
    splited_part2 = participants2.split(separator)
    final_list = set(splited_part1) & set(splited_part2)
    return sorted(final_list)


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
print(f"Общий список имеет вид: {find_common_participants(participants_first_group, participants_second_group, '|')}")
