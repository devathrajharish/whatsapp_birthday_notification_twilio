
# **Birthday Reminder Bot**  

This Python-based project automates birthday reminders and messages using GitHub Actions and Twilio. The script checks for upcoming birthdays, sends reminder messages a day before the birthday, and sends birthday wishes on the day of the birthday.  

---

## **Features**  
- Automated daily checks for upcoming birthdays.  
- Sends a **reminder message** one day before the birthday.  
- Sends a **birthday wish** on the day of the birthday.  
- Secure handling of sensitive information like Twilio credentials and birthday data using GitHub Secrets.  
- Free hosting via GitHub Actions with scheduling support.  

---

## **Technologies Used**  
- **Python**: Core programming language.  
- **Twilio API**: For sending WhatsApp or SMS messages.  
- **GitHub Actions**: To schedule and automate the script execution.  

---

## **How It Works**  

1. **Twilio Setup**:  
   - Sign up for a free Twilio account at [Twilio](https://www.twilio.com/).  
   - Get your **Account SID** and **Auth Token** from the Twilio console.  
   - Set up a Twilio number to send messages.  

2. **GitHub Secrets**:  
   - Add the following secrets to your repository:  
     - `TWILIO_ACCOUNT_SID`: Your Twilio Account SID.  
     - `TWILIO_AUTH_TOKEN`: Your Twilio Auth Token.  
     - `BIRTHDAYS_DICT`: A JSON string containing the birthdays dictionary, e.g.,  
       ```json
       {"Mom": "01-20", "Dad": "02-15", "Sister": "03-10"}
       ```  

3. **GitHub Actions Workflow**:  
   - The script runs daily at a specified time using GitHub Actions.  
   - It sends messages based on the current date and the birthdays dictionary.  

---

## **Setup and Deployment**  

### **1. Clone the Repository**  
```bash  
git clone https://github.com/<your-username>/birthday-reminder-bot.git  
cd birthday-reminder-bot  
```  

### **2. Install Dependencies**  
Install the required Python libraries locally (for testing):  
```bash  
pip install twilio  
```  

### **3. Test the Script Locally**  
- Create a `.env` file for local testing:  
  ```env  
  TWILIO_ACCOUNT_SID=your_account_sid  
  TWILIO_AUTH_TOKEN=your_auth_token  
  BIRTHDAYS_DICT={"Mom": "01-20", "Dad": "02-15", "Krishna": "03-10"}  
  ```  
- Use `python-dotenv` to load these variables:
  ```bash
  pip install python-dotenv
  ```  
- Run the script locally:  
  ```bash  
  python script.py  
  ```  

### **4. Add Secrets to GitHub**  
- Go to your repository’s **Settings > Secrets and Variables > Actions**.  
- Add the following secrets:  
  - `TWILIO_ACCOUNT_SID`  
  - `TWILIO_AUTH_TOKEN`  
  - `BIRTHDAYS_DICT`  

### **5. GitHub Actions Workflow**  
Ensure your repository has a `.github/workflows/birthday_reminder.yml` file. Here's an example workflow:  
```yaml  
name: Run Birthday Reminder  

on:  
  schedule:  
    - cron: '0 9 * * *'  # Runs daily at 9:00 AM UTC  

jobs:  
  build:  
    runs-on: ubuntu-latest  

    steps:  
      - name: Checkout code  
        uses: actions/checkout@v3  

      - name: Set up Python  
        uses: actions/setup-python@v4  
        with:  
          python-version: '3.x'  

      - name: Install dependencies  
        run: |  
          pip install twilio  

      - name: Run Script  
        env:  
          TWILIO_ACCOUNT_SID: ${{ secrets.TWILIO_ACCOUNT_SID }}  
          TWILIO_AUTH_TOKEN: ${{ secrets.TWILIO_AUTH_TOKEN }}  
          BIRTHDAYS_DICT: ${{ secrets.BIRTHDAYS_DICT }}  
        run: |  
          python script.py  
```  

---

## **Example Birthday Dictionary**  
Store the birthdays in JSON format:  
```json  
{
  "Mom": "01-20",
  "Dad": "02-15",
  "Sister": "03-10"
}  
```  

---

## **How to Customize**  
- **Change Message Content**: Edit the `script.py` file to modify the birthday and reminder messages.  
- **Adjust Schedule**: Update the `cron` expression in the workflow file to change when the script runs.  

---

## **Limitations**  
- **GitHub Actions Free Tier**: Limited to 2000 minutes/month for free accounts. Ensure the script execution is efficient.  
- **Twilio Free Tier**: Messages may contain a Twilio promotional footer and until you run out of credits.  

---

## **Future Enhancements**  
- Add support for multiple messaging services (e.g., Telegram, Email).  
- Fetch birthdays from a remote database or spreadsheet (e.g., Google Sheets).  
- Add notification retries for failed messages.  

---

## **Contributing**  
Contributions are welcome! Feel free to submit a pull request or report issues.  


