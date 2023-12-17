class Pyramid:

    def __init__(self, name):
        self.name = name
        self.middle_dict = {}
        self.result_dict = {}
        self.current_str = ''

    def __str__(self):
        return self.name

    def to_output_format(self):
        """
        Функция формирует строку для вывода после
        первого сжатия.
        """
        dictionary_list = [k * v for k, v in self.result_dict.items()]
        dictionary_string = ''.join(dictionary_list)
        self.current_str = dictionary_string
        self.result_dict.clear()
        with open('output.txt', 'a+') as o:
            o.write(dictionary_string + '\n')
        o.close()
        return dictionary_string

    def input_take(self):
        """
        Функция принимает входные данные и производит их сжатие
        согласно инструкции.
        """
        if len(self.current_str) == 0:
            with open('input.txt', 'r') as i:
                input_text = i.read()[:-1:]
        else:
            input_text = self.current_str
        for x in input_text:
            if x not in self.middle_dict:
                self.middle_dict[x] = 1
            else:
                self.middle_dict[x] += 1
                if self.middle_dict[x] >= 4:
                    if x not in self.result_dict:
                        self.result_dict[x] = 1
                    else:
                        self.result_dict[x] += 1
                    self.middle_dict.pop(x)
                else:
                    continue
        for letter in set(input_text):
            if letter not in self.result_dict.keys():
                with open('output.txt', 'a+') as out:
                    out.write('Еще больше сжать уже нельзя! Конец сжатия.' + '\n')
                out.close()
                break
            else:
                continue
        return self.to_output_format()


first_example = Pyramid(name='Первый преобразователь (не мститель)')
