# SUS Survey Data Engineering - Pipelining, Cleaning, and Visualization

## Project Overview

This project focuses on analyzing and visualizing data from the **System Usability Scale (SUS)** survey of our capstone research system Vista. The primary goal is to process the survey data, clean it, and provide insightful visualizations that highlight the usability of a system based on participants' feedback.

Using Python and libraries like **Pandas**, **Matplotlib**, **Seaborn**, and **Jupyter Notebook**, I built an ETL pipeline for processing and cleaning the raw data, performed statistical analysis, and created both **participant-focused** and **question-focused** visualizations.

### Key Features:
- **Data Cleaning**: Handle missing or inconsistent data, ensuring the dataset is ready for analysis.
- **Statistical Analysis**: Conducted descriptive statistics such as calculating standard deviations and identifying trends in responses.
- **Visualization**: Generated heatmaps and bar plots to display the relationships between participants' responses and the usability scores of the system.

## What I Did

1. **Loading the Data**:
   - The data is stored in an `.xlsx` file containing responses from 50 participants. I used the **Pandas** library to read and load this data.
   
2. **Data Cleaning**: 
   - Removed unnecessary columns, handled missing data, and ensured proper formatting for further analysis.

3. **Statistical Analysis**:
   - Calculated **standard deviations** for each question to determine the spread of responses and better understand participant sentiment.
   
4. **Visualizations**:
   - I created two types of visualizations:
     - **Heatmap**: To observe correlations between questions, showing the relationship between different SUS questions.
     - **Bar Plots**: To provide a **participant-focused** view of their responses for better insights.

## How to Do This on Your Own

1. **Clone this repository**:
   ```bash
   git clone https://github.com/yourusername/your-repo.git

2. ### 2. Install Dependencies

- **Create a virtual environment**:
    ```bash
    python -m venv venv
    ```

- **Activate the virtual environment**:
    - On **Windows**:
        ```bash
        venv\Scripts\activate
        ```
    - On **Mac/Linux**:
        ```bash
        source venv/bin/activate
        ```

- **Install the necessary Python libraries**:
    ```bash
    pip install pandas matplotlib seaborn openpyxl
    ```

### 3. Run the Analysis

- Place your SUS data file in the correct path (`data/sus_results.xlsx`).
- Run the data processing code (`data_processing.py`), and you should see the processed output along with the visualizations in your Jupyter Notebook.

### 4. Customize

- You can replace the SUS data file with your own to apply the analysis to different datasets.

## Challenges Encountered

1. **Missing Data**:
    - The data provided by participants often contained missing or inconsistent entries, requiring a thorough cleaning process to handle the issues.

2. **Data Type Conversion**:
    - Some columns had mixed data types (like numbers and text), so I had to ensure correct formatting before performing any calculations.

3. **Visualization Challenges**:
    - Generating meaningful visualizations for this type of survey data was challenging, especially when interpreting the correlations and aggregating the data in a way that is visually clear and informative.

## Visualizations

### 1. **Heatmap of Correlations Between SUS Questions**
This heatmap visualizes the correlation between different SUS questions based on participants' responses. The closer to 1 or -1, the stronger the correlation.

![SUS-Response-Heatmap](https://github.com/user-attachments/assets/0a972f42-5d4d-47b3-b2ff-5ed600a1894c)

### 2. **Bar Plot for Standard Deviations Across Questions**
This bar plot shows the standard deviation for each SUS question, indicating how widely participants' answers vary for each question.

![Standard-Deviation-PerQ-Barplot](https://github.com/user-attachments/assets/d2e71338-7f90-49e7-bccd-c5ed00fd1f4f)

### 3. **Participant Responses by Question (Bar Plot)**
This plot visualizes how each participant responded to the different SUS questions. It's a participant-focused view that helps in understanding individual response trends.

![Participant-Responses-Heatmap](https://github.com/user-attachments/assets/f3854e38-5cdf-4e2d-b3b9-3dd82876fef4)

## My takeaway

This project showcases the entire pipeline of handling a real-world dataset from loading and cleaning data to performing analysis and creating visualizations.

By going through this process, I also learned the importance of effective data cleaning, handling edge cases, and choosing the right visualizations to represent complex data in an understandable manner.
