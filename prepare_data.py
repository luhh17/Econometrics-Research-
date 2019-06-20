import pandas as pd
import numpy as np
import csv
import os

# data = pd.read_csv('GFDDData.csv')
#
# Indicator_list = pd.read_csv('GFDDSeries.csv')['Indicator Name']
# Indicator_Code_list = pd.read_csv('GFDDSeries.csv')['Series Code']
# Country_Code_list = pd.read_csv('GFDDCountry.csv')['Country Code']
# Year_list = list(range(1960, 2018))
# # for i in range(len(Indicator_list)):
# #     v = np.ndarray
# #     indicator = Indicator_list[i]
# #     indicator_code = Indicator_Code_list[i]
# #     print(indicator_code)
# #     for j in range(len(data)):
# #         if data.iloc[j, 3] != indicator_code:
# #             continue
# #         data_line = data.iloc[j, :].drop(['Country Code',
# #                                          'Indicator Code', 'Indicator Name'])
# #         data_line = data_line.values
# #         if data_line[0] == 'Afghanistan':
# #             v = np.hstack(data_line)
# #         else:
# #             v = np.vstack((v, data_line))
# #     data_frame = pd.DataFrame(v)
# #     fname = indicator_code + '.csv'
# #     data_frame.to_csv(fname)
# #
# # year_list = list(range(1960, 2018))
# # year_list.insert(0, 'Country')
# # year_list.append('None')
# #
# # for i in range(len(Indicator_list)):
# #     indicator_code = Indicator_Code_list[i]
# #     file = pd.read_csv(str(indicator_code + '.csv'))
# #     file = file.drop('Unnamed: 0', axis=1)
# #     file.columns = year_list
# #     file.to_csv(str(indicator_code + 'b.csv'))
# #
# # for i in range(len(Indicator_list)):
# #     indicator_code = Indicator_Code_list[i]
# #     file = pd.read_csv(str(indicator_code + '.csv'))
# #     file = file.drop(['Unnamed: 0', 'None'], axis=1)
# #     file.to_csv(str(indicator_code + 'b.csv'))
# #
# #
# # for i in range(len(Indicator_list)):
# #     indicator_code = Indicator_Code_list[i]
# #     # if os.path.exists(str(indicator_code + '.csv')):
# #     #     os.remove(str(indicator_code + '.csv'))
# #     if os.path.exists(str(Indicator_list[i] + '.csv')):
# #         os.remove(str(Indicator_list[i] + '.csv'))
# #     if os.path.exists(str(indicator_code + 'b.csv')):
# #         os.renames(str(indicator_code + 'b.csv'), str(indicator_code + '.csv'))
# #
#
# All_Country_data = []
# with open('GFDDData.csv', 'r', encoding='utf8') as file:
#     reader = csv.reader(file)
#     for row in reader:
#         All_Country_data.append(row)
#
#
# def Curtain_Country_Data(country, year):
#     _data = []
#     rank = year - 1956
#     start = 0
#     end = 0
#     for i in range(len(All_Country_data)):
#         if All_Country_data[i][1] == country:
#             start = i
#             break
#
#     for i in range(start, len(All_Country_data)):
#         if All_Country_data[i][1] != country:
#             end = i - 1
#             break
#
#     for i in range(len(Indicator_Code_list)):
#         indicator = Indicator_Code_list[i]
#         for j in range(start, end+1):
#             if All_Country_data[j][1] == country and All_Country_data[j][3] == indicator:
#                 _data.append(All_Country_data[j][rank])
#                 break
#
#     return _data
#
#
# out_list = []
#
# first_line = ['Country', 'Year']
# for i in range(len(Indicator_Code_list)):
#     first_line.append((Indicator_Code_list[i]))
# out_list.append(first_line)
#
# for i in range(len(Country_Code_list)):
#     country_code = Country_Code_list[i]
#     for j in range(len(Year_list)):
#         year = Year_list[j]
#         line = Curtain_Country_Data(country_code, year)
#         line.insert(0, year)
#         line.insert(0, country_code)
#         out_list.append(line)
#
# with open('Data.csv', 'w', encoding='utf8') as file:
#     writer = csv.writer(file, lineterminator='\n')
#     for line in out_list:
#         writer.writerow(line)
#


All_Country_data = []
with open('Data.csv', 'r', encoding='utf8') as file:
    reader = csv.reader(file)
    for row in reader:
        All_Country_data.append(row)

count = 0
start = 1
end = 1


def ReName(start, end, count):
    for i in range(start, end+1):
        All_Country_data[i][0] = count


for i in range(1, len(All_Country_data)):
    if All_Country_data[i-1][0] != All_Country_data[i][0]:
        end = i - 1
        ReName(start, end, count)
        start = i
        count += 1
ReName(start, len(All_Country_data)-1, count)


with open('Data_2.csv', 'w', encoding='utf8') as file:
    writer = csv.writer(file, lineterminator='\n')
    for line in All_Country_data:
        writer.writerow(line)




