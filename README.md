````markdown
# ent_url_generator

This tool helps you quickly open **ORCID** or **Scopus** profile URLs from your **OTOMAP Data Collection Spreadsheet**.

---

## 📋 Prerequisites

Before starting, make sure you have these installed:

- [Python 3](https://www.python.org/downloads/)  
- [Git](https://git-scm.com/downloads)  

👉 If you’re not sure, you can check:

- For Python:  
  ```bash
  python --version
````

* For Git:

  ```bash
  git --version
  ```

If these commands show a version number, you’re good to go. If not, install them first.

---

## 🚀 Step 1: Open Terminal / Command Prompt

* **On Windows**

  1. Open **Command Prompt** (press `Win + R`, type `cmd`, and hit Enter).
  2. Type the following command and press Enter:

     ```cmd
     cd %userprofile%\Desktop
     ```

     This will take you to your Desktop folder.

* **On macOS / Linux**

  1. Open **Terminal**.
  2. Type the following command and press Enter:

     ```bash
     cd ~/Desktop
     ```

---

## 📂 Step 2: Create a Project Folder

Type these commands (press Enter after each):

```bash
mkdir otomap_url
cd otomap_url
```

This creates a folder named **otomap\_url** on your Desktop.

---

## ⬇️ Step 3: Download the Project

Run this command to download the tool from GitHub:

```bash
git clone https://github.com/wuhu2022/ent_url_generator.git
```

Then go into the folder:

```bash
cd ent_url_generator
```

---

## 📑 Step 4: Prepare Your Data Sheet

1. Download your **OTOMAP Data Collection Spreadsheet**.
2. Open it and **delete all extra sheets** so that only **your data sheet** remains.
3. Save this file into the `ent_url_generator` folder you created earlier.

---

## ⚙️ Step 5: Run the URL Extractor

Run the following command (replace the filename if yours is different):

```bash
python extract_urls.py "OTOMAP Data Collection Spreadsheet.xlsx"
```

---

## 🌐 Step 6: Open the URLs

* To open **all ORCID URLs**, double-click:

  ```
  open_all_orcid_urls.bat
  ```
* To open **all Scopus URLs**, double-click:

  ```
  open_all_scopus_urls.bat
  ```

Your default web browser will automatically open all the links.

---

## ❓ Troubleshooting

* **Command not found** → Make sure Python and Git are installed.
* **File not found error** → Double-check the spreadsheet name matches exactly (including `.xlsx`).
* **Nothing happens when running `.bat` files** → Try running them from Command Prompt instead of double-clicking.

---
