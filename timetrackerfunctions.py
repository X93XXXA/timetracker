import csv, datetime

def newmonth():
    """Will create new output file output_file.csv with five columns containing
    header Date, Start Time, End Time, Project, Task. Function newmonth() is
    likely to be executed at beginning of every new billing month.
    ATTENTION: If output_file.csv exists, it will be overwritten and its data
    lost.
    """
    with open('output_file.csv', 'w') as create_output_file:
        writer = csv.writer(create_output_file)
        writer.writerow([
            'Date',
            'Start Time',
            'End Time',
            'Project',
            'Task',
        ])

def start():
    """Will prompt user to enter Project and Task they are currently working
    on, then log today's Date, current Start Time, Project and Task in
    temporary file temp_file.csv of length one row. End Time in the third
    column is omitted because it will be logged by function end(), but a
    placeholder will be logged in form of an empty string. temp_file.csv will
    be overwritten with every execution of function start() as it serves as a
    temporary storage for function end().
    """
    project = input('What project are you working on?\n')
    task = input('What task are you working on?\n')
    with open('temp_file.csv', 'w') as write_temp_file:
        writer = csv.writer(write_temp_file)
        writer.writerow([
            datetime.date.today(),
            datetime.datetime.now().strftime('%H:%M'),
            '',
            str(project),
            str(task),
            ])

def end():
    """Will read Date, Start Time, Project and Tast from temporary file
    temp_file.csv and write data into output file output_file.csv, supplemented
    by current End Time in the third column.
    """
    with open('temp_file.csv', 'r') as read_temp_file:
        reader = csv.reader(read_temp_file)
        for row in reader:
            date = row[0]
            start_time = row[1]
            project = row[3]
            task = row[4]

            with open('output_file.csv', 'a') as write_output_file:
                writer = csv.writer(write_output_file)
                writer.writerow([
                    date,
                    start_time,
                    datetime.datetime.now().strftime('%H:%M'),
                    project,
                    task,
                ])