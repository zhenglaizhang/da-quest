import csv
import pprint

data_path = "./survey.csv"


def run():
    male_set = {'male', 'm'}
    female_set = {'female', 'f'}
    # value is list with 2 elements, 1st element is result of female, 2nd element is the result of male's
    result = {}

    with open(data_path, newline='') as csv_file:
        rows = csv.reader(csv_file)
        for i, row in enumerate(rows):
            if i == 0:
                continue
            if i % 50 == 0:
                print("processing row {}".format(i))

            # raw data
            gender_val = row[2]
            country_val = row[3]

            # cleaning
            gender_val = gender_val.lower().replace(' ', '')
            country_val = country_val.lower()

            if country_val not in result:
                result[country_val] = [0, 0]

            if gender_val in female_set:
                result[country_val][0] += 1
            elif gender_val in male_set:
                result[country_val][1] += 1
            else:
                # noise data
                # pass
                print("unknown gender_val: {}", gender_val)

    pprint.pprint(result)

    with open('survey_result1.csv', 'w', newline='', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        writer.writerow(['Country', 'Male', 'Female'])
        for k, v in list(result.items()):
            writer.writerow([k, v[0], v[1]])

if __name__ == '__main__':
    run()
