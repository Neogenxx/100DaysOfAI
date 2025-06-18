### 📅 Day 4: Weather App

This project fetches real-time weather data for any city using the **OpenWeatherMap API**, displays it in the terminal, and visualizes key metrics like temperature, humidity, and wind speed using a bar chart.

---

### 📦 Libraries Used

| Library      | Purpose                                     |
| ------------ | ------------------------------------------- |
| `requests`   | To make API calls to OpenWeatherMap         |
| `os`         | To handle file paths and environment access |
| `json`       | To work with JSON data formats              |
| `matplotlib` | To visualize weather metrics in bar graphs  |
| `dotenv`     | To load the API key from `.env` file        |

---

### 🧠 Key Functions

#### `get_weather(city)`

* Fetches weather data for the given city using OpenWeatherMap.
* Extracts and displays:

  * Temperature (°C)
  * Weather description
  * Humidity (%)
  * Wind speed (m/s)
* Logs the raw weather response to `weather_log.json`.

#### `visualize_weather(city, temp, humidity, wind_speed)`

* Creates a bar chart comparing the key weather metrics.
* Saves the chart as `weather_visual.png` in the same folder.

---

### 🚀 How to Run

1. **Install dependencies** (inside a virtual environment):

   ```bash
   pip install -r requirements.txt
   ```

2. **Create a `.env` file** in the same directory with your API key:

   ```
   API_KEY=your_openweathermap_api_key
   ```

3. **Run the script**:

   ```bash
   python weather_app.py
   ```

---

### 📂 Output

* `weather_log.json`: Stores the raw JSON weather data (updated each run).
* `weather_visual.png`: Bar graph of current weather metrics.


