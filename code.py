import csv
import requests
import logging

# create users from a CSV file
def create_users(file_path):
    # Open the CSV file to read and error log file to write
    with open(file_path, 'r') as csv_file, open('error_log.txt', 'w') as error_log:
        reader = csv.DictReader(csv_file)

        # check each row in the CSV
        for row in reader:
            email = row.get('email')

            # Skip rows with missing email
            if not email:
                error_log.write(f"Skipped row with missing email: {row}\n")
                continue

            # Adding try-except for API
            try:
                response = requests.post("https://example.com/api/create_user", json=row)

                # Check wether user created successfully
                if response.status_code != 201:
                    error_log.write(f"Failed to create user: {email} (Status: {response.status_code})\n")

            # Handle errors (network or request)
            except Exception as e:
                error_log.write(f"Error for user {email}: {str(e)}\n")

# Run the function with CSV file
create_users("users.csv")


#Changes Done
#skiped Rows with Missing Email
#added try-except
#set a basic error logging to a file (error_log.txt)


#improvements
#validate all fields before excute
#use logging module
#try excute the scrpit on a CLI
#decalre meaningful functions and varables


