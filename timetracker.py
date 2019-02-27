import csv, datetime

# Functions
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

def logstart():
    """Will prompt user to enter Project and Task they are currently working
    on, then log today's Date, current Start Time, Project and Task in
    temporary file temp_file.csv of length one row. End Time in the third
    column is omitted because it will be logged by function end, but a
    placeholder will be logged in form of an empty string. temp_file.csv will
    be overwritten with every execution of function logstart as it serves as a
    temporary storage for function logend.
    """
    project = input('\nWhat project are you working on?\n')
    task = input('What task are you working on?\n')
    start_time = datetime.datetime.now().strftime('%H:%M')
    with open('temp_file.csv', 'w') as write_temp_file:
        writer = csv.writer(write_temp_file)
        writer.writerow([
            datetime.date.today(),
            start_time,
            '',
            str(project),
            str(task),
            ])
    print('\nI have started logging ' + str(task) + ' for ' + str(project) +
        ' with a start time of ' + str(start_time) + '.')

def logend():
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

    end_time = datetime.datetime.now().strftime('%H:%M')
    with open('output_file.csv', 'a') as write_output_file:
        writer = csv.writer(write_output_file)
        writer.writerow([
            date,
            start_time,
            end_time,
            project,
            task,
        ])
    print('\nI have finsihed logging ' + str(task) + ' for ' + str(project) +
        ' with an end time of ' + str(end_time) + '.')

def logchange():
    """In order to finish logging the current task and start logging another,
    function logchange will end current log by executing function logend and
    start a new log by executing function logstart.
    """
    logend()
    logstart()

# Program
flag = True

new_month = input('\nDo you want to create a new output file? (Yes/No)\n' +
    'ATTENTION: If you answer "Yes", your current output file may be ' +
    'overwritten and your data potentially lost.\n')
if new_month.lower() == 'yes':
    newmonth()

logstart()

while flag:
    command = input('\nDo you wish to:\n' +
                'Finish working on the current task and project? ' +
                '(Pleae enter "Done")\n' +
                'Start working on another task or project? ' +
                '(Please enter "Switch")\n')
    
    if command.lower() == 'done':
        logend()
        print('\nThe current logging session has been terminated.\n')
        flag = False
    elif command.lower() == 'switch':
        logchange()
    else:
        print('\nYou seem to have made a typo. Please reconsider:')