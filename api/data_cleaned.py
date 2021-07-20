import pandas

pandas.options.display.max_rows = 1000
pandas.options.display.max_columns = 1000
messages = pandas.read_excel('data.xlsx', engine='openpyxl', sheet_name='Messages')
subjects = pandas.read_excel('data.xlsx', engine='openpyxl', sheet_name='Subjects')
combined = pandas.merge(subjects, messages, on='ticket_id', how='inner')
combined['intents'] = [row['body_text'].split('(')[0].replace('Detected intent:', '') for index, row in combined.iterrows()]
combined['subject'] = [row['subject'].split(']')[1] if ']' in row['subject'] else row['subject'] for index, row in combined.iterrows()]
combined.drop('body_text', axis=1, inplace=True)

unique_tkt = combined.groupby('ticket_id')['intents'].apply(list).reset_index(name='intents')
final_df = unique_tkt
for col in list(combined):
    if col != 'ticket_id':
        temp = combined.groupby('ticket_id')[col].apply(list).reset_index(name=col)
        print(temp)
        pandas.merge(final_df, temp, on='ticket_id', how='inner')