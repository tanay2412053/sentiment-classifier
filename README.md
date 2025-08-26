# sentiment-classifier  

A simple sentiment analysis tool built with **Python, scikit-learn, and TF-IDF**.  
A simple Python script that demonstrates how to perform sentiment analysis on movie reviews using machine learning.  
The model classifies reviews as **positive**, **negative**, or **neutral**. 


## ⚙️ How It Works
The script uses two components from the **scikit-learn** library:

- **TF-IDF Vectorizer**: Converts raw text into numerical features.  
- **Logistic Regression**: A classification algorithm trained to predict sentiment.



## 📂 Project Structure
sentiment-classifier/
│── sentiment.py # Main script for sentiment analysis
│── requirements.txt # Dependencies
│── README.md # Documentation


## ⚙️ Installation

1. Clone the repository:

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

Enter movie name: The Great Film
Enter your review for 'The Great Film': A truly fantastic and memorable experience.
Movie: The Great Film
Predicted Sentiment: Positive (score: 0.85)


🛠 Tech Stack
-Python
-scikit-learn
-pandas
-numpy


⚠️ Limitations-
Small Training Data: The model is trained on only five example sentences.
I have maded a Simple Model: For real-world accuracy, you’ll need larger datasets and more advanced models.
