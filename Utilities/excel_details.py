import openpyxl
def get_booking_data(file):
    workbook = openpyxl.load_workbook(file)
    sheet = workbook.active
    data = []
    headers = []
    # Read headers from first row
    for col in range(1, sheet.max_column + 1):
        headers.append(sheet.cell(row=1, column=col).value)

    # Read data rows
    for row in range(2, sheet.max_row + 1):

        row_data = {}
        is_empty = True

        for col in range(1, sheet.max_column + 1):

            key = headers[col - 1]
            value = sheet.cell(row=row, column=col).value

            if value is not None and str(value).strip() != "":
                is_empty = False

            row_data[key] = value

        if not is_empty:
            data.append(row_data)

    return data