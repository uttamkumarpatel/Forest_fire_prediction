# 🌲 Forest Fire Prediction 🔥

## 📌 Overview
Forest fires can cause severe environmental and economic damage. This project leverages **machine learning** to predict the likelihood of forest fires based on various features such as temperature, humidity, wind speed, and more. The system consists of **data processing, model training, and a web-based application** that allows users to visualize predictions interactively. 

## 📁 Project Structure
```
forestfire/
├── application.py       # 🎯 Main application script that runs the web app
├── datasets/            # 📊 Contains dataset files for training & testing
├── models/              # 🤖 Pre-trained models for fire prediction
├── notebooks/           # 📔 Jupyter notebooks for experimentation & EDA
├── templates/           # 🎨 HTML templates for the web-based UI
├── requirements.txt     # 📌 Project dependencies & required libraries
└── .git/                # 🛠️ Git repository metadata
```

## 🚀 Installation
To get started with this project, follow these steps:

1️⃣ Clone the repository:
   ```sh
   git clone <repository-url>
   ```
2️⃣ Navigate to the project directory:
   ```sh
   cd forestfire
   ```
3️⃣ Install the required dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## 🎯 Usage
Once the setup is complete, you can start using the application by running:
   ```sh
   python application.py
   ```
This will start a **Flask-based web application** that you can access in your browser at:
   ```
   http://127.0.0.1:5000/
   ```

## 📊 Dataset Information
The dataset used in this project is located in the `datasets/` folder. It contains crucial environmental parameters affecting fire outbreaks, including:
- 🌡 **Temperature**: Higher temperatures increase fire risk.
- 💧 **Humidity**: Lower humidity levels can lead to drier conditions, increasing flammability.
- 🌬 **Wind Speed**: Strong winds can rapidly spread fires.
- 🌲 **Vegetation Index**: More vegetation can fuel fires.

## 🤖 Machine Learning Model
The trained models are stored in the `models/` directory and are used for real-time predictions. The model is built using **scikit-learn** and other machine learning libraries, employing techniques such as:
- **Data Preprocessing** 📊
- **Feature Engineering** 🛠️
- **Hyperparameter Tuning** ⚙️
- **Model Evaluation & Optimization** 📈

## 🌍 Web Application
This project includes an interactive **web application** where users can:
- 🌟 Input environmental conditions
- 🔥 Get a prediction on the likelihood of a fire occurring
- 📊 Visualize model performance and accuracy

## 🌐 Live Demo
🚀 The application is live at: [Click Here](https://forest-fire-prediction-kdk9.onrender.com)

## 🏗️ Contribution
Contributions are always welcome! If you’d like to improve this project:
- Fork the repository 🍴
- Make your changes ✏️
- Submit a **Pull Request** ✅

