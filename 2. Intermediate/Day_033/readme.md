# Day 033: ISS Overhead Automation & Weekly Kanye Quotes

## Tasks

### 1. ISS Overhead Notification
- **Goal:** Create an automation that notifies you when the International Space Station (ISS) is overhead.
- **Steps:**
    - Use an API (e.g., [Open Notify ISS API](http://open-notify.org/Open-Notify-API/ISS-Location-Now/)) to get the current location of the ISS.
    - Check if the ISS is overhead your location (within a certain latitude/longitude range).
    - Automate notifications (e.g., email, SMS, or console log).

### 2. Weekly Kanye Quotes
- **Goal:** Fetch and display a weekly quote from Kanye West.
- **Steps:**
    - Use an API (e.g., [Kanye Rest API](https://api.kanye.rest/)) to get a random Kanye quote.
    - Schedule the script to run once a week (using cron, Task Scheduler, or a Python scheduler like `schedule`).

## Example APIs

- **ISS Location:**  
    `http://api.open-notify.org/iss-now.json`
- **Kanye Quote:**  
    `https://api.kanye.rest/`

## Example Python Libraries

- `requests` for API calls
- `smtplib` or `twilio` for notifications
- `schedule` or `cron` for automation

---

**Challenge:** Combine both features into a single script for daily automation and weekly inspiration!
