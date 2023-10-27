# Rain Forecast App
 Queries weather API to check for possibility of rain within the next 12 hours. Sends an SMS via Twilio's SMS API to user's phone number(s) to remind them to bring an umbrella while going out if there is chance of rain. 

 I used [WeatherAPI](https://www.weatherapi.com) since it offers hourly weather forecast data upto 14 days unlike most other APIs.

## Prerequisites:
- Create an account in [WeatherAPI](https://www.weatherapi.com) and generate your API key.
- Create an account in [Twilio](https://www.twilio.com/en-us), generate your Twilio phone number, verify your personal number(s) and set aside your Twilio Auth Token and Account SID.
- Create environment variables containing your private API keys and tokens within your local environment by typing in terminal:
  
  ```bash
   export WEATHER_API_KEY=weather_api_key
   export TWILIO_AUTH_TOKEN=twilio_api_key
  ```
  
- Python 3.9 & up

### To run in terminal:
- Open Powershell in the local repository folder
- Type:

  ```bash
   python main.py
  ```

### Deployment
You could automate the python file to run everyday at 7 AM in the morning and send a reminder to you before you head out for the day. In order to do this, host the script on [PythonAnywhere](https://www.pythonanywhere.com). 

- Create a free account, go the Files and upload the `main.py` file.
- Next, click on Consoles and under Other click Bash. Once the terminal opens, first set the environment variables for the API keys.
- Run `python3 main.py`
  - If you encountered an error in the console, check this [troubleshooting guide](https://help.pythonanywhere.com/pages/TwilioBehindTheProxy/).
- Once your program works correctly, head to Tasks. PythonAnywhere allows all of its users to schedule 1 script to run everyday for free. Under Scheduled tasks, create a new task.
- Under Frequency, set the timing you want the program to remind you at in UTC time.
- Under command mention:
 
  ```bash
  export WEATHER_API_KEY=weather_api_key; export TWILIO_AUTH_TOKEN=twilio_api_key; python3 main.py
  ```

Now your program will be run once everyday at the time you specified. In case of rainfall forecast within the next 12 hours from its runtime, an automatic SMS will be sent to your phone number(s).
