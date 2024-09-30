

# Indian Students Heatmap

This project visualizes the distribution of Indian students across different locations using a heatmap. The heatmap allows users to see the concentration of students based on their geographical coordinates.

## Overview

The application is built using:

- **Pandas**: For data manipulation and analysis.
- **Folium**: To create interactive maps.
- **Shiny**: A Python framework for building web applications.

## Data

The application uses a CSV file named `indian_students_final.csv`, which contains the following columns:

- `Latitude`: The latitude of the location.
- `Longitude`: The longitude of the location.
- `No of Indian Students`: The number of Indian students at that location.

Make sure to include this CSV file in the project directory.

## Installation

1. Clone this repository or download the files.
2. Install the required packages if you haven't already:

   ```bash
   pip install pandas folium shiny
   ```

## Usage

1. Ensure that the `indian_students_final.csv` file is present in the project directory.
2. Run the application using the following command:

   ```bash
   python app.py
   ```

3. Open a web browser and go to `http://127.0.0.1:8000` to view the heatmap.

## Features

- An interactive heatmap showing the distribution of Indian students.
- The size of the heatmap points is proportional to the number of students at each location.
- A footer providing additional information about the heatmap.

## Contributing

Feel free to contribute by submitting issues or pull requests if you have suggestions for improvements or new features.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments

- Thanks to the developers of Pandas, Folium, and Shiny for providing excellent tools for data visualization and web development.

```

### Notes:
- Replace `app.py` with the actual filename of your script if it's different.
- You can modify the content to better fit your project's specifics, such as the description of the dataset and any additional features or functionalities.
