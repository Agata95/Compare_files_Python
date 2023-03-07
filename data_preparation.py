import pickle
import pandas as pd
import commons

"""
Przygotowanie picle z bazy domów i mieszkań
"""

path = r'files'

# xlsx_files = {
#     'baza_domow_old': {'file': 'baza_domow_old.xlsx', 'sheet': 'data', 'header': 0},
#     'baza_domow_new': {'file': 'baza_domow_new.xlsx', 'sheet': 'data', 'header': 0},
#     'baza_mieszkan_old': {'file': 'baza_mieszkan_old.xlsx', 'sheet': 'data', 'header': 0},
#     'baza_mieszkan_new': {'file': 'baza_mieszkan_new.xlsx', 'sheet': 'data', 'header': 0}
#     }
#
#
# # budowanie struktury ułatwiającej pisanie taryfy
# data_object = {}
#
# for k in xlsx_files.keys():
#     row = xlsx_files[k]
#     data_object[k] = pd.read_excel(f'{path}/'+row['file'], sheet_name=row['sheet'], header = row['header'],
#                                                  converters={'pozycja taryfy - value': str,
#                                                              'pozycja taryfy - name': str,
#                                                              'idProductModule': str}).values
#
# data_object['baza_domow_old'] = dict(data_object['baza_domow_old'])
# data_object['baza_domow_new'] = dict(data_object['baza_domow_new'])
# data_object['baza_mieszkan_old'] = dict(data_object['baza_mieszkan_old'])
# data_object['baza_mieszkan_new'] = dict(data_object['baza_mieszkan_new'])

# zapis do pickle
localization = f"{path}/baza.pickle"
# pickle_file = open(localization, "wb")
# pickle.dump(data_object, pickle_file)
# pickle_file.close()

a = commons.get_data_from_pickle(localization)
print(a)