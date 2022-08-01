import csv

class Work_csv:
    def __init__(self, path_csv, add_data, remove_name):
        self.path_csv = path_csv
        self.add_data = add_data
        self.remove_name = remove_name

    @staticmethod
    def read_notes_from(path_csv):
        with open(path_csv) as f:
            reader = csv.reader(f)
            return list(reader)

    @staticmethod
    def open_csv(path_csv):
        with open(path_csv) as f:
            reader = csv.reader(f)
            for row in reader:
                print(row)

    @staticmethod
    def add_to_csv(path_csv, add_data):
        with open(path_csv, 'a') as f:
            writer = csv.writer(f, quoting=csv.QUOTE_NONNUMERIC)
            writer.writerow(add_data)

    @staticmethod
    def remove_note(path_csv, remove_name):
        with open('test.csv', 'r') as f, open('test2.csv', 'w') as ff:
            reader = csv.reader(f)
            writer = csv.writer(ff, quoting=csv.QUOTE_NONNUMERIC)
            for row in reader:
                if row[0] != remove_name:
                    print(row[0])
                    writer.writerow(row)

    @staticmethod
    def print_to_console(path_csv):
        with open(path_csv) as f:
            reader = csv.reader(f)
            for row in reader:
                print(row)

    @staticmethod
    def highest_rating(path_csv):
        with open('test.csv') as f:
            reader = csv.reader(f)
            numer = []
            for row in reader:
                numer.append(row[2])
            f.close()

        with open('test.csv') as f:
            reader = csv.reader(f)
            for row in reader:
                if row[2] == max(numer[1:]):
                    print(*row)

    @staticmethod
    def lowest_rating(path_csv):
        with open('test.csv') as f:
            reader = csv.reader(f)
            numer = []
            for row in reader:
                numer.append(row[2])
            f.close()

        with open('test.csv') as f:
            reader = csv.reader(f)
            for row in reader:
                if row[2] == min(numer[1:]):
                    print(*row)

    @staticmethod
    def rating(path_csv):
        with open(path_csv) as f:
            reader = csv.reader(f)
            numer = []
            for row in reader:
                numer.append(row[2])
            ints = [eval(x) for x in numer]
            average = sum(ints) / len(ints)
            print("Average rating is: " + str(average))
# Work_csv.read_notes_from('test.csv')
# Work_csv.add_to_csv('test.csv', ['Titanik','Best fil ever', 4.9])
# Work_csv.remove_note('test.csv', "Terminator")
# Work_csv.print_to_console('test.csv')
# Work_csv.highest_rating('test.csv')
# Work_csv.lowest_rating('test.csv')
# Work_csv.rating('test.csv')
