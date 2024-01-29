import gspread
from typing import List, Union

class GoogleSheetsClient:
    """
    Represents a client for interacting with Google Sheets.

    Attributes:
    - credentials_file (str): The path to the JSON file containing Google Sheets API credentials.
    - spreadsheet_id (str): The ID of the Google Spreadsheet.
    - file_key (str): The file key used for service account authentication.

    Methods:
    - read_data(worksheet_name: str) -> List[List[Union[str, int]]]:
        Reads data from a specified worksheet in the Google Spreadsheet.

    - write_data(worksheet_name: str, data: List[List[Union[str, int]]]):
        Writes data to a specified worksheet in the Google Spreadsheet.

    Raises:
    - ValueError: If the specified worksheet is not found or if there is an error writing data.
    """

    def __init__(self, credentials_file: str, spreadsheet_id: str, file_key: str):
        """
        Initializes the GoogleSheetsClient.

        Parameters:
        - credentials_file (str): The path to the JSON file containing Google Sheets API credentials.
        - spreadsheet_id (str): The ID of the Google Spreadsheet.
        - file_key (str): The file key used for service account authentication.
        """
        self.credentials_file = credentials_file
        self.spreadsheet_id = spreadsheet_id
        self.gc = gspread.service_account(filename=file_key)

    def read_data(self, worksheet_name: str) -> List[List[Union[str, int]]]:
        """
        Reads data from a specified worksheet in the Google Spreadsheet.

        Parameters:
        - worksheet_name (str): Name of the worksheet to read.

        Returns:
        - List[List[Union[str, int]]]: The data read from the worksheet.
        """
        try:
            worksheet = self.gc.open_by_key(self.spreadsheet_id).worksheet(worksheet_name)
            return worksheet.get_all_values()
        except gspread.exceptions.WorksheetNotFound:
            raise ValueError(f"The worksheet '{worksheet_name}' was not found.")

    def write_data(self, worksheet_name: str, data: List[List[Union[str, int]]]):
        """
        Writes data to a specified worksheet in the Google Spreadsheet.

        Parameters:
        - worksheet_name (str): Name of the worksheet to write data to.
        - data (List[List[Union[str, int]]]): The data to be written to the worksheet.

        Raises:
        - ValueError: If the specified worksheet is not found or if there is an error writing data.
        """
        try:
            worksheet = self.gc.open_by_key(self.spreadsheet_id).worksheet(worksheet_name)
            worksheet.clear()  # Clears the worksheet before writing new data
            worksheet.append_rows(data)
        except gspread.exceptions.WorksheetNotFound:
            raise ValueError(f"The worksheet '{worksheet_name}' was not found.")
        except gspread.exceptions.APIError as e:
            raise ValueError(f"Error writing data: {e}")