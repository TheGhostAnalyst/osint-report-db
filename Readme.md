# 🕵️ OSINT Report Template Database (CLI Tool)

A lightweight, command-line based database application for storing and searching Open-Source Intelligence (OSINT) report templates. Designed for solo analysts, researchers, and investigators who need a fast and structured way to manage intel without relying on heavy tools.

Built by **TheGhostAnalyst**.

---

## 📌 Features

- 📄 Save detailed OSINT report templates with:
  - Full name, username(s), bio, contacts
  - Location, DOB, gender, geolocation, relationships
  - Job title, company, recent activity
  - Social media data
  - Sources & notes
  - Timestamps

- 🔍 Search saved reports by title

- 📂 View all report titles in the database

- 🧠 Optional fields supported — skip what you don't know

- 💾 Persistent local storage using Python’s `shelve` module

---

## ⚙️ How It Works

```bash
1. Choose an action:
   - Save new OSINT report
   - Search saved reports
   - List all saved report titles
   - Exit

2. Fill in known data — press Enter to skip any field.

3. Data is saved locally in `OSINTbase.db` with a timestamp.

4. Search or retrieve reports by title any time.
````

---

## 🛠️ Tech Stack

* 🐍 **Python 3.10+**
* 🧾 [`pyinputplus`](https://pypi.org/project/PyInputPlus/) — for validated and user-friendly input
* 💾 `shelve` — simple object persistence for local storage
* ⏰ `datetime` & `time` — for tracking data collection

---

## 📁 Example Output

```
Fullname                    : John Doe
Username(s)                 : johnd_thetruth
Date of Birth               : 1993-04-17
Location                    : Berlin, Germany
Gender                      : Male
Social Followers in Total   : Instagram: 10k, X: 4.5k
All Social Media Username(s): Instagram: johnd_insta, X: realjohnd
Description                 : Public speaker and activist
Contact Phone(s)            : +49-123-4567890
Contact Email(s)            : john.d@example.com
Job Title(s)                : Investigative Journalist
Company/Employer            : Freelance
Relationship                : Single
Recent Activity             : Tweeted article on dark web markets
Age                         : 32
Geolocation                 : GPS: 52.5200° N, 13.4050° E
Sources                     : LinkedIn, Instagram, Pipl
Short Note                  : Appears at protests often
Timestamp of collection     : 2025-08-25 23:02
----------------------------------------
```

---

## 🚀 Getting Started

1. **Clone the repo** (or just download the `.py` file):

```bash
git clone https://github.com/TheGhostAnalyst/osint-report-db.git
cd osint-report-db
```

2. **Install dependencies**:

```bash
pip install pyinputplus
```

3. **Run the script**:

```bash
python3 OSINTdatabase.py
```

---

## ✍️ Author

**TheGhostAnalyst**
🔗 [GitHub](https://github.com/TheGhostAnalyst)
💬 OSINT | Cybersecurity | Python Projects

---

## 📜 License

MIT License — feel free to use, modify, and share with credit.

---

## 💡 Future Ideas

* 🖥️ GUI version using Tkinter or PyQt
* 🌐 Web app version with Flask
* 📤 Export to PDF/CSV for reports
* 🔐 Add encryption or login system
* 🧠 AI-assisted autofill for common OSINT data fields

---

> *“If it's online, it's intel.” — TheGhostAnalyst*

