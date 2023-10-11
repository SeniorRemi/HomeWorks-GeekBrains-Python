from return_data_file import data_file 

def copy_data():
    data_1, nf_1 = data_file()
    data_length = len(data_1)

    if data_length == 0:
        print("Из файла нечего копировать!")
        return

    input_user = int(input(f"Введите номер строки \nот 1 до {data_length}: "))

    while input_user < 1 or input_user > data_length:
        input_user = int(input(f"Введите номер строки \nот 1 до {data_length}: "))

    print("\nКуда хотите копировать?")
    data_2, nf_2 = data_file()
    data_2_length = len(data_2)

    data_line = [
        f'{data_2_length + 1};',
        data_1[input_user - 1].split(";")[1],
        data_1[input_user - 1].split(";")[2],
        data_1[input_user - 1].split(";")[3],
        data_1[input_user - 1].split(";")[4]
    ]
    
    final_string = ";".join(data_line)
    
    with open(f'db/data_{nf_2}.txt', 'a', encoding='utf-8') as file:
        file.write(final_string)

    print("Данные успешно скопированы! \n")

copy_data()

