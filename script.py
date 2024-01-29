"""
Tunts Rocks 2024 Student Analysis Script

This script reads data from a Google Spreadsheet, analyzes the data, and updates the student's situation based on attendance and grades.

Usage:
    python script.py <client_key>

Arguments:
    client_key (str): Path to a JSON file containing Google Sheets API credentials.

Requirements:
    - gspread: Python API for Google Sheets
    - Credentials JSON file with proper Google Sheets API access

Example:
    python script.py path/to/your/credentials.json

"""

from google_client import GoogleSheetsClient
from student import Student
import argparse
import json

def read_credentials_file(file_path):
    """
    Read and parse the JSON file containing Google Sheets API credentials.

    Parameters:
        file_path (str): Path to the JSON file.

    Returns:
        dict: Parsed JSON credentials.
    
    Raises:
        FileNotFoundError: If the credentials file is not found.
        ValueError: If the JSON file has an invalid format.
    """
    try:
        with open(file_path, 'r') as file:
            credentials = json.load(file)
        return credentials
    except FileNotFoundError:
        raise FileNotFoundError(f"Credentials file not found at: {file_path}")
    except json.JSONDecodeError:
        raise ValueError(f"Invalid JSON format in the credentials file: {file_path}")

def main():
    """
    Main function to execute the student analysis script.
    """
    parser = argparse.ArgumentParser(
        description="This script reads data from a Google Spreadsheet, analyzes the data, and writes the student's situation."
    )
    parser.add_argument("client_key", help="A JSON file with your credentials.")
    parser.add_argument("sheet_id", help="A Google Spreadsheet id.")
    parser.add_argument("sheet_name", help="A name of spreadsheed.")
    args = parser.parse_args()

    try:
        credentials_file = read_credentials_file(args.client_key)
        spreadsheet_id = args.sheet_id
        file_key = args.client_key

        client = GoogleSheetsClient(credentials_file, spreadsheet_id, file_key)

        worksheet_name = args.sheet_name
        data = client.read_data(worksheet_name)

        total_classes = int(data[1][0][-2::])

        for student_row in data[3:]:
            student = Student(student_row[0], student_row[1], int(student_row[2]))
            for grade in student_row[3:5]:
                student.add_grade(int(grade))
            student.calculate_average()
            student.calculate_percentual_absences(total_classes)
            student.calculate_situation()
            student_row[6] = student.situation
            student_row[7] = student.final_situation

        # client.write_data(worksheet_name, data)

        print("The process has been finished. Please check the Spreadsheet.")
    except FileNotFoundError as e:
        print(f"Error: {e}")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()