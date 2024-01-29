# Chalenge Tunts Rocks 2024

This script analyzes student data from a Google Spreadsheet and updates their situation based on attendance and grades.

## Requirements

- **git**

- **python 3.12.0**

```bash
python --version
```

- **gspread 6.0.0**: Python API for Google Sheets

```bash
pip install gspread
```

- Credentials JSON file with proper Google Sheets API access. [How To Get Credentials](#how-to-obtain-google-sheets-api-credentials)

## Usage

```bash
mkdir <dir_name>
cd <dir_name>
git init
git remote add origin
python script.py <client_key>
```

* <client_key>: Path to a JSON file containing Google Sheets API credentials.

## Example

```bash
mkdir tunts-rocks
cd tunts-rocks
git init
git remote add origin
python script.py path/to/your/credentials.json
```
## How to Obtain Google Sheets API Credentials

1. Visit the Google Cloud Console.
2. Create a new project.
3. Enable the Google Sheets API for the project.
4. Create credentials for the project, choosing "Service account key" as the credential type.
5. Download the JSON file containing your credentials and specify its path when running the script.

## Script Details

The script performs the following actions:

1. Reads data from a specified Google Spreadsheet (worksheet: 'engenharia_de_software').
2. Analyzes student data, calculates their situation based on attendance and grades.
3. Updates the student data with the calculated situation.
4. Prints a message indicating the completion of the process.

## Important Note

This script assumes the existence of the google_client.py and student.py files containing the necessary classes and functions. Ensure these files are present and properly structured in the project directory.

## License

This project is licensed under the MIT License.