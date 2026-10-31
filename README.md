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
4. Paste your code into the empty editor window.
5. Go to **File** -> **Save As...** (or press `Ctrl + S`).
6. Name the file exactly **`DocShieldDaemon.py`** and choose your local repository folder path (e.g., `C:\<YOUR_REPOSITORY_PATH>\DocShield\`).

#### Option B: Using Visual Studio Code (VS Code)
1. Open **VS Code**.
2. Create a new file by pressing `Ctrl + N`.
3. Paste the code into the empty file.
4. Save the file by pressing `Ctrl + S`.
5. Name the file exactly **`DocShieldDaemon.py`**. Ensure the dropdown save type is set to "Python" or "All Files", so it doesn't accidentally append a `.txt` extension.

#### Option C: Using Standard Windows Notepad
1. Open the Windows Start Menu, type **Notepad**, and open it.
2. Paste the code into the text area.
3. Click **File** -> **Save As...**
4. Set the **Save as type** dropdown to **`All Files (*.*)`** to prevent saving as a text file.
5. Name the file exactly **`DocShieldDaemon.py`** and click Save.

### Step 2: Establish Your Environment File
To prevent Windows from hidden-appending a text extension (like `.env.txt`), you can use a single-line command to force create the perfectly formatted hidden environmental file.
Open your standard terminal, navigate to your folder path, and paste this command exactly:

"GOOGLE_API_KEY=AIzaSyYourSecretKeyHere...`nGOOGLE_DOC_ID=1_DocumentIDStringFromYourGoogleDocsURL`nMS_GRAPH_TOKEN=eyJ0eXAiOiJKV1QiLC...`nMS_ONEDRIVE_ITEM_ID=01YOURDRIVEITEMID" | Out-File -FilePath .env -Encoding utf8

### Step 3: Run the Python Script Locally
Run the daemon directly from your command line interface to verify your cloud connection configurations before converting it into a service.
1. **Open Your Terminal:** Press `Win + R`, type **`powershell`**, and hit Enter.
2. **Navigate to the Directory:** Move your terminal focus into your target repository workspace path:
   cd "C:\<YOUR_REPOSITORY_PATH>"
3. **Initialize the Script:** Execute the code using your machine's Python runtime engine:
   python DocShieldDaemon.py
   *Verification Check:* The terminal will display initial activation text stamps, indicating that the background tracking loops are active and querying your target URLs.
4. **Terminate Execution:** To exit the interactive script execution and return to your standard folder path, press **`Ctrl + C`** within the terminal window.

---

## Production Installation & Deployment

### Step 1: Install Dependencies
Install Python's web transport module, the secure environment parser, and the compiler configuration:
python -m pip install requests python-dotenv pyinstaller

### Step 2: Compile the Binary
Compile the script into a clean, standalone background executable. Note that contemporary PyInstaller syntax uses the explicit `--copy-metadata` flag to package environmental parser metrics:
python -m PyInstaller --onefile --noconsole --copy-metadata python-dotenv DocShieldDaemon.py

### Step 3: Stage the Configuration and Application
Because the executable dynamically loads secrets at runtime, your configuration parameters must be placed directly adjacent to the application binary inside the system core directory.
Run this block inside an **Administrative PowerShell** window to transfer both assets to their secure staging area:

# Create the permanent production directory
New-Item -ItemType Directory -Path "C:\ProgramData\DocShieldDefense" -Force
# Copy your compiled binary executable from the development project folder
Copy-Item -Path ".\dist\DocShieldDaemon.exe" -Destination "C:\ProgramData\DocShieldDefense\DocShieldDaemon.exe" -Force
# Copy your local secret configuration matrix to the production directory
Copy-Item -Path ".\.env" -Destination "C:\ProgramData\DocShieldDefense\.env" -Force

### Step 4: Register the Persistent Background Task
Register the framework with Task Scheduler using the universal security identifier (`S-1-5-18`). This enables the system to safely execute the daemon using your staged `.env` profiles automatically at every boot:

$Action = New-ScheduledTaskAction -Execute "C:\ProgramData\DocShieldDefense\DocShieldDaemon.exe" -WorkingDirectory "C:\ProgramData\DocShieldDefense"; $Trigger = New-ScheduledTaskTrigger -AtStartup; Register-ScheduledTask -TaskName "DocShieldDaemon" -Action $Action -Trigger $Trigger -User "S-1-5-18" -RunLevel Highest -Force

*\*Note: Specifying the `-WorkingDirectory` parameter ensures that the background process initializes in the exact subfolder containing your `.env` configuration file.*

---

## Deployment Verification
Confirm that your document daemon is actively reading and validating data by analyzing the log output:
Get-Content -Path "C:\ProgramData\DocShieldDefense\document_defense_daemon.log" -Tail 20 -Wait
*Verification Check:* Look for lines stamped with `[DOCSHIELD] Initializing structural tracking` to confirm active cloud synchronization patterns.

---

## Troubleshooting & Common Deployment Errors
If you encounter initialization errors during compilation or task registration, look up the resolution matrix below.

### 1. PyInstaller Administrative Compilation Restriction
* **Symptoms:** 
  DEPRECATION: Running PyInstaller as admin is not necessary nor sensible...
  ERROR: Do not run pyinstaller from C:\Windows\system32.
* **Cause:** PyInstaller explicitly blocks compilation tasks executed within administrative windows or core system paths to prevent accidental binary corruptions.
* **Resolution:** Close your elevated administrator window, open a standard user terminal instance, navigate cleanly to your repository folder workspace, and re-execute:
  cd "C:\<YOUR_REPOSITORY_PATH>"
  python -m PyInstaller --onefile --noconsole --copy-metadata python-dotenv DocShieldDaemon.py

### 2. Script File Does Not Exist Error
* **Symptoms:**
  ERROR: Script file 'DocShieldDaemon.py' does not exist.
* **Cause:** Your local workspace directory has not been populated with the primary script filename indicator template yet.
* **Resolution:** Ensure your active source code asset matches the target build argument parameter, or duplicate your main python file explicitly before triggering the compiler configuration execution loops:
  Copy-Item -Path ".\YourOriginalScriptName.py" -Destination ".\DocShieldDaemon.py" -ErrorAction SilentlyContinue
  python -m PyInstaller --onefile --noconsole --copy-metadata python-dotenv DocShieldDaemon.py

### 3. Task Scheduler Account Mapping Fault (HRESULT 0x80070534)
* **Symptoms:**
  Register-ScheduledTask : No mapping between account names and security IDs was done.
* **Cause:** Your host environment is utilizing non-English, localized, or highly customized regional security strings, preventing Windows from correctly interpreting the default literal string `"NT AUTHORITY\SYSTEM"`.
* **Resolution:** Run the commands as a single inline block using the universal Security Identifier (SID) sequence for the root system profile, which remains constant across all international language environments (`S-1-5-18`) as shown in Step 4 of the installation instructions.

---

## Uninstallation Procedure
To completely remove the framework from the system, execute the following commands from an **Administrative PowerShell** window.

### Step 1: Remove the Scheduled Task
Unregister-ScheduledTask -TaskName "DocShieldDaemon" -Confirm:$false

### Step 2: Terminate Running Processes
Stop-Process -Name "DocShieldDaemon" -Force -ErrorAction SilentlyContinue

### Step 3: Clean Up System Files
Remove-Item -Path "C:\ProgramData\DocShieldDefense" -Recurse -Force -ErrorAction SilentlyContinue

# DocShield Online Document Framework

An advanced, keyless multi-threaded asset integrity daemon designed to monitor, track, and alert structural mutations inside online collaborative platforms silently.

## Overview & Core Workflow
The daemon targets cloud public data layers using a lightweight Keyless Hash Monitor parsing active response deltas via Google's public export server grid, capturing external edits instantly via SHA-256 hash fingerprints.

## Summary of Sections in Full Documentation
* **Pre-Deployment Verification:** Configure your Google Docs sharing permissions to *Anyone with the link* (Viewer role) and ensure your workspace contains configuration markers.
* **Saving and Running the Script:** Instructions are provided for creating `DocShieldFinal.py` using Visual Studio, VS Code, or Notepad, establishing your `.env` configuration file via PowerShell, and running the script locally (`python -B .\DocShieldFinal.py`).
* **Production Installation & Deployment:** Steps cover installing dependencies (`requests`, `python-dotenv`, `pyinstaller`), compiling the binary, staging the application in `C:\ProgramData\DocShieldDefense`, and registering a persistent background task via Task Scheduler using the system SID (`S-1-5-18`).
* **Troubleshooting:** Addresses common errors including PyInstaller administrative restrictions, missing script file errors, and Task Scheduler account mapping faults (`HRESULT 0x80070534`).
* **Uninstallation:** Provides commands to unregister the scheduled task, stop running processes, and clean up system directories.
* **License:** Standard MIT License (Copyright (c) 2026 Candra).


---

## License
Copyright (c) 2026 Candra

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, herby under the conditions of the MIT License.
