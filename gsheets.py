def get_user_name(service, spreadsheet_id):
    range_name = 'A1:A1'
    sheet = service.spreadsheets()

    result = sheet.values().get(spreadsheetId=spreadsheet_id,
                                range=range_name).execute()

    values = result.get('values', [])

    if not values:
        print('No data found.')

    else:
        for row in values:
            print(row)
