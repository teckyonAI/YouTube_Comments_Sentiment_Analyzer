# YouTube Sentiment Analyzer: Understand Audience Feedback

Dive deep into your YouTube audience's opinions and emotions with this powerful sentiment analysis tool. This project processes YouTube comments, classifies them into sentiment categories, and visualizes audience feedback, providing actionable insights to creators and analysts.

---

## Features

- **Sentiment Classification**: Automatically categorizes comments into positive, neutral, or negative sentiments using pre-trained models.
- **Preprocessing Pipeline**: Cleans and structures raw text data by removing noise, stop words, and special characters for accurate analysis.
- **Trained Model**: Leverages state-of-the-art machine learning techniques for high precision and recall in sentiment detection.
- **Interactive Dashboard**: Visualize sentiment distribution, trends over time, and individual comment analysis with user-friendly graphs and charts.
- **Batch Analysis**: Processes thousands of comments efficiently, providing summary statistics and detailed breakdowns.

---

## Tools and Libraries

The project utilizes the following technologies:
- **Python**: Core programming language.
- **NLTK & SpaCy**: For natural language processing and text preprocessing.
- **Scikit-learn**: For implementing machine learning models.
- **Matplotlib & Seaborn**: For creating interactive visualizations.
- **Flask**: To deploy the tool as a web-based application.
- **Pandas & NumPy**: For data manipulation and numerical operations.

---

## Dataset

The input dataset consists of YouTube comments, typically in a `.csv` format. An example file (`youtube-comments.csv`) is included in the repository.

### Dataset Fields:
- **Comment ID**: Unique identifier for each comment.
- **Comment Text**: The actual text content of the comment.
- **Timestamp**: Time the comment was posted (optional).
- **Predicted Sentiment**: Output sentiment label (positive, neutral, negative).

---

## Challenges Addressed

- **Unstructured Text**: Cleaned and preprocessed raw YouTube comments for meaningful analysis.
- **Multi-language Support**: Designed to handle multilingual comments with proper tokenization.
- **Scalability**: Optimized to analyze large datasets of comments without compromising speed or accuracy.
- **Visualization**: Simplified complex sentiment data into intuitive, actionable visuals.

---

## Results

The YouTube Sentiment Analyzer provides the following outcomes:
- **Sentiment Distribution**: Pie charts and bar graphs for sentiment breakdowns.
- **Trend Analysis**: Visualize sentiment changes over time or across different videos.
- **Keyword Insights**: Highlight frequently used words in positive, neutral, or negative comments.
- **Audience Engagement**: Understand how audience sentiment correlates with content themes.

---
## Installation

Follow these steps to set up the project locally:

1. Clone the repository:
   ```bash
   git clone https://github.com/teckyonAI/YouTube_Sentiment_Analyzer.git

2. Navigate to the project directory:
   ```bash
   cd YouTube_Sentiment_Analyzer

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt

4. Run the application:
    ```bash
    python app.py

---

## Usage

1. Provide a `.csv` file containing YouTube comments (`youtube-comments.csv` is included as an example).
2. The tool preprocesses the comments and predicts their sentiment.
3. Explore the results through visualizations and summary statistics.

---

## Deployment

This project is ready for deployment on platforms like Heroku. Use the included Procfile and setup.sh for easy deployment.

---

## Contribution

Contributions are welcome! Here's how you can contribute:
1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Submit a pull request with a detailed explanation of the changes.
