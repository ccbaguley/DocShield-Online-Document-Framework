import os
import time
import logging
import threading
import hashlib
import requests
from dotenv import load_dotenv

# Configure clean console and production logging outputs
logging.basicConfig(
    level=logging.INFO, 
    format="%(asctime)s [%(levelname)s] (%(threadName)s) %(message)s"
)

class KeylessDocShieldEngine:
    def __init__(self):
        load_dotenv()
        self.google_doc_id = os.getenv("GOOGLE_DOC_ID")
        self.last_structural_hash = None
        self.is_running = True

    def monitor_public_doc(self):
        if not self.google_doc_id:
            logging.error("[DOCSHIELD] Google Document ID missing from .env configuration.")
            return

        # Pristine, explicitly separated web path routing to the public export layout server
        url = f"https://google.com{self.google_doc_id}/export?format=txt"
        logging.info(f"[DOCSHIELD] Launching keyless structural hash tracking for Doc ID: {self.google_doc_id}")

        while self.is_running:
            try:
                # Custom User-Agent prevents automated scraper blocking policies
                headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
                response = requests.get(url, headers=headers, timeout=15)
                
                if response.status_code == 200:
                    raw_content = response.content
                    current_hash = hashlib.sha256(raw_content).hexdigest()

                    if self.last_structural_hash is None:
                        self.last_structural_hash = current_hash
                        logging.info(f"[DOCSHIELD] Keyless Base Verification Fingerprint Established: [{current_hash[:12]}]")
                    
                    elif current_hash != self.last_structural_hash:
                        logging.warning(f"[MUTATION DETECTED] Structural file change identified! Old Hash: {self.last_structural_hash[:12]} -> New Hash: {current_hash[:12]}")
                        self.last_structural_hash = current_hash  # Dynamic reset updates baseline immediately
                        
                elif response.status_code in:
                    logging.error("[DOCSHIELD] Access Denied. Verify share settings are open to 'Anyone with link can view'.")
                else:
                    logging.error(f"[DOCSHIELD] Public Cloud Grid Transport Fault. Status: {response.status_code}")
            except Exception as e:
                logging.error(f"[DOCSHIELD] Scraping Loop Exception: {str(e)}")
            
            # Polling cadence optimized to preserve bandwidth and stealth thresholds
            time.sleep(10)

    def execute_daemon(self):
        logging.info("[DOCSHIELD] Keyless DocShield Defense Engine active and armed.")
        tracking_thread = threading.Thread(target=self.monitor_public_doc, name="Strand-KeylessGoogle", daemon=True)
        tracking_thread.start()

        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            logging.info("[DOCSHIELD] Keyless Daemon manual shutdown sequence completed.")
            self.is_running = False

if __name__ == "__main__":
    daemon = KeylessDocShieldEngine()
    daemon.execute_daemon()
