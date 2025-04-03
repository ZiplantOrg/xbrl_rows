import os
from lxml import etree

# Получить список файлов в директории
files = os.listdir('/home/vlad/Документы/xbrl_1_5_gb/test1')

# Обработать каждый файл
for file in files:
    # Проверить, что файл имеет расширение .xbrl или .xml
    if file.endswith('.xbrl') or file.endswith('.xml'):
        # Загрузка XML файла
        tree = etree.parse('/home/vlad/Документы/xbrl_1_5_gb/test1/' + file)
        root = tree.getroot()

        # Найти блок <xbrli:context>
        context_block = root.find('.//{http://www.xbrl.org/2003/instance}context')

        # Дублировать блок 3 раза
        for i in range(3):
            new_block = etree.fromstring(etree.tostring(context_block))
            # Найти элемент <dim-int:ID_NomeraInformSoobshheniyaOSdelkeTypedName>

            # id_element_ctx = root.find(
            #     './/{http://www.xbrl.org/2003/instance}context[@id="ctx_3ef9ba1955544d373419e57e7596c2ba"]')
            id_element_dim = new_block.find(
                './/{http://www.xbrl.org/2003/instance}scenario/{http://xbrl.org/2006/xbrldi}typedMember/{http://www.cbr.ru/xbrl/udr/dim/dim-int}ID_NomeraInformSoobshheniyaOSdelkeTypedName')

            # Проверить, что элемент найден
            if id_element_dim is not None:
                # Изменить значение элемента
                id_element_dim.text = 'Taxis_' + str(int(id_element_dim.text.split('_')[1]) + i + 1)
                # id_element_dim.attrib['id'] = 'ctx_' + str(int(id_element_dim.text.split('_')[1]) + i + 1)
                context_block.set('id', f'ctx_{i + 1}')
            # Добавить новый блок в корень
            root.append(new_block)

        # Сохранить изменения в файл
        tree.write('/home/vlad/Документы/xbrl_1_5_gb/test1/result/' + file, pretty_print=True, xml_declaration=True, encoding='UTF-8')




