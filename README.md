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
To empower YouTube content creators and marketers with actionable insights into their channels' performance, especially in comparison to related channels, I developed an **ETL pipeline** for analyzing and comparing YouTube channel performance. This involved:
+ **Data Extraction**: Collected data on three selected channels, including videos and comments, using the YouTube API.
+ **Data Transformation**: Cleaned and processed data with Pandas.
+ **Data Loading**: Stored the processed data in a MySQL database on AWS.
+ **Automation**: Managed the ETL workflow using Apache Airflow, Docker, and AWS.
+ **Data Visualization**: Created an interactive PowerBI report that provides insigths into channel performance, featuring key metrics and comparative analysis.

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
+ **Problem**:  Analyzing and comparing the performance of multiple YouTube channels is crucial for content creators and marketers. Most available tools focus on single-channel analytics, making it difficult to perform comparisons with similar YouTube channels.
+ **Project goal**: Empower content creators and marketers with insights into a YouTube channel's performance to enable informed decision-making and content optimization strategies by developing an automated ETL pipeline and providing insightful visualizations.

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- ETL PIPELINE -->
## 🔄 ETL Pipeline
Built using Apache Airflow to automate the extraction, transformation, and loading of data from multiple YouTube channels.
+ **Data Extraction**: Utilized the YouTube API to gather comprehensive data from three selected channels, including video metadata, view counts, likes, comments, and more.
+ **Data Transformation**: Implemented data manipulation and transformation techniques using Pandas to prepare the extracted data for analysis.
+ **Data Loading**: Stored the transformed data in a MySQL database hosted on an AWS RDS instance, ensuring persistent storage and facilitating easy access for comparative analysis.
+ **Automation**: Orchestrated the ETL workflow using Apache Airflow with Docker, hosted on an AWS EC2 t2.micro instance.

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- DATA VISUALIZATION -->
## 📊 Data Visualization
Created an interactive PowerBI report with multiple pages designed to offer in-depth insights into channel performance and audience engagement:

+ **Home**: Provides an overview with subscriber counts, video metrics, and area charts showing videos by month. Users can select time periods and compare channels side-by-side for a comprehensive analysis.
+ **Engagement**: Visualizes key engagement metrics such as views, likes, and comments. Includes per-video and per-1000-views averages, complemented by area charts tracking monthly comment trends.
+ **Top 5 Videos**: Highlights each channel's top 5 videos, with user-defined ranking criteria (views, likes, or comments), enabling a tailored exploration of high-performing content.

The report facilitates an interactive exploration of various metrics, allowing users to easily navigate through time periods and metrics to uncover patterns and trends in channel performance and audience behavior.

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
+ **Apache Airflow**: Tutorials by [coder2j](https://www.youtube.com/watch?v=z7xyNOF8tak&list=PLwFJcsJ61oujAqYpMp1kdUBcPG0sE0QMT) and [Data with Marc](https://www.youtube.com/watch?v=vEApEfa8HXk&list=PL79i7SgJCJ9hf7JgG3S-3lOpsk2QCpWkD).
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
