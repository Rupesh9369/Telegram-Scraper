
<p align="center">
  <img src="telegram-scrapper.jpeg" width="380" height="145">
</p>
<p align="center"><img src="https://img.shields.io/badge/Version-1.0-brightgreen"></p>
<p align="center">
  <a href="https://github.com/rupesh9369">
    <img src="https://img.shields.io/github/followers/rupesh9369?label=Follow&style=social">
  </a>
  <a href="https://github.com/rupesh9369/TeleGram-Group-Scraper">
    <img src="https://img.shields.io/github/stars/th3unkn0n/TeleGram-Group-Scraper?style=social">
  </a>
</p>
<p align="center">
  Telegram Group Scrapper
</p>

### Features

* ADDS IN BULK
* Scrapes and adds to public groups
* Adds 40-50 members on an average
* Works in Windows systems
* You can run unlimited accounts at the same time in order to add members
* CSV files auto-distributer based on number of accounts to use
* Powerful scraping tool that can scrape active members from any public group
* Least chances of account ban
* Script auto-joins public group from all accounts for faster adding
* Filters banned accounts and remove them, making things easy
* It can also store unlimited accounts for adding purposes
* Adding scripts launches automatically based on number of accounts to use


## Setup Guide

### 1. **Download and Install Required Software**

- **Python**: Download and install Python from [python.org](https://www.python.org/downloads/).
- **VS Code / PyCharm**: Download and install your preferred IDE:
  - [VS Code](https://code.visualstudio.com/)
  - [PyCharm](https://www.jetbrains.com/pycharm/)

### 2. **Clone the Repository**

```bash
git clone https://github.com/yourusername/your-repo.git
```

### 3. **Navigate to the Project Directory**

```bash
cd your-repo
```

### 4. **Open Project in VS Code**

```bash
code .
```

### 5. **Set Up the Virtual Environment**

```bash
python -m venv env
```

### 6. **Activate the Virtual Environment**

- **Windows**:

  ```bash
  .\env\Scripts\activate
  ```

- **macOS/Linux**:

  ```bash
  source env/bin/activate
  ```

### 7. **Install Dependencies**

```bash
pip install -r requirements.txt
```
## • API Setup
* Go to http://my.telegram.org  and log in.
* Click on API development tools and fill the required fields.
* put app name you want & select other in platform Example :
* copy "api_id" & "api_hash" after clicking create app ( will be used in setup.py )
### 8. **Update `setup.py` with Your Credentials**

Edit the `setup.py` file and update the following fields:

- `phone_number` = `"+91xxxxxxxxxxxxx"`
- `app_id` = `"12345555555"`
- `api_hash` = `"1d554xxxxxxxxxxxxxxxx4813fxxxxxxxxxxxxxx"`

Run the script and follow the prompt to enter the OTP sent to your Telegram account:

```bash
python setup.py
```

This will create a `config.txt` file.

### 9. **Prepare for Scraping**

Update `group_link.txt` with the group link you want to scrape members from.

### 10. **Run the Scraper**

```bash
python scraper.py
```

This will generate a `members.csv` file with the scraped members.

### 11. **Add Members to Your Group**

Run the `add.py` script:

```bash
python add.py
```

- Enter your own group link (e.g., `https://t.me/joinchat/XXXXXXX`).
- Provide the name of the `members.csv` file.

If you want to change the number of members added at a time (default is 50), update this line in `add.py`:

```python
def read_members(file_path, limit=50):
```

Change the `limit` to your desired number (e.g., 100 or more). The default value of 50 is recommended for optimal performance.

### 12. **All Done**

Your setup is complete. You can now manage your Telegram group members as needed.

---

### Credits

This project is maintained by [Rupesh](https://www.github.com/rupesh9369).


### Warning

* This tool is official and completely free to use. Do not buy if anyone tries to sell by copying script

### Contacts

* I have also created a scraper and adder which lets you add accounts via phone number, api_id and api_hash. If you need it contact me:

[![Telegram Contact](https://img.shields.io/badge/Telegram-Contact-brightgreen)](https://t.me/mrcrypttt) 
[![Telegram Contact](https://img.shields.io/badge/Telegram-Contact-brightgreen)](https://t.me/spoxy_dev) 
* If you have any problems regarding the script then write it in this groupchat:

[![Telegram Contact](https://img.shields.io/badge/Telegram-Contact-brightgreen)](https://t.me/mrcrypttt) 
[![Telegram Contact](https://img.shields.io/badge/Telegram-Contact-brightgreen)](https://t.me/spoxy_dev)


<h2 align="center">Visitors Counts👀</h2>
<a href="https://github.com/rupesh9369/Telegram-Members-Adder"><img alt="Cute Count" src="https://moe-counter.glitch.me/get/@Telegram-Scraper?theme=gelbooru" /></a>

### Contribution
- Fork this repo.
- Add new features.
- Create a new pull request for this branch.

<h1 align="center">⚠️ALERT⚠️</h1>

> **Disclaimer**  Please Note that this is a research project. I am by no means responsible for any usage of this tool. Use on your own behalf. I'm also not responsible if your accounts get banned due to extensive use of this tool

> **Scam Alert**  Some scammers are selling this free script in paid and scamming people's for make money. You don't need to pay anyone for any script, if you want any script in free of cost, you can message me on Whatsapp, Telegram, Instagram and Gmail which mentioned on my git profile. and i never message you for selling anything</samp></p>
