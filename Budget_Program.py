from display.app import start_app, open_browser
from src.credentials import get_credentials
from src.reading_email import GetAttachments
from src.get_id import ListMessagesMatchingQuery
import time
import schedule
from src.file_processing import process_files
from src.export_to_database import export_to_database
from pathlib import Path
def task():
    service = get_credentials()
    cache_folder = Path("cache/")
    download_path = cache_folder / "downloads"
    unencrypted_path = cache_folder / "unencrypted"
    csv_path = cache_folder / "csv"
    query = 'ibsupport@standardbank.co.za'
    messages = ListMessagesMatchingQuery(service, 'me', query)

    GetAttachments(service, 'me', messages, download_path)

    password = "Adamozbayr"
    process_files(password, download_path, unencrypted_path, csv_path)
    export_to_database(csv_path)

def main():
    task()
    open_browser()
    start_app()

    #schedule.every().day.at("11:00").do(task)
    #while True:
    #    schedule.run_pending()
    #    time.sleep(1)

if __name__ == "__main__":
    main()
