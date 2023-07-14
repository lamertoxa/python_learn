import csv
with open('test_file.csv', mode='w') as csv_file:

    writer = csv.DictWriter(
        csv_file,
        fieldnames=['first_col', 'second_col']
    )
    writer.writeheader()

    # This input dictionary is what the question is referring
    # to and is not necessarily correct as shown.
    writer.writerow({'key1':'value1', 'key2':'value2'})
