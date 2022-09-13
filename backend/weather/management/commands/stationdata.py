import csv
from django.core.management.base import BaseCommand, CommandError
from weather.models import StationData
import datetime


class Command(BaseCommand):
    help = 'Imports weather data from a local weather station in to the database from a .csv file'

    def add_arguments(self, parser):
        parser.add_argument(
            'file', type=str, help='CSV File name (Ex.: ws_01_averages.csv).'
            )

    def handle(self, *args, **options):
        csvPath = options['file']
        if not csvPath:
            raise CommandError('%s doesnt exist.' %csvPath)    

        errors = False
        station_data = []

        with open('../csv_files/' + csvPath, 'r', newline='', encoding='utf-8-sig') as csvFile:
            reader = csv.reader(csvFile, delimiter=',')
            next(reader)
            try:
                for row in reader:
                    station_data.append(StationData(
                        temperature_avg=row[0],
                        temperature_max=row[1],
                        temperature_min=row[2],
                        relative_humidity=row[3],
                        sunshine_duration=row[4],
                        global_radiation=row[5],
                        daily_eto=row[6],
                        wind_speed=row[7],
                        precipitation=row[8],
                        event_date=datetime.datetime.strptime(row[9], '%m/%d/%Y').strftime('%Y-%m-%d'),
                        station_id=row[10]                        
                        ))
            except KeyError as e:
                self.stderr.write('Look this error: {0}'
                                  .format(str(e)))
                self.stderr.flush()
                errors = True
        if errors:
            self.stdout.write(self.style.ERROR(
                'File has incorrect format. It''s missing a column.'))
            return
        created = StationData.objects.bulk_create(
            station_data, ignore_conflicts=True)
        count = len(created)
        if not count:
            self.stdout.write(self.style.WARNING(
                'File was imported but no data was registered.'))
            return
        self.stdout.write(
            self.style.SUCCESS(
                f'Successfully imported station data file and registered {count} '
                f'record{"s" if count != 1 else ""}. '
            )
        )

