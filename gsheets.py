def get_user_cell(service, spreadsheet_id, user):
    range_literal = 'A'
    range_number = 4

    sheet = service.spreadsheets()

    list_of_cells = []

    while range_number < 30:
        range_name = range_literal + str(range_number)
        result = sheet.values().get(spreadsheetId=spreadsheet_id,
                                    range=range_name).execute()

        values = result.get('values', [])

        if values:
            if values[0][0] == user:
                list_of_cells.append(range_number)

        range_number += 1

    return list_of_cells
