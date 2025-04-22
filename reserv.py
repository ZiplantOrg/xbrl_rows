import os
from lxml import etree
# Получить список файлов в директории
files = os.listdir('/home/vlad/Документы/xbrl_1_5_gb/test1')

#Параметры
count_double = 200000 # сколько осей нужно создать в  xbrl(максимум 1гб и 100.000строк на 61 колонку 6.000.000 показателей)
count_block =0 # концепт= уникальный код для контекста в концепте ( по умолчанию 0)
count_id_item = 0# концепт = уникальный код для каждого итема в концепте ( по умолчанию 0)
count_name_taxis = 0 # Контекст = taxis_ + (1) индентификатора дайменшина для открытой оси. ( по умолчанию 0)
count_name_taxis_and_id_ctx = -1 # !!!минус "-1" должен быть всегда!!!!! Контекст = taxis_ + (n) индентификатора дайменшина для открытой оси.  и ID ctx_(n) ( по умолчанию -1)
# Обработать каждый файл
for file in files:
    # Проверить, что файл имеет расширение .xbrl или .xml
    if file.endswith('.xbrl') or file.endswith('.xml'):
        # Загрузка XML файла
        tree = etree.parse('/home/vlad/Документы/xbrl_1_5_gb/test1/' + file)
        root = tree.getroot()

        # Найти блок <xbrli:context>
        context_block = root.find('.//{http://www.xbrl.org/2003/instance}context')
        count = 0
        purcb_elements = root.findall('.//{http://www.cbr.ru/xbrl/nso/purcb/dic/purcb-dic}*')
        # 1. Дублировать каждый элемент 3 раза в концептах
        for x in range(count_double):
            count_block += 1
            count +=1
            for purcb_element in purcb_elements:
                count_id_item += 1
                new_element = etree.fromstring(etree.tostring(purcb_element))
                new_element.attrib['contextRef'] = 'ctx_' + str(count_block)
                new_element.attrib['id'] = 'item_' + str(count_id_item)
                root.append(new_element)

            if count > 70000:
                tree.write('/home/vlad/Документы/xbrl_1_5_gb/test1/result/' + file, pretty_print=True, xml_declaration=True,
                           encoding='UTF-8')
                count = 0

        tree.write('/home/vlad/Документы/xbrl_1_5_gb/test1/result/' + file, pretty_print=True, xml_declaration=True,
                   encoding='UTF-8')
        count = 0

        # 2. Cоздает сктолько контекстов сколько концептов
        for i in range(count_block):
            count += 1
            count_name_taxis_and_id_ctx +=1

            new_block = etree.fromstring(etree.tostring(context_block))
            # Найти элемент <dim-int:ID_NomeraInformSoobshheniyaOSdelkeTypedName>
            id_element_dim = new_block.find(
                './/{http://www.xbrl.org/2003/instance}scenario/{http://xbrl.org/2006/xbrldi}typedMember/{http://www.cbr.ru/xbrl/udr/dim/dim-int}ID_NomeraInformSoobshheniyaOSdelkeTypedName')
            # Проверить, что элемент найден
            if id_element_dim is not None:
                # Изменить значение элемента
                id_element_dim.text = 'Taxis_' + str(int(id_element_dim.text.split('_')[1]) + count_name_taxis_and_id_ctx + 1)
                context_block.set('id', f'ctx_{count_name_taxis_and_id_ctx + 1}')
            # Добавить новый блок в корень
            root.append(new_block)

            if count > 70000:
                tree.write('/home/vlad/Документы/xbrl_1_5_gb/test1/result/' + file, pretty_print=True,
                           xml_declaration=True,
                           encoding='UTF-8')
                count = 0

        # Сохранить изменения в файл
        tree.write('/home/vlad/Документы/xbrl_1_5_gb/test1/result/' + file, pretty_print=True, xml_declaration=True, encoding='UTF-8')










import os
from lxml import etree
# Получить список файлов в директории
files = os.listdir('/home/vlad/Документы/xbrl_1_5_gb/test1')

#Параметры
count_double = 2 # сколько осей нужно создать в  xbrl(максимум 1гб и 100.000строк на 61 колонку 6.000.000 показателей)
count_block =0 # концепт= уникальный код для контекста в концепте ( по умолчанию 0)
count_id_item = 0# концепт = уникальный код для каждого итема в концепте ( по умолчанию 0)
count_name_taxis = 0 # Контекст = taxis_ + (1) индентификатора дайменшина для открытой оси. ( по умолчанию 0)
count_name_taxis_and_id_ctx = -1 # !!!минус "-1" должен быть всегда!!!!! Контекст = taxis_ + (n) индентификатора дайменшина для открытой оси.  и ID ctx_(n) ( по умолчанию -1)
# Обработать каждый файл
for file in files:
    # Проверить, что файл имеет расширение .xbrl или .xml
    if file.endswith('.xbrl') or file.endswith('.xml'):
        # Загрузка XML файла
        tree = etree.parse('/home/vlad/Документы/xbrl_1_5_gb/test1/' + file)
        root = tree.getroot()

        # Найти блок <xbrli:context>
        context_block = root.find('.//{http://www.xbrl.org/2003/instance}context')
        count = 0
        purcb_elements = root.findall('.//{http://www.cbr.ru/xbrl/nso/purcb/dic/purcb-dic}*')
        if not purcb_elements:
            # uk_dic_elements = root.findall('.//{http://www.cbr.ru/xbrl/nso/uk/dic}*')
            # srki_dic_elements = root.findall('.//{http://www.cbr.ru/xbrl/nso/srki/dic}*')
            # nfo_dic_elements = root.findall('.//{http://www.cbr.ru/xbrl/nso/nfo/dic}*')
            purcb_elements = root.findall('.//{http://www.cbr.ru/xbrl/nso/uk/dic}*')

        # 1. Дублировать каждый элемент 3 раза в концептахdd
        for x in range(count_double):
            count_block += 1
            count +=1
            for purcb_element in purcb_elements:
                count_id_item += 1
                new_element = etree.fromstring(etree.tostring(purcb_element))
                new_element.attrib['contextRef'] = 'ctx_' + str(count_block)
                new_element.attrib['id'] = 'item_' + str(count_id_item)
                root.append(new_element)

            if count > 70000:
                tree.write('/home/vlad/Документы/xbrl_1_5_gb/test1/result/' + file, pretty_print=True, xml_declaration=True,
                           encoding='UTF-8')
                count = 0

        tree.write('/home/vlad/Документы/xbrl_1_5_gb/test1/result/' + file, pretty_print=True, xml_declaration=True,
                   encoding='UTF-8')
        count = 0

        # 2. Cоздает сктолько контекстов сколько концептов
        for i in range(count_block):
            count += 1
            count_name_taxis_and_id_ctx +=1

            new_block = etree.fromstring(etree.tostring(context_block))
            id_element_dim = new_block.find(
                './/{http://www.xbrl.org/2003/instance}scenario/{http://xbrl.org/2006/xbrldi}typedMember/{http://www.cbr.ru/xbrl/udr/dim/dim-int}ID_NomeraInformSoobshheniyaOSdelkeTypedName')
            if not id_element_dim:
                id_element_dim = new_block.find(
                    './/{http://www.xbrl.org/2003/instance}scenario/{http://xbrl.org/2006/xbrldi}typedMember/{http://www.cbr.ru/xbrl/udr/dim/dim-int}TipCZennyxBumagAxis')
            # Проверить, что элемент найден
            if id_element_dim is not None:
                # Изменить значение элемента
                id_element_dim.text = 'Taxis_' + str(int(id_element_dim.text.split('_')[1]) + count_name_taxis_and_id_ctx + 1)
                context_block.set('id', f'ctx_{count_name_taxis_and_id_ctx + 1}')
            # Добавить новый блок в корень
            root.append(new_block)

            if count > 70000:
                tree.write('/home/vlad/Документы/xbrl_1_5_gb/test1/result/' + file, pretty_print=True,
                           xml_declaration=True,
                           encoding='UTF-8')
                count = 0

        # Сохранить изменения в файл
        tree.write('/home/vlad/Документы/xbrl_1_5_gb/test1/result/' + file, pretty_print=True, xml_declaration=True, encoding='UTF-8')



































# import os
# from lxml import etree
# # Получить список файлов в директории
# files = os.listdir('/home/vlad/Документы/xbrl_1_5_gb/test1')
#
# #Параметры
# count_double = 50000 # сколько осей нужно создать в  xbrl(максимум 1гб и 100.000строк на 61 колонку 6.000.000 показателей)
# count_block =10000 # концепт= уникальный код для контекста в концепте ( по умолчанию 0)
# count_id_item = 10000# концепт = уникальный код для каждого итема в концепте ( по умолчанию 0)
# count_name_taxis = 10000 # Контекст = taxis_ + (1) индентификатора дайменшина для открытой оси. ( по умолчанию 0)
# count_name_taxis_and_id_ctx = 99999 # !!!минус "-1" должен быть всегда!!!!! Контекст = taxis_ + (n) индентификатора дайменшина для открытой оси.  и ID ctx_(n) ( по умолчанию -1)
# # Обработать каждый файл
# for file in files:
#     # Проверить, что файл имеет расширение .xbrl или .xml
#     if file.endswith('.xbrl') or file.endswith('.xml'):
#         # Загрузка XML файла
#         tree = etree.parse('/home/vlad/Документы/xbrl_1_5_gb/test1/' + file)
#         root = tree.getroot()
#
#         # Найти блок <xbrli:context>
#         context_block = root.find('.//{http://www.xbrl.org/2003/instance}context')
#
#         purcb_elements = root.findall('.//{http://www.cbr.ru/xbrl/nso/purcb/dic/purcb-dic}*')
#         # 1. Дублировать каждый элемент 3 раза в концептах
#         for x in range(count_double):
#             count_block += 1
#             for purcb_element in purcb_elements:
#                 count_id_item += 1
#                 new_element = etree.fromstring(etree.tostring(purcb_element))
#                 new_element.attrib['contextRef'] = 'ctx_' + str(count_block)
#                 new_element.attrib['id'] = 'item_' + str(count_id_item)
#                 root.append(new_element)
#
#         # 2. Cоздает сктолько контекстов сколько концептов
#         for i in range(count_block):
#             count_name_taxis_and_id_ctx +=1
#
#             new_block = etree.fromstring(etree.tostring(context_block))
#             # Найти элемент <dim-int:ID_NomeraInformSoobshheniyaOSdelkeTypedName>
#             id_element_dim = new_block.find(
#                 './/{http://www.xbrl.org/2003/instance}scenario/{http://xbrl.org/2006/xbrldi}typedMember/{http://www.cbr.ru/xbrl/udr/dim/dim-int}ID_NomeraInformSoobshheniyaOSdelkeTypedName')
#             # Проверить, что элемент найден
#             if id_element_dim is not None:
#                 # Изменить значение элемента
#                 id_element_dim.text = 'Taxis_' + str(int(id_element_dim.text.split('_')[1]) + count_name_taxis_and_id_ctx + 1)
#                 context_block.set('id', f'ctx_{count_name_taxis_and_id_ctx + 1}')
#             # Добавить новый блок в корень
#             root.append(new_block)
#
#         # Сохранить изменения в файл
#         tree.write('/home/vlad/Документы/xbrl_1_5_gb/test1/result/' + file, pretty_print=True, xml_declaration=True, encoding='UTF-8')
#
#
# #
#
#
# import os
# from lxml import etree
# import xml.etree.ElementTree as ET
#
# # Получить список файлов в директории
# files = os.listdir('/home/vlad/Документы/xbrl_1_5_gb/test1')
#
# # Обработать каждый файл
# for file in files:
#     # Проверить, что файл имеет расширение .xbrl или .xml
#     if file.endswith('.xbrl') or file.endswith('.xml'):
#         # Загрузка XML файла
#         tree = etree.parse('/home/vlad/Документы/xbrl_1_5_gb/test1/' + file)
#         root = tree.getroot()
#
#         # Найти блок <xbrli:context>
#         context_block = root.find('.//{http://www.xbrl.org/2003/instance}context')
#
#         count_double = 20
#
#         purcb_elements = root.findall('.//{http://www.cbr.ru/xbrl/nso/purcb/dic/purcb-dic}*')
#         # Дублировать каждый элемент 3 раза
#         s = 0
#         сount_block = 0
#         for x in range(count_double):
#             сount_block += 1
#             for purcb_element in purcb_elements:
#                 s += 1
#                 new_element = etree.fromstring(etree.tostring(purcb_element))
#                 new_element.attrib['contextRef'] = 'ctx_' + str(сount_block)
#                 new_element.attrib['id'] = 'item_' + str(s)
#                 root.append(new_element)
#
#             # Дублировать блок 3 раза
#         for i in range(сount_block):
#             new_block = etree.fromstring(etree.tostring(context_block))
#             # Найти элемент <dim-int:ID_NomeraInformSoobshheniyaOSdelkeTypedName>
#             id_element_dim = new_block.find(
#                 './/{http://www.xbrl.org/2003/instance}scenario/{http://xbrl.org/2006/xbrldi}typedMember/{http://www.cbr.ru/xbrl/udr/dim/dim-int}ID_NomeraInformSoobshheniyaOSdelkeTypedName')
#             # Проверить, что элемент найден
#             if id_element_dim is not None:
#                 # Изменить значение элемента
#                 id_element_dim.text = 'Taxis_' + str(int(id_element_dim.text.split('_')[1]) + i + 1)
#                 context_block.set('id', f'ctx_{i + 1}')
#             # Добавить новый блок в корень
#             root.append(new_block)
#
#         # Сохранить изменения в файл
#         tree.write('/home/vlad/Документы/xbrl_1_5_gb/test1/result/' + file, pretty_print=True, xml_declaration=True,
#                    encoding='UTF-8')








    # for x, element in enumerate(root.iter()):
      #       if element.tag.startswith('{http://www.cbr.ru/xbrl/nso/purcb/dic/purcb-dic}'):
      #           for j in range(count_double):
      #               new_element = etree.Element(element.tag, element.attrib)
      #               new_element.attrib['contextRef'] = 'ctx_' + str(x + 1)
      #               new_element.attrib['id'] = 'item_' + str(x + 1)
      #               root.append(new_element)
      #





#
#
# import os
# from lxml import etree
#
# # Получить список файлов в директории
# files = os.listdir('/home/vlad/Документы/xbrl_1_5_gb/test1')
#
# # Обработать каждый файл
# for file in files:
#     # Проверить, что файл имеет расширение .xbrl или .xml
#     if file.endswith('.xbrl') or file.endswith('.xml'):
#         # Загрузка XML файла
#         tree = etree.parse('/home/vlad/Документы/xbrl_1_5_gb/test1/' + file)
#         root = tree.getroot()
#
#         # Найти блок <xbrli:context>
#         context_block = root.find('.//{http://www.xbrl.org/2003/instance}context')
#         # Найти блок <purcb-dic:VnebirzhSdelka>
#         vnebirzh_sdelka_block = root.find('.//{http://www.cbr.ru/xbrl/nso/purcb/dic/purcb-dic}VnebirzhSdelka')
#         # Дублировать блок 3 раза
#         for i in range(3):
#             new_block = etree.fromstring(etree.tostring(context_block))
#             # Найти элемент <dim-int:ID_NomeraInformSoobshheniyaOSdelkeTypedName>
#             id_element_dim = new_block.find(
#                 './/{http://www.xbrl.org/2003/instance}scenario/{http://xbrl.org/2006/xbrldi}typedMember/{http://www.cbr.ru/xbrl/udr/dim/dim-int}ID_NomeraInformSoobshheniyaOSdelkeTypedName')
#             new_block_concept = etree.fromstring(etree.tostring(vnebirzh_sdelka_block))
#             # Изменить значение в contextRef
#             new_block_concept.attrib['contextRef'] = 'ctx_' + str(i + 1)
#             # Изменить значение в id
#             new_block_concept.attrib['id'] = 'item_' + str(i + 1)
#             root.append(new_block_concept)
#
#             # Проверить, что элемент найден
#             if id_element_dim is not None:
#                 # Изменить значение элемента
#                 id_element_dim.text = 'Taxis_' + str(int(id_element_dim.text.split('_')[1]) + i + 1)
#                 context_block.set('id', f'ctx_{i + 1}')
#             # Добавить новый блок в корень
#             root.append(new_block)
#
#         # Сохранить изменения в файл
#         tree.write('/home/vlad/Документы/xbrl_1_5_gb/test1/result/' + file, pretty_print=True, xml_declaration=True, encoding='UTF-8')
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#










# import os
# from lxml import etree
#
# # Получить список файлов в директории
# files = os.listdir('/home/vlad/Документы/xbrl_1_5_gb/test1')
#
# # Обработать каждый файл
# for file in files:
#     # Проверить, что файл имеет расширение .xbrl или .xml
#     if file.endswith('.xbrl') or file.endswith('.xml'):
#         # Загрузка XML файла
#         tree = etree.parse('/home/vlad/Документы/xbrl_1_5_gb/test1/' + file)
#         root = tree.getroot()
#
#         # Найти блок <xbrli:context>
#         context_block = root.find('.//{http://www.xbrl.org/2003/instance}context')
#
#         # Дублировать блок 3 раза
#         for i in range(3):
#             new_block = etree.fromstring(etree.tostring(context_block))
#             # Найти элемент <dim-int:ID_NomeraInformSoobshheniyaOSdelkeTypedName>
#
#             # id_element_ctx = root.find(
#             #     './/{http://www.xbrl.org/2003/instance}context[@id="ctx_3ef9ba1955544d373419e57e7596c2ba"]')
#             id_element_dim = new_block.find(
#                 './/{http://www.xbrl.org/2003/instance}scenario/{http://xbrl.org/2006/xbrldi}typedMember/{http://www.cbr.ru/xbrl/udr/dim/dim-int}ID_NomeraInformSoobshheniyaOSdelkeTypedName')
#
#             # Проверить, что элемент найден
#             if id_element_dim is not None:
#                 # Изменить значение элемента
#                 id_element_dim.text = 'Taxis_' + str(int(id_element_dim.text.split('_')[1]) + i + 1)
#                 # id_element_dim.attrib['id'] = 'ctx_' + str(int(id_element_dim.text.split('_')[1]) + i + 1)
#                 context_block.set('id', f'ctx_{i + 1}')
#             # Добавить новый блок в корень
#             root.append(new_block)
#
#         # Сохранить изменения в файл
#         tree.write('/home/vlad/Документы/xbrl_1_5_gb/test1/result/' + file, pretty_print=True, xml_declaration=True, encoding='UTF-8')




