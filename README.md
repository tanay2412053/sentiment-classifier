# sentiment-classifier  

A simple sentiment analysis tool built with **Python, scikit-learn, and TF-IDF**.  
It classifies text reviews into **positive, negative, or neutral** sentiments.  


## 🚀 Features
- Preprocesses raw text using **TF-IDF Vectorization**  
- Trains a **Logistic Regression** model  
- Predicts sentiment of new text inputs  
- Easy to run from the command line  


## 📂 Project Structure
sentiment-classifier/
│── sentiment.py # Main script for sentiment analysis
│── requirements.txt # Dependencies
│── README.md # Documentation


## ⚙️ Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/sentiment-classifier.git
   cd sentiment-classifier


Create a virtual environment (recommended):
python3 -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows


#Install the dependencies:
pip install -r requirements.txt


▶️ Usage
Run the script with:
python sentiment.py


#Example output:
Accuracy: 0.90
Review: "Amazing movie with great storyline!" → Sentiment: Positive
Review: "Terrible film, waste of time." → Sentiment: Negative


🛠 Tech Stack
-Python
-scikit-learn
-pandas
-numpy












