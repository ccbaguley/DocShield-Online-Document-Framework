import os
import sys
import time
import logging
import requests
from pathlib import Path
from threading import Thread
from logging.handlers import RotatingFileHandler

# Define cross-platform production storage and logging fallback directories
if os.name == 'nt':
    LOG_DIRECTORY = Path(os.environ.get("PROGRAMDATA", r"C:\ProgramData")) / "DocShieldDefense"
else:
    LOG_DIRECTORY = Path("/var/log/docshielddefense")

LOG_FILE_PATH = LOG_DIRECTORY / "document_defense_daemon.log"

if not LOG_DIRECTORY.exists():
    try:
        LOG_DIRECTORY.mkdir(parents=True, exist_ok=True)
    except Exception as e:
        sys.exit(f"Critical Initialization Failure: Cannot create logging structure: {e}")

log_handler = RotatingFileHandler(str(LOG_FILE_PATH), maxBytes=5 * 1024 * 1024, backupCount=3)
logging.basicConfig(
    handlers=[log_handler, logging.StreamHandler(sys.stdout)],
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] (%(threadName)s) %(message)s'
)

class DocShieldMonitor:
    def __init__(self, check_interval_seconds=10):
        self.interval = check_interval_seconds
        self.is_running = True
        # Historical memory state arrays to track modifications across iterations
        self.document_vault = {}

    def monitor_google_doc(self, doc_id, api_key):
        """Watches changes via the Google Docs REST API v1 endpoint."""
        url = f"https://googleapis.com{doc_id}?key={api_key}"
        logging.info(f"[DOCSHIELD] Initializing structural tracking for Google Doc: {doc_id}")
        
        while self.is_running:
            try:
                response = requests.get(url, timeout=5)
                if response.status_code == 200:
                    doc_data = response.json()
                    # Track revisions via standard document body sizing constraints
                    current_length = len(str(doc_data.get('body', '')))
                    
                    if doc_id in self.document_vault:
                        previous_length = self.document_vault[doc_id]
                        if current_length != previous_length:
                            logging.warning(f"[RESONATOR ALERT] Google Doc [{doc_id}] structurally altered! Delta: {current_length - previous_length} chars.")
                    
                    self.document_vault[doc_id] = current_length
                else:
                    logging.error(f"[ERROR] Google API connection validation anomaly. Status: {response.status_code}")
            except Exception as e:
                logging.error(f"[ERROR] Fault encountered matching Google connection stream: {e}")
            
            time.sleep(self.interval)

    def monitor_microsoft_word(self, drive_item_id, oauth_token):
        """Watches structural revisions inside Microsoft Graph OneDrive repositories."""
        url = f"https://microsoft.com{drive_item_id}"
        headers = {"Authorization": f"Bearer {oauth_token}"}
        logging.info(f"[DOCSHIELD] Initializing cTag vector watch for MS Word/OneDrive Item: {drive_item_id}")
        
        while self.is_running:
            try:
                response = requests.get(url, headers=headers, timeout=5)
                if response.status_code == 200:
                    item_data = response.json()
                    # cTag changes globally whenever individual file content changes inside OneDrive
                    current_ctag = item_data.get('cTag')
                    
                    if drive_item_id in self.document_vault:
                        previous_ctag = self.document_vault[drive_item_id]
                        if current_ctag != previous_ctag:
                            logging.warning(f"[RESONATOR ALERT] Microsoft Cloud Document [{drive_item_id}] has been updated! New cTag: {current_ctag}")
                    
                    self.document_vault[drive_item_id] = current_ctag
                else:
                    logging.error(f"[ERROR] Microsoft Graph communication failure. Status: {response.status_code}")
            except Exception as e:
                logging.error(f"[ERROR] Fault encountered matching Microsoft connection stream: {e}")
                
            time.sleep(self.interval)

def run_defense_daemon():
    # Placeholder cloud security asset markers (Replace with valid cloud credentials)
    GOOGLE_API_KEY = "AIzaSyYourSecretKeyHere..."
    SAMPLE_GOOGLE_DOC_ID = "1_DocumentIDStringFromYourGoogleDocsURL"
    
    MS_GRAPH_TOKEN = "eyJ0eXAiOiJKV1QiLC..."
    SAMPLE_ONEDRIVE_ITEM_ID = "01YOURDRIVEITEMID"

    monitor = DocShieldMonitor(check_interval_seconds=15)
    
    # Launch parallel tracking strands as decoupled background operations
    google_thread = Thread(target=monitor.monitor_google_doc, args=(SAMPLE_GOOGLE_DOC_ID, GOOGLE_API_KEY), name="Strand-GoogleDocs", daemon=True)
    ms_thread = Thread(target=monitor.monitor_microsoft_word, args=(SAMPLE_ONEDRIVE_ITEM_ID, MS_GRAPH_TOKEN), name="Strand-MSGraph", daemon=True)
    
    google_thread.start()
    ms_thread.start()
    
    logging.info("DocShield Defense Framework engine successfully armed and operational.")
    
    while True:
        try:
            time.sleep(1.0)
        except KeyboardInterrupt:
            logging.info("Background document validation engine interrupted by administrator command.")
            monitor.is_running = False
            sys.exit(0)

if __name__ == "__main__":
    run_defense_daemon()
