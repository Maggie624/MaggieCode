import xlrd
import os

class ExcelUtil():
    def __init__(self, excelPath=os.path.dirname(__file__) + '/test_params.xlsx', sheetName='Sheet1'):
        self.data = xlrd.open_workbook(excelPath)
        self.table = self.data.sheet_by_name(sheetName)
        self.keys = self.table.row_values(0)    # 获取第一行作为key值
        self.rowNum = self.table.nrows          # 获取总行数
        self.colNum = self.table.ncols          # 获取总列数

    def dict_data(self):
        if self.rowNum <= 1:
            print("没有测试数据")
        else:
            result = []
            current_row = 1
            for i in range(self.rowNum-1):
                s = {}
                values = self.table.row_values(current_row)
                for x in range(self.colNum):
                    s[self.keys[x]] = values[x]
                result.append(s)
                current_row += 1
            return result

if __name__ == "__main__":
    filepath = os.path.dirname(__file__) + '/test_params.xlsx'
    sheetName = 'login'
    data = ExcelUtil(filepath, sheetName)
    print(data.dict_data())
