<!-- anchor tag for back-to-top links -->
<a name="readme-top"></a>

<!-- PROJECT LOGO -->
<div align="center">
  <a href="https://github.com/JensBender/youtube-channel-analytics">
    <img src="images/logo1.jpg" width=15%>
  </a>
  <a href="https://github.com/JensBender/youtube-channel-analytics">
    <img src="images/logo2.png" width=80%>
  </a>
  <p>
    <br />
    Provide insights about a YouTube channel’s performance.
    <br />
  </p>
</div> 

---

<!-- TABLE OF CONTENTS -->
## 📋 Table of Contents
<ol>
  <li>
    <a href="#-summary">Summary</a>
    <ul>
      <li><a href="#️-built-with">Built With</a></li>
    </ul>
  </li>
  <li>
    <a href="#-motivation">Motivation</a>
  </li>
  <li>
    <a href="#-etl-pipeline">ETL Pipeline</a>
  </li>
  <li>
    <a href="#-data-visualization">Data Visualization</a>
  </li>
  <li>
    <a href="#️-license">License</a>
  </li>
  <li>
    <a href="#️-credits">Credits</a>
  </li>
</ol>


<!-- SUMMARY -->
## 🎯 Summary
Built an **ETL pipeline** to analyze and compare YouTube channel performance, involving:
+ **Extraction**: Collected data on three selected channels, including videos and comments, using the YouTube API.
+ **Transformation**: Cleaned and processed data with Pandas.
+ **Loading**: Stored data in a MySQL database on AWS.
+ **Automation**: Managed the entire ETL workflow using Apache Airflow, Docker, and AWS.
+ **Visualization**: Created a PowerBI report to compare channel performance on key metrics.

### 🛠️ Built With
* [![Python][Python-badge]][Python-url]
* [![Pandas][Pandas-badge]][Pandas-url]
* [![MySQL][MySQL-badge]][MySQL-url]
* [![Airflow][Airflow-badge]][Airflow-url]
* [![Docker][Docker-badge]][Docker-url]
* [![AWS][AWS-badge]][AWS-url]
* [![Power BI][PowerBI-badge]][PowerBI-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- MOTIVATION -->
## 💡 Motivation
+ **Problem**: Analyzing the performance of a YouTube channel is crucial for content creators and marketers alike. However, manual data extraction and analysis can be time-consuming and prone to errors.
+ **Project goal**: Empower content creators and marketers with insights into a YouTube channel's performance to enable informed decision-making and content optimization strategies by developing an automated ETL pipeline and providing insightful visualizations.

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- ETL PIPELINE -->
## 🔄 ETL Pipeline
Built using Apache Airflow to automate the extraction, transformation, and loading of YouTube channel data.
+ **Data Extraction**: Utilized the YouTube API to extract comprehensive data about the channel, including video metadata, view counts, likes, comments, etc.
+ **Data Transformation**: Implemented data manipulation and transformation techniques using NumPy and Pandas to prepare the extracted data for analysis.
+ **Data Loading**: Stored the transformed data in a MySQL database hosted on AWS, ensuring persistent storage and easy accessibility for analysis.

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- DATA VISUALIZATION -->
## 📊 Data Visualization
Implemented a **word cloud** to visualize the main topics of the YouTube channel by identifying frequently occurring words or phrases in video titles or descriptions.

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- LICENSE -->
## ©️ License
This project is licensed under the [MIT License](LICENSE).

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- CREDITS -->
## 👏 Credits
This project was made possible with the help of the following resources and tutorials:
+ **Project logo**: Created using AI technology by [Microsoft Copilot](https://play.google.com/store/apps/details?id=com.microsoft.copilot&pcampaignid=web_share).
+ **YouTube API**: Tutorials by [Corey Schafer](https://www.youtube.com/watch?v=th5_9woFJmk) and [Thu Vu data analytics](https://www.youtube.com/watch?v=D56_Cx36oGY).
+ **Power BI**: Tutorials by [BI Elite](https://www.youtube.com/@BIElite) and [How to Power BI](https://www.youtube.com/@HowtoPowerBI).
+ **Power BI icons**: Attributions for icons used in the report.
  + <a href="https://www.flaticon.com/free-icons/eye" title="eye icons">Eye icons created by Kiranshastry - Flaticon</a>
  + <a href="https://www.flaticon.com/free-icons/like" title="like icons">Like icons created by logisstudio - Flaticon</a>
  + <a href="https://www.flaticon.com/free-icons/comment" title="comment icons">Comment icons created by Freepik - Flaticon</a>
  + <a href="https://www.flaticon.com/free-icons/youtube" title="youtube icons">Youtube icons created by Freepik - Flaticon</a>
  + <a href="https://www.flaticon.com/free-icons/subscribe" title="subscribe icons">Subscribe icons created by Komar Dews - Flaticon</a>
  + <a href="https://www.flaticon.com/free-icons/information" title="information icons">Information icons created by Freepik - Flaticon</a>

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- MARKDOWN LINKS -->
[Python-badge]: https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54
[Python-url]: https://www.python.org/
[Pandas-badge]: https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white
[Pandas-url]: https://pandas.pydata.org/
[MySQL-badge]: https://img.shields.io/badge/mysql-4479A1.svg?style=for-the-badge&logo=mysql&logoColor=white 
[MySQL-url]: https://www.mysql.com/
[Airflow-badge]: https://img.shields.io/badge/Apache%20Airflow-017CEE?style=for-the-badge&logo=Apache%20Airflow&logoColor=white
[Airflow-url]: https://airflow.apache.org/
[Docker-badge]: https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white
[Docker-url]: https://www.docker.com/
[AWS-badge]: https://img.shields.io/badge/AWS-%23FF9900.svg?style=for-the-badge&logo=amazon-aws&logoColor=white
[AWS-url]: https://aws.amazon.com/
[PowerBI-badge]: https://img.shields.io/badge/power_bi-F2C811?style=for-the-badge&logo=powerbi&logoColor=black
[PowerBI-url]: https://www.microsoft.com/en-us/power-platform/products/power-bi
