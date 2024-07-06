import os
from time import sleep

directories = os.environ['WATCH_DIRECTORIES'].split(',')

# Make directory for file
sleep_timer = int(os.environ.get('SLEEP_TIMER', 10))
while True:
    for directory in directories:
        for fl in os.listdir(directory):
            try:
                file_path = os.path.join(directory, fl)
                if os.path.isfile(file_path):
                    # Get file name
                    rename_file_base_name = fl.split('.')[:-1]
                    if not rename_file_base_name:
                        raise ValueError(f"I cant do anything with this file [{fl}]. Ensure there is an extension!")

                    # Ensure directory exists
                    new_directory = os.path.join(
                        directory,
                        '.'.join(rename_file_base_name)
                    )
                    os.makedirs(new_directory, exist_ok=True)

                    # Rename fl
                    new_filename = os.path.join(
                        new_directory,
                        fl
                    )
                    print(f"Renaming {file_path} to {new_filename}")
                    os.rename(
                        file_path,
                        new_filename
                    )
            except Exception as err:
                print(f"Error: {err}")
    print(f"Sleeping for {sleep_timer} seconds")
    sleep(sleep_timer)
