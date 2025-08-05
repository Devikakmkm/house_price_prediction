# Bangalore House Price Prediction

A machine learning-based web application that predicts house prices in Bangalore, India based on various parameters like location, square footage, number of bedrooms, and bathrooms.

## Features

- **Interactive Web Interface**: User-friendly interface to input property details
- **Location-based Prediction**: Supports predictions across various localities in Bangalore
- **Machine Learning Model**: Trained on real estate data to provide accurate price estimates
- **RESTful API**: Backend service that can be integrated with other applications

## Project Structure

```
.
├── client/                # Frontend files
│   ├── app.html          # Main HTML file
│   ├── app.js            # Frontend JavaScript
│   └── app.css           # Styling
├── server/               # Backend files
│   ├── artifacts/        # Model and configuration
│   │   ├── columns.json  # Location data
│   │   ├── server.py     # Flask server
│   │   └── compat.py     # Compatibility layer
│   └── util.py           # Utility functions
├── venv/                 # Python virtual environment
└── requirements.txt      # Python dependencies
```

## Prerequisites

- Python 3.8+ (tested with Python 3.12)
- pip (Python package manager)
- Web browser with JavaScript enabled

## Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd bangalore-house-price-prediction
   ```

2. **Set up a virtual environment** (recommended)
   ```bash
   python -m venv venv
   .\venv\Scripts\activate  # On Windows
   source venv/bin/activate  # On macOS/Linux
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

1. **Start the backend server**
   ```bash
   cd server/artifacts
   python server.py
   ```
   The server will start at `http://127.0.0.1:5000/`

2. **Open the frontend**
   - Navigate to the `client` folder
   - Open `app.html` in your web browser
  
   <img width="1862" height="915" alt="image" src="https://github.com/user-attachments/assets/061d830f-d059-420b-99a4-6e827ce52768" />


## Usage

1. Enter the area in square feet
2. Select the number of bedrooms (BHK)
3. Select the number of bathrooms
4. Choose the location from the dropdown
5. Click "Estimate Price" to see the predicted price

## API Endpoints

- `GET /` - API documentation
- `GET /get_location_names` - Get list of available locations
- `POST /predict_home_price` - Predict house price
  - Parameters: `total_sqft`, `location`, `bhk`, `bath`

## Technical Details

- **Backend**: Python Flask
- **Frontend**: HTML, CSS, JavaScript (jQuery)
- **Machine Learning**: Scikit-learn (Linear Regression)
- **Data**: Pre-trained model on Bangalore real estate data

## Troubleshooting

- **CORS Issues**: Ensure the backend server is running and accessible
- **Location Not Loading**: Check browser console for JavaScript errors
- **Prediction Errors**: Verify all fields are filled correctly

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Dataset sourced from [Kaggle](https://www.kaggle.com/)
- Built for educational purposes

## Future Improvements

- Add user authentication
- Implement a more sophisticated ML model
- Add more location data
- Include property images and more details
- Mobile-responsive design
