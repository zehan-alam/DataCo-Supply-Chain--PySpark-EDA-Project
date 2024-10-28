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


# Business Analysis Report

## 1. Operational Efficiency

### How does shipping mode affect delivery times and customer satisfaction? Which shipping modes are most reliable?

<div align="center">
    <img src="Images/Shipping_Mode_by_Delivary_Time.png" alt="Figure 1.1: Delivery Times by Shipping Mode">
    <br>
    <b>Figure 1.1:</b> Delivery Times by Shipping Mode
    <br>
</div>

From **Figure 1.1**, we observe the following trends:
- **Same Day Delivery**: Although expected to deliver in 0 days, it consistently takes at least 1 day.
- **First Class Delivery**: Expected delivery in 1 day but consistently takes 2 days minimum.
- **Second Class Delivery**: Occasionally on schedule, but averages 4 days (twice the expected 2 days).
- **Standard Class**: The most reliable mode, with delivery times aligning closely to expectations.

<div align="center">
    <img src="Images/Delivery_Status_Distribution_by_Shipping_Mode.png" alt="Figure 1.2: Delivery Status Distribution by Shipping Mode">
    <br>
    <b>Figure 1.2:</b> Delivery Status Distribution by Shipping Mode
    <br>
</div>

In **Figure 1.2**:
- **Standard Time** and **Same Day Shipping**: Both deliver on time or early around 50% of the time.
- **Second Class**: Achieves on-time delivery for only 20% of orders.
- **First Class**: Records no on-time deliveries.
- Each mode experiences about 5% canceled shipments.

**Conclusion**: **First Class** shipping requires improvements in speed or reconsideration. Standard and Second Class also warrant optimizations to improve on-time rates.

---

### What is the average delay in delivery time, and how often do orders arrive late?

<div align="center">
    <img src="Images/Late_Delivery_Distribution.png" alt="Figure 1.3: Late Delivery Distribution">
    <br>
    <b>Figure 1.3:</b> Late Delivery Distribution
    <br>
</div>

On average, orders are delayed by **1.62 days**, affecting **0.57%** of all shipments. **Figure 1.3** reveals that most late deliveries are delayed by only 1 day, but **40%** of delayed shipments take 2 or more days to arrive.

---

### What regions have the highest late delivery rates? What is the relationship to their distance?

<div align="center">
    <img src="Images/Order_Distance_Distribution_by_Delivery.png" alt="Figure 1.4: Order Distance Distribution by Delivery Status">
    <br>
    <b>Figure 1.4:</b> Order Distance Distribution by Delivery Status
    <br>
</div>

Regions with the highest late delivery rates include **República Democrática del Congo** (62% of orders late), followed by Nicaragua, Egipto, Austria, Alemania, India, El Salvador, Filipinas, Indonesia, and Francia, each with more than 58% of orders arriving late.

In **Figure 1.4**, we see that distance has minimal impact on delivery timeliness; the distribution of distances for late versus on-time deliveries is nearly identical.

## 2. Financial Analysis:

### What is the average profit per order?
The average profit per order is **$21.97**, indicating that while some orders result in significant losses, the overall performance remains positive. The maximum profit achieved was **$911.80**, demonstrating the potential for high returns, whereas the maximum loss reached **$-4274.98**, highlighting the risk of unprofitable orders. 

The profits are concentrated, and a more granular look shows that approximately 25% of orders generate profits of **$6.75 or less**, while the median profit stands at **$30.86**, reflecting that half of the orders exceed this amount. A 75% percentile profit of **$63.16** indicates that a quarter of orders yield even higher returns.

The Order Item Profit Ratio has a mean of **0.1206**, suggesting that, on average, orders yield a profit margin of about **12%**. The standard deviation of **0.4668** implies considerable variation, with some orders experiencing losses up to **-2.75** and others yielding a maximum profit ratio of **0.50**. The 25% percentile profit ratio of **0.07** suggests that a significant portion of orders has a low profit margin, while a median profit ratio of **0.27** shows that half of the orders are more profitable.

### What is the return on discounts provided to customers?
For customers who received discounts, the return on discount (calculated as Order Profit Per Order divided by Order Item Discount) averages **2.23**, meaning for every dollar discounted, the company earns over **$2** in profit. The standard deviation of **14.13** indicates variability in return rates, with a minimum return of **-272.24** showcasing instances where discounts led to substantial losses. Conversely, the maximum return of **49.82** illustrates the potential for significant profit from discounted sales.

The approximate median return of **1.84** and the 25% and 75% percentiles of **0.46** and **4.47**, respectively, reinforce that while many discounted orders yield a good return, some yield minimal returns.

### Which product categories generate the most revenue and profit?
From the figure below, we can see that the **Fishing** category has the highest revenue and profit, generating almost **$7,000,000** in revenue. The categories with good total revenue and profit include: **Cleats**, **Camping & Hiking**, **Cardio Equipment**, **Women's Apparel**, **Water Sports**, **Men's Footwear**, and **Indoor/Outdoor Games**.

![Revenue by Category](Images/Revenue_by_Category.png)
*Figure 2.1: Revenue by Category*

### How do discounts affect overall profitability?

|                          | Discounted Products      | Regular Price Products  |
|--------------------------|--------------------------|--------------------------|
| Total Profit             | $3,699,490.57            | $267,412.40              |
| Average Profit           | $21.70                   | $26.67                   |
| Average Profit Ratio     | 0.1202                   | 0.1275                   |

It seems like for regular products, the profit was greater by a huge margin than for discounted products. However, the average profit ratio is almost similar, indicating that discounted and regular products have similar profit margins.

## 3. Customer and Market Analysis

### How do customer segments differ in purchasing behavior?
![Sales by Customer Segment](Images/Sales_by_Customer_Segment.png)
*Figure 3.1: Sales by Customer Segment*

![Profit by Customer Segment](Images/Profit_by_Customer_Segment.png)
*Figure 3.2: Profit by Customer Segment*

From Figures 3.1 and 3.2, we observe that both total revenue and profit are predominantly driven by **Consumers**, who contribute to half of the sales. The remaining revenue and profit are divided between **Corporate** customers (30%) and **Home Office** customers (20%).

### Which markets perform the best in terms of sales and profit?
![Sales by Region](Images/Sales_By_Region.png)
*Figure 3.3: Sales by Region*

![Profit by Region](Images/Profit_by_Region.png)
*Figure 3.4: Profit by Region*

In Figures 3.3 and 3.4, it’s clear that **Western Europe** and **Central America** are the top-performing markets, each generating approximately **$5.8 million** in revenue. **South America** follows with nearly **$3 million** in revenue, while all other regions report revenue below **$2.2 million**.

### What regions have the highest customer demand for certain product categories?
**Western Europe**, **Central America**, and **South America** show strong customer demand for **Cleats**, **Men’s Footwear**, and **Women’s Apparel**. Similar preferences are observed in other regions, though at varying levels of demand.

## 4. Fraud and Risk Analysis

### Are there patterns in suspected fraudulent orders?
We calculated the ratio of suspected fraud cases across different regions, countries, and product categories to identify patterns and areas of concern.

![Suspected Fraud by Region](Images/Suspected_Fraud_by_Region.png)
*Figure 4.1: Suspected Fraud by Region*

From Figure 4.1, fraud ratios appear highest in **Canada**, the **Western USA**, and **Southern Africa**. However, these regions don’t exhibit significantly higher fraud rates than others, suggesting that suspected fraud is somewhat evenly distributed.

![Suspected Fraud by Country](Images/Suspected_Fraud_by_Country.png)
*Figure 4.2: Suspected Fraud by Country*

Figure 4.2 reveals that **Ethiopia** has a markedly high fraud ratio, with **25%** of its orders flagged as suspected. Other countries with higher fraud rates include **Guinea**, **Hong Kong**, **Syria**, and **Martinique**, each with suspected fraud ratios exceeding **10%**. Heightened fraud monitoring is recommended in these countries.

![Suspected Fraud by Category](Images/Suspected_Fraud_by_Category.png)
*Figure 4.3: Suspected Fraud by Category*

As shown in Figure 4.3, the **Basketball** and **Women’s Golf Club** categories experience a notably high level of suspected fraud. Orders within these categories should be carefully reviewed to prevent fraudulent transactions.
