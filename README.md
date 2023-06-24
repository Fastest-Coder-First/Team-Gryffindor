<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="#">
    <img src="https://github.com/Gryffindor-House/Innovate-with-MongoDB/blob/Innovate-Chakra/images/logo.png" alt="Logo" width="150" height="80">
  </a>
</div>

<h1 align="center">Weather Forecasting CLI</h1>
</div>

<!-- ABOUT THE PROJECT -->

## About The Project

### Introduction

- The CLI Weather Forecast Application is a command-line interface (CLI) tool designed to provide weather forecasts for a given city or location. It utilizes weather data from a reliable weather API to generate accurate forecasts.
- Additionally, the application allows users to generate graphs or convert weather data into CSV format for further analysis or integration with other tools.

### Features

1. Weather Forecast: The application retrieves current weather conditions and a five-day forecast for the specified location.
   Location Search: Users can search for a location using the city name or geographical coordinates (latitude and longitude).
2. Graph Generation: The application can generate graphs to visualize the weather data, such as temperature, precipitation, or wind speed, for better understanding and analysis.
3. CSV Conversion: Weather data can be converted into Comma-Separated Values (CSV) format, which enables easy importing and manipulation of data in spreadsheet software or other tools.

### CLI Help

```sh
   python app.py -h
```

![CLI_HELP](https://github.com/Fastest-Coder-First/Team-Gryffindor/blob/main/images/1.png)
</br>

### CLI Weather Forecast Usage

1. Using Latitude and Longitude

```sh
   python app.py -lat 20.0 -lon 34.0
```

![LAT_LAN](https://github.com/Fastest-Coder-First/Team-Gryffindor/blob/main/images/2.png)

2. Using City Name

```sh
   python app.py -city "Chennai"
```

![CITY](https://github.com/Fastest-Coder-First/Team-Gryffindor/blob/main/images/3.png)

3. Converting weather data to CSV

```sh
   python app.py -city "Chennai" --to-csv
```

![csv](https://github.com/Fastest-Coder-First/Team-Gryffindor/blob/main/images/4.png)

4. Generating temperature graph

```sh
   python app.py -city "London" --temp-graph
```

![graph](https://github.com/Fastest-Coder-First/Team-Gryffindor/blob/main/images/5.png)
![graph](https://github.com/Fastest-Coder-First/Team-Gryffindor/blob/main/images/6.png)

</br>

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- API's Used -->

## API's Used

- [MeteoAPI](https://open-meteo.com/en/docs)
- [OpenWeatherAPI](https://openweathermap.org/api)
<p align="right">(<a href="#readme-top">back to top</a>)</p>
<!-- GETTING STARTED -->

## Getting Started

To get a local copy up and running follow these simple example steps.

### Installation

1. Get a free API Key at [https://example.com](https://example.com)
2. Clone the repo
   ```sh
   git clone https://github.com/Fastest-Coder-First/Team-Gryffindor
   ```
3. Navigate to the project directory
   ```sh
   cd Team-Gryffindor
   ```
4. Install Python packages
   ```sh
   pip install -r requirements.txt
   ```
5. Enter your API keys in `configs/config.js`
   ```
   api_key": "API_KEY",
   ```
6. Run the app
   ```sh
    python app.py
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- USAGE EXAMPLES -->

## Usage of Copilot

### Error Handling

- Copilot's ability to suggest error handling and debugging code snippets was another valuable asset during development. It helped me identify potential edge cases and provided suggestions for error handling and exception handling mechanisms. By incorporating Copilot's suggestions
  - Certain instances were
    - When the user enters an invalid location, the application will display an error message and exit.

### Accelaerated Development

- Github copilot enabled me to accelerate the development process by providing code snippets for common tasks such as reading and writing files, parsing JSON data, and generating graphs. This allowed me to focus on the core functionality of the application.

- Repetitive tasks such as reading and writing files, parsing JSON data, and generating graphs were made easier by Github Copilot's ability to provide code snippets for common tasks. This allowed me to focus on the core functionality of the application and save time on repetitive tasks.

- Its ability to give extensive suggestions for function and variable names was also beneficial. This allowed me to save time on naming variables and functions and focus on the core functionality of the application.

- Copilot's ability to suggest comments for functions and classes was also beneficial. This allowed me to save time on writing comments and focus on the core functionality of the application.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTACT -->

## Contact

![https://www.linkedin.com/in/ashwin-balasubramanian-0293691a5/][linkedin-shield] ![https://github.com/sinking8](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
