# идентификатор должен быть создан   "Taxis_1"
import os
from lxml import etree
from concept import data_cnc
from context import data_ctx
import  datetime
import xml.etree.ElementTree as ET
from lxml import etree as ET
import re

start = datetime.datetime.now()
#Параметры
count_double = 30 # сколько осей нужно создать в  xbrl(максимум 1гб и 100.000строк на 61 колонку 6.000.000 показателей)
count_block =0 # концепт= уникальный код для контекста в концепте ( по умолчанию 0)
count_id_item = 0# концепт = уникальный код для каждого итема в концепте ( по умолчанию 0)
count_name_taxis = 0 # Контекст = taxis_ + (1) индентификатора дайменшина для открытой оси. ( по умолчанию 0)
count_name_taxis_and_id_ctx = 0 # !!! убрал минус 1! Контекст = taxis_ + (n) индентификатора дайменшина для открытой оси.  и ID ctx_(n) ( по умолчанию -1)
count_save = 0
count_save_name = 0
# Обработать каждый файл

# Получить список файлов в директории
path_folder = '/home/vlad/Документы/xbrl_1_5_gb/test1/'
path_folder_ctx = '/home/vlad/Документы/xbrl_1_5_gb/test1/result'
path_folder_ctc = '/home/vlad/Документы/xbrl_1_5_gb/test1/result'
path_folder_itog =  '/home/vlad/Документы/xbrl_1_5_gb/test1/result'

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

        # 1. Дублировать каждый концепт столько раз сколько указано в count_double
        for x in range(count_double):
            count_block += 1
            count += 1
            # обрабоат каждый элемент
            for purcb_element in elements:
                count_id_item += 1
                new_element = etree.fromstring(etree.tostring(purcb_element))
                new_element.attrib['contextRef'] = 'ctx_' + str(count_block)
                new_element.attrib['id'] = 'item_' + str(count_id_item)
                # root.append(new_element)

                file_name = 'concept.txt'
                file_path = os.path.join(path_folder_ctc, file_name)

                # Создайте директорию, если она не существует
                os.makedirs(path_folder_ctc, exist_ok=True)

                with open(file_path, 'ab') as f:

                    # Преобразуйте элемент в строку
                    element_str = ET.tostring(new_element, pretty_print=True, xml_declaration=True,
                                              encoding='UTF-8').decode(
                        'utf-8')
                    # Удалите нежелательные ссылки из строки
                    element_str = re.sub(r'xmlns:[^"]+="[^"]+"', '', element_str).strip()
                    element_str = element_str.replace(" ", "")
                    # Удалите строку <?xml version='1.0' encoding='UTF-8'?>
                    element_str = re.sub(r'<\?xml[^>]*\?>', '', element_str).strip()
                    # запись файла
                    f.write((element_str + '\n').encode('utf-8'))

        # 1. Дублировать контекст  столько раз сколько указано в count_double
        new_block = etree.fromstring(etree.tostring(context_block))
        # Получить список контекстов
        for key, value in data_ctx.items():
            print(f"Ключ: {key}, Значение: {value}")
            id_element_dim = new_block.find(value)
            if id_element_dim is not None:
                break

        for i in range(count_block):
            count += 1
            print(f'--------------------сохранение_cnc {count}-------------')
            count_name_taxis_and_id_ctx += 1


            try:
                # Проверить, что элемент найден
                if id_element_dim is not None:
                    # Изменить значение элемента
                    id_element_dim.text = 'Taxis_' + str(
                        int(id_element_dim.text.split('_')[1]) + count_name_taxis_and_id_ctx + 1)
                    new_block.set('id', f'ctx_{count_name_taxis_and_id_ctx}')
                # Добавить новый блок в корень
                # root.append(new_block)

                file_name = 'context.txt'
                file_path = os.path.join(path_folder_ctx, file_name)

                # Создайте директорию, если она не существует
                os.makedirs(path_folder_ctx, exist_ok=True)

                with open(file_path, 'ab') as f:

                    # Преобразуйте элемент в строку
                    element_str = ET.tostring(new_block, pretty_print=True, xml_declaration=True,
                                              encoding='UTF-8').decode(
                        'utf-8')
                    # Удалите нежелательные ссылки из строки
                    element_str = re.sub(r'xmlns:[^"]+="[^"]+"', '', element_str).strip()
                    element_str = element_str.replace(" ", "")
                    # Удалите строку <?xml version='1.0' encoding='UTF-8'?>
                    element_str = re.sub(r'<\?xml[^>]*\?>', '', element_str).strip()
                    # запись файла
                    f.write((element_str + '\n').encode('utf-8'))
            except Exception as e:
                print(f"Ошибка: {e}")
                print("Идентификатор должен быть создан 'Taxis_1'")
                print('Cчет_контектов: ', count_name_taxis_and_id_ctx)





        end = datetime.datetime.now()
        total_time = end - start
        print('Завершилось: ',total_time )






