<!-- anchor tag for back-to-top links -->
<a name="readme-top"></a>

<!-- PROJECT LOGO -->
<div align="center">
  <a href="https://github.com/JensBender/youtube-channel-analytics">
    <img src="images/logo.png" width=80%>
  </a>
  <p>
    <br />
    Provide insights about a YouTube channel’s performance and subscribers.
    <br />
  </p>
</div> 

---

<!-- TABLE OF CONTENTS -->
## Table of Contents
<ol>
  <li>
    <a href="#summary">Summary</a>
    <ul>
      <li><a href="#built-with">Built With</a></li>
    </ul>
  </li>
  <li>
    <a href="#motivation">Motivation</a>
  </li>
  <li>
    <a href="#etl-pipeline">ETL Pipeline</a>
  </li>
  <li>
    <a href="#data-visualization">Data Visualization</a>
  </li>
</ol>


<!-- SUMMARY -->
## Summary
+ Built an ETL (Extract, Transform, Load) pipeline leveraging Apache Airflow, which involved:
  + Extracting YouTube channel data through the YouTube API
  + Transforming data by leveraging NumPy and Pandas
  + Loading the processed data into a MySQL database hosted on AWS
+ Showcased the main topics of the channel using a word cloud
+ Visualized the geographic distribution of subscribers on an interactive world map using Folium

### Built With
* [![Python][Python-badge]][Python-url]
* [![NumPy][NumPy-badge]][NumPy-url]
* [![Pandas][Pandas-badge]][Pandas-url]
* [![MySQL][MySQL-badge]][MySQL-url]
* [![AWS][AWS-badge]][AWS-url]
* [![Jupyter Notebook][JupyterNotebook-badge]][JupyterNotebook-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- MOTIVATION -->
## Motivation
+ **Problem**: Analyzing the performance and audience demographics of a YouTube channel is crucial for content creators and marketers alike. However, manual data extraction and analysis can be time-consuming and prone to errors.
+ **Project goal**: Empower content creators and marketers with insights into a YouTube channel's performance and audience demographics to enable informed decision-making and content optimization strategies by developing an automated ETL pipeline and providing insightful visualizations.

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- ETL PIPELINE -->
## ETL Pipeline
Built using Apache Airflow to automate the extraction, transformation, and loading of YouTube channel data.
+ **Data Extraction**: Utilized the YouTube API to extract comprehensive data about the channel, including video metadata, view counts, likes, comments, etc.
+ **Data Transformation**: Implemented data manipulation and transformation techniques using NumPy and Pandas to prepare the extracted data for analysis.
+ **Data Loading**: Stored the transformed data in a MySQL database hosted on AWS, ensuring persistent storage and easy accessibility for analysis.

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- DATA VISUALIZATION -->
## Data Visualization
Implemented two visualization components:
+ **Word Cloud**: Visualized the main topics of the YouTube channel by identifying frequently occurring words or phrases in video titles, descriptions, or tags.
+ **Interactive World Map**: Presented the subscribers' country of origin on an interactive world map using Folium, allowing for geographical analysis of the channel's audience.

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- MARKDOWN LINKS -->
[Python-badge]: https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54
[Python-url]: https://www.python.org/
[NumPy-badge]: https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white
[NumPy-url]: https://numpy.org/
[Pandas-badge]: https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white
[Pandas-url]: https://pandas.pydata.org/
[MySQL-badge]: https://img.shields.io/badge/mysql-4479A1.svg?style=for-the-badge&logo=mysql&logoColor=white 
[MySQL-url]: https://www.mysql.com/
[AWS-badge]: https://img.shields.io/badge/AWS-%23FF9900.svg?style=for-the-badge&logo=amazon-aws&logoColor=white
[AWS-url]: https://aws.amazon.com/
[JupyterNotebook-badge]: https://img.shields.io/badge/jupyter-%23FA0F00.svg?style=for-the-badge&logo=jupyter&logoColor=white
[JupyterNotebook-url]: https://jupyter.org/
