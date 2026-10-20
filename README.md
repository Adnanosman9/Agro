<div align="center">

# Agrowise - A farming related platform

</div>

Agrowise is a website built to make the farming with proper situation and environmental info instead guessing. By analyzing soil NPK with real-time local weather data, the web runs classifications through the ML model to recommend the best crop for a specific field.

**Live Website:** https://agro-wa64.onrender.com/

### **>> NOTE:** This version represents a stable, fully functioning core MVP. I wanted to pack it out with advanced systems (such as voice control and other APIs connected and I was trying to work on them), but this will require a long time to build and get approved. Due to tight event deadlines, I am shipping this working version to lock down my milestone baseline first. 

## Live Prediction Preview

<img width="464" height="240" alt="1020 (3)" src="https://github.com/user-attachments/assets/21649196-367c-405f-99a7-ccb6c33fe1b3" />


## How It Works
* The user inuts their data in specific data points for Nitrogen (N), Phosphorus (P), Potassium (K), and soil pH levels.
* Instead of making users look for weather and environmental data manually, the app uses open-meteo api and instantly pulls local live temperature and humidity metrics.
* The combined parameters are structured and passed to a machine learning model hosted directly on the web server to calculate the highest-yielding crop recommendation.

## The Architecture & Tough Bugs I Solved

I made the data pipeline and deployed the entire application stack live on Render connected directly to the machine learning core. 

The biggest roadblock was managing the API calls for live weather. Connecting the weather api with the website backend was being hard for me. **Claude sonnet 4.6** was used to solve this connection issue. 

## Resources 

Drop data was downloaded from kaggle.com

## Project Status & Next Steps 

I am actively building out the following features in my local environment to push over the coming days:
* **Voice Commands Integration:** Building an audio overlay so users can speak their soil values aloud instead of typing them into form inputs.
* **Expanded Agricultural APIs:** Integrating historical rainfall data logs and soil degradation index endpoints to make the model predictions even more precise over a long-term calendar year.

## License
MIT
