# Will-You-Survive 🚢

A Flask-based machine learning web app that predicts whether a passenger would have survived the Titanic disaster based on input features like age, fare, number of siblings/spouses, and number of parents/children aboard.

## Features 🛠️
- Web-based prediction using Flask
- Pre-trained machine learning model for survival prediction
- Simple UI for user interaction

## Installation 📥

1. Clone the repository:
   ```bash
   git clone https://github.com/ad1lhasan/Will-You-Survive.git
   cd Will-You-Survive
   ```

2. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Ensure you have the trained model (`model.pkl`) in the project directory.

## Usage 🚀

1. Run the Flask app:
   ```bash
   python app.py
   ```

2. Open your browser and go to:
   ```
   http://127.0.0.1:5000/
   ```

3. Enter the passenger details and get the prediction on whether they would have survived.

## File Structure 📂
```
Will-You-Survive/
│── app.py              # Flask application
│── model.pkl           # Trained machine learning model
│── templates/
│   └── index.html      # Frontend HTML file
│── static/             # Static assets (CSS, JS, Images, etc.)
│── requirements.txt    # List of dependencies
│── README.md           # This file
```

## Requirements 📌
Make sure you have the following installed:
- Python 3.x
- Flask
- NumPy
- seaborn
- matplotlib
- scikit-learn

Install missing dependencies using:
```bash
pip install -r requirements.txt
```

## Contributing 🤝
Feel free to contribute! Fork the repository, create a new branch, and submit a pull request with your changes.

## License 📜
This project is licensed under the MIT License.

## Acknowledgments 🎉
- Inspired by Titanic survival prediction datasets.
- Built using Flask and a pre-trained machine learning model.

---
Happy coding! 🚢

