# MetroTrafficPrediction
Big Data analytics project using Hadoop MapReduce and PySpark to classify and predict metro interstate traffic volume
Big Data Traffic Analytics

## Contents
- `mapper.py`: Python script for MapReduce mapper
- `reducer.py`: Python script for MapReduce reducer
- `traffic_volume_clean_full.csv`: Cleaned dataset used in the analysis
- PySpark notebook or code for ML model 
- Output screenshots and result files

## ML Models
- Logistic Regression (Classification)
- Linear Regression (Prediction)

## Tools Used
- Apache Hadoop (MapReduce via Streaming)
- Apache Spark (MLlib)
- Python (PySpark)

- ## How to Run
- Ensure Hadoop and Spark are set up in Docker
- Place `traffic_volume_clean_full.csv` in HDFS
- Run `mapper.py` and `reducer.py` using Hadoop Streaming
- Use PySpark for ML pipeline (classification and prediction)


## Screenshots
See `/screenshots` folder for MapReduce output, Spark metrics, and model evaluations.
## Dataset Source

Hogue, J. (2019). *Metro Interstate Traffic Volume* [Dataset]. UCI Machine Learning Repository. https://doi.org/10.24432/C5X60B


## Author
**Rajveer Kaur**  
[GitHub Profile](https://github.com/RajveerKR)
