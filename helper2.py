class Parser:
    def __init__(self, file):
        self.F = file

    def read_excel(self):
        filename = self.F
        wb = xlrd.open_workbook(filename)
        data = {}
        for sheet_name in wb.sheet_names():
            data[sheet_name] = []
            # print("Reading sheet", sheet_name)
            sheet1 = wb.sheet_by_name(sheet_name)
            nrows = sheet1.nrows
            ncols = sheet1.ncols

            sheet_data = []
            for i in range(nrows):
                row = []
                for j in range(ncols):
                    # print(i, j, sheet1.cell_value(i, j))
                    row.append(sheet1.cell_value(i, j))
                sheet_data.append(row)
            data[sheet_name] = sheet_data
        self.DATA = data
    # self.DATA = ALL_EXCEL_DATA
    # write the logic to read the excel file
    # self.F


f = Parser("test.xls")
x1 = Parser("test1.xls")
x1 = Parser("test2.xls")

f.read_excel()

print(f.DATA)
