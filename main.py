# идентификатор должен быть создан   "Taxis_1"
import os
from lxml import etree
from concept import data_cnc
from context import data_ctx
import  datetime


start = datetime.datetime.now()
#Параметры
count_double = 1000 # сколько осей нужно создать в  xbrl(максимум 1гб и 100.000строк на 61 колонку 6.000.000 показателей)
count_block =0 # концепт= уникальный код для контекста в концепте ( по умолчанию 0)
count_id_item = 0# концепт = уникальный код для каждого итема в концепте ( по умолчанию 0)
count_name_taxis = 0 # Контекст = taxis_ + (1) индентификатора дайменшина для открытой оси. ( по умолчанию 0)
count_name_taxis_and_id_ctx = 0 # !!! убрал минус 1! Контекст = taxis_ + (n) индентификатора дайменшина для открытой оси.  и ID ctx_(n) ( по умолчанию -1)
count_save = 0
# Обработать каждый файл

# Получить список файлов в директории
path_folder = '/home/vlad/Документы/xbrl_1_5_gb/test1/'
# получает файлы из деректории:
files = os.listdir(path_folder)
for file in files:
    # Проверить, что файл имеет расширение .xbrl или .xml
    if file.endswith('.xbrl') or file.endswith('.xml'):
        # Загрузка XML файла
        tree = etree.parse(path_folder + file)
        root = tree.getroot()

        # Найти блок <xbrli:context>
        context_block = root.find('.//{http://www.xbrl.org/2003/instance}context')
        count = 0
        # Получить список концептов.
        for key, value in data_cnc.items():
            print(f"Ключ: {key}, Значение: {value}")
            elements = root.findall(value)
            if elements:  # проверяем, является ли elements пустым списком
                break

        # 1. Дублировать каждый элемент 3 раза в концептах
        for x in range(count_double):
            count_block += 1
            count += 1
            print(f'--------------------сохранение_cnc {count}-------------')
            # сохраняем все дочерние элементы и файл
            tree.write(f'{path_folder}result/' + file, pretty_print=True, xml_declaration=True, encoding='UTF-8')

            # открываем файл для продолжения записи
            tree = etree.parse(f'{path_folder}result/' + file)
            root = tree.getroot()

            # продолжаем запись
            for purcb_element in (etree.fromstring(etree.tostring(purcb_element)) for purcb_element in elements):
                count_id_item += 1
                count_save += 1
                new_element = purcb_element
                new_element.attrib['contextRef'] = 'ctx_' + str(count_block)
                new_element.attrib['id'] = 'item_' + str(count_id_item)
                root.append(new_element)
                # если больше 100000 строк -- сохранить
                if count_save == 400000:  # проверяем, является ли счетчик кратным 100
                    tree.write(f'{path_folder}result/' + file, pretty_print=True, xml_declaration=True,
                               encoding='UTF-8')
                    print(f'--------------------сохранение_cnc_100000  {count}-------------')
                    # root.clear()  # очищаем root после сохранения
                    count_save = 0

        count_save= 0
        tree.write(f'{path_folder}/result/' + file, pretty_print=True, xml_declaration=True, encoding='UTF-8')
        count = 0
        elements.clear()  # удаляем первый элемент из списка после его обработки (особождаем ОЗУ)

        # 2. Cоздает сктолько контекстов сколько концептов

        for i in range(count_block):
            count += 1
            print(f'--------------------сохранение_cnc {count}-------------')
            count_name_taxis_and_id_ctx += 1
            new_block = etree.fromstring(etree.tostring(context_block))
            # Получить список контекстов
            for key, value in data_ctx.items():
                print(f"Ключ: {key}, Значение: {value}")
                id_element_dim = new_block.find(value)
                if id_element_dim is not None:
                    break
            try:
                # Проверить, что элемент найден
                if id_element_dim is not None:
                    # Изменить значение элемента
                    id_element_dim.text = 'Taxis_' + str(
                        int(id_element_dim.text.split('_')[1]) + count_name_taxis_and_id_ctx + 1)
                    new_block.set('id', f'ctx_{count_name_taxis_and_id_ctx}')
                # Добавить новый блок в корень
                root.append(new_block)
            except Exception as e:
                print(f"Ошибка: {e}")
                print("Идентификатор должен быть создан 'Taxis_1'")
                print('Cчет_контектов: ', count_name_taxis_and_id_ctx)
            if  count_save == 70000:
                tree.write(f'{path_folder}/result/' + file, pretty_print=True,
                           xml_declaration=True,
                           encoding='UTF-8')
                count = 0

        # Сохранить изменения в файл
        tree.write(f'{path_folder}/result/' + file, pretty_print=True, xml_declaration=True, encoding='UTF-8')
        end = datetime.datetime.now()
        total_time = end - start
        print('Завершилось: ',total_time )

        # # 1. Дублировать каждый элемент 3 раза в концептах
        # for x in range(count_double):
        #     count_block += 1
        #     count += 1
        #     print(f'--------------------сохранение_cnc {count}-------------')
        #     for purcb_element in (etree.fromstring(etree.tostring(purcb_element)) for purcb_element in elements):
        #         count_id_item += 1
        #         count_save += 1
        #         new_element = purcb_element
        #         new_element.attrib['contextRef'] = 'ctx_' + str(count_block)
        #         new_element.attrib['id'] = 'item_' + str(count_id_item)
        #         root.append(new_element)
        #         # если больше 100000 строк -- сохранить
        #         if count_save == 100:  # проверяем, является ли счетчик кратным 100
        #             tree.write(f'{path_folder}result/' + file, pretty_print=True, xml_declaration=True,
        #                        encoding='UTF-8', ),
        #             print(f'--------------------сохранение_cnc_100000  {count}-------------')
        #             # count = 0
        #             count_save = 0
        # count_save = 0
        # tree.write(f'{path_folder}/result/' + file, pretty_print=True, xml_declaration=True, encoding='UTF-8')
        # count = 0
        # elements.clear()  # удаляем первый элемент из списка после его обработки (особождаем ОЗУ)