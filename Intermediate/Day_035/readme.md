# Day 35: Weather Forecast API & SMS Alert

## Goal

- Check the daily weather forecast using an API.
- If rain is predicted, send an SMS alert to a specified number every morning at 7 AM.

## Steps

1. **Fetch Weather Data**
    - Use a weather API (e.g., OpenWeatherMap) to get the daily forecast.

2. **Check for Rain**
    - Parse the API response to determine if rain is expected.

3. **Send SMS Alert**
    - Use an SMS service (e.g., Twilio) to send a notification if rain is forecasted.

4. **Schedule the Task**
    - Automate the script to run every day at 7 AM (using cron, Task Scheduler, or a cloud function).

## Example Workflow

- Fetch the weather forecast for your location using a weather API.
- Analyze the forecast data to check if rain is expected for the current day.
- If rain is detected, send an SMS alert to your chosen phone number using an SMS service.
- Set up a scheduler to run this process automatically every morning at 7 AM.

## Notes

- Replace placeholders with your actual API keys and phone numbers.
- Use a scheduler (like `pythonanywhere`) to run the script every morning at 7 AM.
