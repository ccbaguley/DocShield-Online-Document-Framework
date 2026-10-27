# DocShield Online Document Framework

An advanced, multi-threaded asset integrity daemon designed to monitor, track, and alert structural mutations inside online collaborative platforms silently.

## How It Works
Instead of local network endpoint monitoring, this daemon targets cloud service mesh APIs:
* **Strand Listeners:** Decoupled lightweight threads parsing active response deltas using the Google Docs REST API and the Microsoft Graph API.
* **Resonator Log Vectors:** Captures document length variances and OneDrive `cTag` mutations, generating silent log warnings to capture external edits instantly.

---

## Pre-Deployment Verification Requirements

Before executing, you must provision corresponding credentials inside your targeted developer dashboards:
1. **Google Docs Engine:** Enable the Google Docs API inside your **Google Cloud Console**, generate a standard API Key, and share your document as "Anyone with link can view".
2. **Microsoft Graph Engine:** Register an application identity inside **Azure Active Directory / Entra ID** and provision an active OAuth Access Token with `Files.Read` scope capability.

---

## Step-by-Step: Saving and Running the Script

### Step 1: Create and Save the Python File
Before running the script, you must save the source code into a Python file on your local machine using an IDE or text editor.

#### Option A: Using Visual Studio
1. Open **Visual Studio**.
2. Go to **File** -> **New** -> **File...** (or press `Ctrl + N`).
3. Select **Python File** from the template list and click **Open**.
4. Paste your `DocShieldDaemon.py` code into the empty editor window.
5. Go to **File** -> **Save As...** (or press `Ctrl + S`).
6. Name the file exactly **`DocShieldDaemon.py`** and choose a project folder (e.g., `C:\Users\YourUsername\Documents\DocShieldProject`).

#### Option B: Using Visual Studio Code (VS Code)
1. Open **VS Code**.
2. Create a new file by pressing `Ctrl + N`.
3. Paste the code into the empty file.
4. Save the file by pressing `Ctrl + S`.
5. Name the file exactly **`DocShieldDaemon.py`**. *Ensure the dropdown save type is set to "Python" or "All Files", so it doesn't accidentally append a `.txt` extension.*

#### Option C: Using Standard Windows Notepad
1. Open the Windows Start Menu, type **Notepad**, and open it.
2. Paste the code into the text area.
3. Click **File** -> **Save As...**
4. Set the **Save as type** dropdown to **`All Files (*.*)`** (Crucial step to prevent saving as a text file).
5. Name the file exactly **`DocShieldDaemon.py`** and click Save.

### Step 2: Establish Your Environment File
In the exact same folder workspace where you saved `DocShieldDaemon.py`, create a new configuration file named exactly **`.env`** and populates your asset strings:

```text
# DocShield Security Assets Matrix
GOOGLE_API_KEY=AIzaSyYourSecretKeyHere...
GOOGLE_DOC_ID=1_DocumentIDStringFromYourGoogleDocsURL

MS_GRAPH_TOKEN=eyJ0eXAiOiJKV1QiLC...
MS_ONEDRIVE_ITEM_ID=01YOURDRIVEITEMID
```

### Step 3: Run the Python Script Locally
Run the daemon directly from your command line interface to verify your cloud connection configurations before converting it into a service.

1. **Open Your Terminal:**
   * Press `Win + R`, type **`powershell`**, and hit Enter.

2. **Navigate to the Directory:**
   Move your terminal focus into the exact folder where you saved your file:
   ```powershell
   cd "C:\Users\YourUsername\Documents\DocShieldProject"
   ```

3. **Initialize the Script:**
   Execute the code using your machine's Python runtime engine:
   ```powershell
   python DocShieldDaemon.py
   ```
   *Verification Check:* The terminal will display initial activation text stamps, indicating that the background tracking loops are active and querying your target URLs.

4. **Terminate Execution:**
   To exit the interactive script execution and return to your standard folder path, press **`Ctrl + C`** within the terminal window.

---

## Production Installation & Deployment

### Step 1: Install Dependencies
Install Python's web transport module, the secure environment parser, and the compiler configuration:
```bash
pip install requests python-dotenv pyinstaller
```

### Step 2: Compile the Binary
Compile the script into a clean, standalone background executable. We add the `--collect-copy-metadata` flag to ensure the environment parser library initializes cleanly inside the compiled bundle:
```bash
python -m PyInstaller --onefile --noconsole --collect-copy-metadata dotenv DocShieldDaemon.py
```

### Step 3: Stage the Configuration and Application
Because the executable dynamically loads secrets at runtime, your configuration parameters must be placed directly adjacent to the application binary inside the system core directory.

Run this block inside an **Administrative PowerShell** window to transfer both assets to their secure staging area:
```powershell
# Create the permanent production directory
New-Item -ItemType Directory -Path "C:\ProgramData\DocShieldDefense" -Force

# Copy your compiled binary executable from the development project folder
Copy-Item -Path ".\dist\DocShieldDaemon.exe" -Destination "C:\ProgramData\DocShieldDefense\DocShieldDaemon.exe" -Force

# Copy your local secret configuration matrix to the production directory
Copy-Item -Path ".\.env" -Destination "C:\ProgramData\DocShieldDefense\.env" -Force
```

### Step 4: Register the Persistent Background Task
Register the framework with Task Scheduler using the universal security identifier (`S-1-5-18`). This enables the system to safely execute the daemon using your staged `.env` profiles automatically at every boot:
```powershell
$Action = New-ScheduledTaskAction -Execute "C:\ProgramData\DocShieldDefense\DocShieldDaemon.exe" -WorkingDirectory "C:\ProgramData\DocShieldDefense"; $Trigger = New-ScheduledTaskTrigger -AtStartup; Register-ScheduledTask -TaskName "DocShieldDaemon" -Action $Action -Trigger $Trigger -User "S-1-5-18" -RunLevel Highest -Force
```
*\*Note: Specifying the `-WorkingDirectory` parameter ensures that the background process initializes in the exact subfolder containing your `.env` configuration file.*

---

## Deployment Verification
Confirm that your document daemon is actively reading and validating data by analyzing the log output:

```powershell
Get-Content -Path "C:\ProgramData\DocShieldDefense\document_defense_daemon.log" -Tail 20 -Wait
```
*Verification Check:* Look for lines stamped with `[DOCSHIELD] Initializing structural tracking` to confirm active cloud synchronization patterns.

---

## Troubleshooting & Common Deployment Errors

If you encounter initialization errors during compilation or task registration, look up the resolution matrix below.

### 1. PyInstaller Administrative Compilation Restriction
* **Symptoms:** 
  ```text
  DEPRECATION: Running PyInstaller as admin is not necessary nor sensible...
  ERROR: Do not run pyinstaller from C:\Windows\system32.
  ```
* **Cause:** PyInstaller explicitly blocks compilation tasks executed within administrative windows or core system paths to prevent accidental binary corruptions.
* **Resolution:** Close your elevated administrator window, open a standard user terminal instance, navigate cleanly to your repository folder workspace, and re-execute:
  ```powershell
  cd "$HOME\Documents\YourRepositoryPath"
  python -m PyInstaller --onefile --noconsole --collect-copy-metadata dotenv DocShieldDaemon.py
  ```

### 2. Task Scheduler Account Mapping Fault (HRESULT 0x80070534)
* **Symptoms:**
  ```text
  Register-ScheduledTask : No mapping between account names and security IDs was done.
  ```
* **Cause:** Your host environment is utilizing non-English, localized, or highly customized regional security strings, preventing Windows from correctly interpreting the default literal string `"NT AUTHORITY\SYSTEM"`.
* **Resolution:** Run the commands as a single inline block using the universal Security Identifier (SID) sequence for the root system profile, which remains constant across all international language environments (`S-1-5-18`) as shown in Step 4 of the installation instructions.

---

## Uninstallation Procedure

To completely remove the framework from the system, execute the following commands from an **Administrative PowerShell** window.

### Step 1: Remove the Scheduled Task
```powershell
Unregister-ScheduledTask -TaskName "DocShieldDaemon" -Confirm:\$false
```

### Step 2: Terminate Running Processes
```powershell
Stop-Process -Name "DocShieldDaemon" -Force -ErrorAction SilentlyContinue
```

### Step 3: Clean Up System Files
```powershell
Remove-Item -Path "C:\ProgramData\DocShieldDefense" -Recurse -Force -ErrorAction SilentlyContinue
```

---

## License

Copyright (c) 2026 Candra

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, herby under the conditions of the MIT License.
