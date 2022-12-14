import csv


class WorkCSV:
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
        with open(path_csv, 'a', newline='') as f:
            writer = csv.writer(f, quoting=csv.QUOTE_NONNUMERIC)
            writer.writerow(add_data)

    @staticmethod
    def remove_note(path_csv, remove_name):
        with open('test.csv', 'r', newline='') as f, open('test2.csv', 'w', newline='') as ff:
            reader = csv.reader(f)
            writer = csv.writer(ff)
            for row in reader:
                if row[0] != remove_name:
                    print(row[0])
                    writer.writerow(row)
            f.close()
            ff.close()
        with open('test.csv', 'w', newline='') as f, open('test2.csv', 'r', newline='') as ff:
            reader = csv.reader(ff)
            for i in reader:
                writer = csv.writer(f)
                writer.writerow(i)

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
# WorkCSV.read_notes_from('test.csv')
# WorkCSV.add_to_csv('test.csv', ['Titanik','Best film ever', 4.9])
# WorkCSV.remove_note('test.csv', "Terminator")
# WorkCSV.print_to_console('test.csv')
# WorkCSV.highest_rating('test.csv')
# WorkCSV.lowest_rating('test.csv')
# WorkCSV.rating('test.csv')
