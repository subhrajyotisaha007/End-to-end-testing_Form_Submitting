# import openpyxl
# dict1 = {}
# ts3 = []
#
# book = openpyxl.load_workbook("People data.xlsx")
# sheet = book.active
# # cell = sheet.cell(row=1, column=2)
# # print(cell.value)
# sheet.cell(row=5,column=2).value = "Souvik Saha"
# sheet.cell(row=5,column=1).value = 'TS004'
# sheet.cell(row=5,column=3).value = "mail@hotline.com"
# sheet.cell(row=5,column=4).value = "Male"
# sheet.cell(row=5,column=5).value = 12345
#
# book.save("People data.xlsx")
# # print(sheet.max_row)
# # print(sheet.max_column)
# # for i in range(1,sheet.max_row+1):
# #     for j in range(1,sheet.max_column+1):
# #         print(sheet.cell(row=i,column=j).value)
#
# # for i in range(2,sheet.max_column+1):
# #     print(sheet.cell(row=1,column=i).value)
# #     identities.append(sheet.cell(row=1,column=i).value)
# # print(identities)
#
#
# # for i in range(1,sheet.max_row+1):
# #         if sheet.cell(row=i,column=1).value=="TS003":
# #             for j in range(2, sheet.max_column + 1):
# #                 #print(sheet.cell(row=i,column=j).value)
# #                 #ts3.append(sheet.cell(row=i,column=j).value)
# #                 dict1[sheet.cell(row=1,column=j).value] = sheet.cell(row=i,column=j).value
# #                 print(dict1)
#
#
#
# # for i in range(1,sheet.max_row+1):
# #         for j in range(2, sheet.max_column + 1):
# #                 #print(sheet.cell(row=i,column=j).value)
# #                 #ts3.append(sheet.cell(row=i,column=j).value)
# #             dict1[sheet.cell(row=1,column=j).value] = sheet.cell(row=i,column=j).value
# #             print(dict1)
#
# # print(ts3)
#
# # for i in range(len(identities)):
# #     dict1[identities[i]] = ts3[i]
# # print(dict1)
# # dict2 = {'Name': 'Shetty', 'Mail': 'rahul@outlook.com', 'Gender': 'Male', 'Password': '9273hh'}
# #
# # ts3.append(dict2)
# # ts3.append(dict1)
#
# # if test_case_name == all:
# test_cases = [cell.value for cell in sheet['A']]
# print(test_cases)
# for k in range(1,len(test_cases)):
#     for i in range(1,sheet.max_row+1):
#         if sheet.cell(row=i,column=1).value==test_cases[k]:
#             for j in range(2, sheet.max_column + 1):
#                     #print(sheet.cell(row=i,column=j).value)
#                     #ts3.append(sheet.cell(row=i,column=j).value)
#                 dict1[sheet.cell(row=1,column=j).value] = sheet.cell(row=i,column=j).value
#             print(dict1)
#             ts3.append(dict1.copy())
#
#
#
# print(ts3)



from HomepageData import HomePageData

HomePageData.get_test_data("TS003")