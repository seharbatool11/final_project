import csv

from django.core.management.base import BaseCommand, CommandError
from dics.models import Word


class Command(BaseCommand):
    help = "Takes an input file and loads all the words from it"

    def add_arguments(self, parser):
        parser.add_argument("--filename", "-f", nargs="?", type=str)

    def handle(self, *args, **options):
        filename = options["filename"]
        if not filename:
            raise CommandError('Command must be provided with a filename!')

        with open(f"./{filename}", mode='r', encoding="utf8") as csv_file:
            csv_reader = csv.reader(csv_file)
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    # word_column, c_columns = row.split(',', 1)
                    # urdu_columns = [c.strip() for c in c_columns.split(',')]
                    line_count += 1
                word, urdu = row[0], row[1]
                w = Word.objects.create(word=word.strip(), urdu=urdu.strip())
                # for choice in [c.strip() for c in choices]:
                #     Choice.objects.create(question=q, choice_text=choice)
                line_count += 1
            print(f'Processed {line_count} lines.')

        print('Successfully search the meaning of word!')


#===========================
# import csv
# from django.core.management.base import BaseCommand, CommandError
# from dics.models import Word

# filename ="Dictionary.csv"
 
# with open(filename, 'r') as data:
#   for line in csv.DictReader(data):
#       print(line)
#=======================
# answer = {}
# with open('Dictionary.csv') as infile:
#     infile.readline()  
#     for line in infile:
#         word, urdu = (s.strip('"') for s in line.split(','))
#         key = (word, urdu)
#         if key not in answer: answer[key] = {}
#         answer[key][int()] = (int(), None)


