"""
В текстовый файл построчно записаны имя и фамилия учащихся класса и их оценки.

Андрей Говорухи 6 6 1 4 9 9 10 4 8 2 3 8
Василий Петров 2 9 4 7 6 6 3 6 5 5 2 4
Гавриил Варфаломеев 10 10 4 10 7 9 4 6 8 1 1 1
Игнат Тюльпанов 8 1 4 1 1 5 2 5 2 2 10 8
Илья Муромцев 1 6 4 7 10 9 5 3 7 4 7 2
Кощей Бессмертный 3 10 1 4 1 8 10 6 2 10 7 4
Максим Мухин 10 8 9 9 5 8 6 5 7 2 4 10
Маргарита Мартынова 9 1 5 1 10 10 2 4 4 9 8 10
Петр Николаев 2 9 5 9 1 2 8 7 8 1 9 1
Полина Гусева 9 2 8 7 3 9 9 5 1 9 2 6
Спиридов Тереньтьев 4 7 7 3 10 9 7 2 10 9 8 1
Станислав Трердолобов 8 1 6 1 4 1 10 8 8 1 8 8

Вывести на экран всех учащихся, чей средний балл меньше 5, также посчитать и вывести
средний балл по классу. Так же,
записать в новый файл всех учащихся в формате "Фамилия И. Ср. балл"
"""

file_name_in = 'src.txt'
file_name_out = 'dst.txt'

template = '{name:<25}{avr:<7}\n'

with open(file_name_in, encoding='utf-8') as src, open(file_name_out, 'w', encoding='utf-8') as dst:
    avr_per_class = 0
    cnt = 0
    for line in src:
        tmp = line.strip('\n').strip().split()
        avr_per_st = round(sum([int(x) for x in tmp[2:]]) / len(tmp[2:]), 2)
        avr_per_class += avr_per_st
        cnt += 1
        st_name = tmp[1] + ' ' + tmp[0][0] + '.'
        str_out = template.format(name=st_name, avr=avr_per_st)

        dst.write(str_out)
        if avr_per_st <= 5.0:
            print(str_out, end='')

    print('Average per class:', round(avr_per_class / cnt, 2))
