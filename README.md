# DataCo Supply Chain - PySpark EDA Project on Databricks Environment

## Important Links
- **Databricks Notebook**: [Access Here](https://databricks-prod-cloudfront.cloud.databricks.com/public/4027ec902e239c93eaaa8714f173bcfc/649705917837865/179433283878260/8453874180793124/latest.html)
- **Dataset**: [Kaggle - DataCo Supply Chain](https://www.kaggle.com/datasets/shashwatwork/dataco-smart-supply-chain-for-big-data-analysis)

## Project Description
DataCo Global is a multinational company specializing in supply chain management, utilizing data-driven insights to optimize provisioning, production, sales, and distribution processes. In this project, we analyze a dataset from DataCo’s supply chain operations to evaluate performance across key metrics. The analysis was conducted using PySpark in Databricks, where we performed end-to-end data processing and visualization.

This project aims to identify key performance indicators (KPIs) and address essential business questions to improve operational efficiency, enhance customer satisfaction, and optimize financial performance through business analytics techniques.

## Dataset Description
The dataset consists of multiple CSV files:
- **Primary Dataset** (`DataCoSupplyChainDataset.csv`): Contains 53 columns and 180,519 records detailing various aspects of the supply chain, including order details, customer information, shipping, and financial data.
- **Column Description File** (`DescriptionDataCoSupplyChain.csv`): Provides detailed descriptions of each column in the primary dataset.
- **Access Logs** (`tokenized_access_logs.csv`): Contains 469,977 records across 8 columns, covering user access logs with fields such as IP address, visited URLs, and timestamps. These logs span from September 2017 to February 2018.
- **Order Cities Geolocation** (`order_city_geolocation.csv`): A supplementary dataset generated using `coordinate_generator.py`, which includes the geographic coordinates of various order cities. This data was utilized to calculate the distance between seller and buyer locations, enabling further analysis on delivery efficiency and logistics.
