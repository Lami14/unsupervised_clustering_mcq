# Mall Customers Clustering Analysis

## Project Overview
This project performs customer segmentation using **K-Means** and **Hierarchical Clustering**.  
The goal is to group customers based on their **Annual Income** and **Spending Score**, which can help in **targeted marketing** and understanding customer behavior.

## Dataset
The dataset contains:

- CustomerID
- Gender
- Age
- Annual_Income_(k$)
- Spending_Score (1-50)

Source: [ExploreAI Public Dataset](https://raw.githubusercontent.com/Explore-AI/Public-Data/master/Data/unsupervised_sprint/mall_customers.csv)

## Methodology
1. **Data Cleaning & Preprocessing**
2. **Exploratory Data Analysis (EDA)**
3. **Scaling features**
4. **K-Means Clustering**
5. **Elbow Method for Optimal K**
6. **Silhouette Score Evaluation**
7. **Hierarchical Clustering**
8. **Cluster Characterization**

## Results
- Elbow Plot: ![elbow_plot](results/elbow_plot.png)
- Silhouette Analysis: ![silhouette_plot](results/silhouette_plot.png)
- Dendrogram: ![dendrogram](results/dendrogram.png)
- Cluster Scatter Plot: ![cluster_scatter](results/cluster_scatter.png)

## Usage
1. Clone the repo
```bash
git clone https://github.com/Lami14/unsupervised_clustering_mcq.git
