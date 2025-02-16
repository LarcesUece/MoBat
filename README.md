# MoBat

## Proposal Summary

In response to the escalating cyber threats and the critical need for advanced solutions to safeguard data integrity and confidentiality, we propose the implementation of MoBAt (Monitoramento e Analise de Dados de Bases de Ameacas). MoBAt serves as a Threat Intelligence tool, designed to automatically collect and analyze data from various threat databases including VirusTotal, AbuseIPDB, Shodan, IBM X-Force, and AlienVault. The primary objective of MoBAt is to empower companies and institutions to stay updated on emerging threats by providing valuable indicators regarding suspicious IPs and domains. By automating the process of threat intelligence, MoBAt enhances efficiency, scalability, and response time, reducing the burden on cybersecurity teams. The architecture of MoBAt leverages cutting-edge technologies such as FastAPI for API construction, Seaborn for data visualization, Scikit-learn for feature selection and machine learning, and Docker containers for infrastructure deployment. Additionally, it utilizes MongoDB for data storage, Nginx for handling HTTP requests, and Celery for asynchronous task processing. Through extensive performance analysis, MoBAt has demonstrated its efficacy in handling large volumes of data, executing requests multiple times per day, and generating actionable insights for cybersecurity professionals. It addresses the challenges posed by discrepancies among threat databases, providing a comprehensive and contextualized view of IP reputation and behavior. MoBAt offers a range of functionalities including behavior graphs, feature mapping, clustering, feature selection, machine learning model evaluation, and visualization of IP reputation by country. These features enable rapid identification of suspicious activities, visualization of trends over time, and informed decision-making to enhance overall cybersecurity posture. In summary, MoBAt represents a vital tool in the arsenal of cybersecurity defenses, offering automated threat intelligence capabilities to safeguard against evolving cyber threats and ensure the protection of critical data assets.

## Description Project

The MoBAt project focuses on developing a comprehensive tool for monitoring IP addresses and analyzing their behavior across various online platforms. The goal is to provide users with a detailed understanding of IP characteristics from sources like AbuseIPDB, IBMXForce, VirusTotal, AlienVault, and Shodan. The tool processes JSON data, converts it to CSV format, and performs in-depth analysis using graphical representations, machine learning techniques, and feature selection. The ultimate aim is to enhance threat monitoring capabilities and provide actionable insights for cybersecurity professionals and researchers.


## Technologies used:

Python 3.12 - An open-source programming language known for its simplicity and versatility.
Pandas - A powerful data manipulation and analysis library for Python.
NumPy - A fundamental package for scientific computing with Python.
Matplotlib - A comprehensive library for creating static, animated, and interactive visualizations in Python.
Scikit-learn - A simple and efficient tool for data mining and data analysis.
Seaborn - A Python visualization library based on matplotlib that provides a high-level interface for drawing attractive and informative statistical graphics.
Tkinter - Python's standard GUI (Graphical User Interface) package.
Geopandas - A Python library for working with geospatial data.
Pytz - A Python library for working with time zones.
JSON - A lightweight data interchange format.
Regular expressions (re) - A module for working with regular expressions in Python.
Geopandas - A Python library for working with geospatial data.
Pycountry - A Python package to access ISO databases.
Time - A Python module providing various time-related functions.
KMeans - A clustering algorithm available in scikit-learn.
VarianceThreshold, SelectKBest, f_classif, f_regression, mutual_info_regression - Feature selection techniques available in scikit-learn.
GradientBoostingRegressor, RandomForestRegressor, ExtraTreesRegressor, Lasso, LinearRegression, KNeighborsRegressor - Machine learning models available in scikit-learn.
Mean_squared_error - A metric for evaluating the performance of regression models in scikit-learn.

Participantes

## Coordenador do projeto:

Rafael Lopes Gomes: http://lattes.cnpq.br/5212299313885086

## Back-end e Data Analyst:
Yago Melo da Costa

Currículo lattes: http://lattes.cnpq.br/0381069814979157

Davi Oliveira

Currículo lattes: http://lattes.cnpq.br/6275027161080881

Ramon Araújo

Currículo lattes: http://lattes.cnpq.br/4482457290815759

Lyedson Silva

Currículo lattes: http://lattes.cnpq.br/6321492413240258

Francisco Nobre

Currículo lattes:  http://lattes.cnpq.br/8242344331454843

