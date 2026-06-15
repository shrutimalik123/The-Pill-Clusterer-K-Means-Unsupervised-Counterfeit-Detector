# 🕵️ The Pill Clusterer: K-Means Unsupervised Counterfeit Detector

An interactive Unsupervised Learning simulation designed to teach **K-Means Clustering**, **Centroid Optimization**, and **Iterative Spatial Convergence** from scratch. You play as a Forensic Pharmaceutical Chemist analyzing intercepted border shipments without past data labels ($y$), letting the algorithm naturally isolate hidden molecular patterns to separate genuine medication from high-end counterfeit copies.

## 🎓 Learning Objectives

This project focuses on teaching:
* **Unsupervised Learning:** Exploring a class of machine learning where models find hidden structural relationships within unlabeled datasets without historical correction vectors.
* **K-Means Clustering:** A foundational partitioning algorithm that groups multi-dimensional coordinate fields into $K$ distinct geometric boundaries.
* **Centroid Management:** Setting up structural gravity centers that shift to represent the localized mathematical mean of their assigned members.
* **Iterative Convergence:** Simulating the algorithmic feedback loop where repeating step assignments and re-centering matrices optimize data cluster tight-fitting.

---

## ✨ Features

* **Forensic Regulatory Narrative:** Translates abstract space clustering mechanics into an interactive chemical tracking and fraud-detection pipeline.
* **Mathematical Similarity Analytics:** Traces and outputs the exact continuous Euclidean distances separating unlabelled sample vectors from competing gravity centers.
* **Autonomous Trend Recognition:** Automatically judges group properties at execution time to label clusters based on resulting mass-to-dissolution ratios.
* **Native Codebase Design:** Built purely on standard Python loops and primitive variables, completing geometric cluster updates without using numerical libraries or framework wrappers.

---

## 🚀 How to Run the Game

### 1. Prerequisites
You only need **Python 3** installed.

### 2. Setup and Execution
1.  **Clone the Repo:**
    ```bash
    git clone [https://github.com/YOUR_USERNAME/pill-clusterer-kmeans.git](https://github.com/YOUR_USERNAME/pill-clusterer-kmeans.git)
    cd pill-clusterer-kmeans
    ```
2.  **Save the Code:** Save the provided script as `counterfeit_clusterer.py`.
3.  **Run the Script:**
    ```bash
    python counterfeit_clusterer.py
    ```

### 3. Gameplay Instructions
1.  **Review Unlabeled Scanner Logs:** Examine raw continuous measurements mapping Active Ingredient Mass (mg) and Dissolution Rates (seconds) with zero classification tags.
2.  **Inspect Initial Centroids:** Track the initial random coordinates seeded for Centroid 0 and Centroid 1 across your material graph.
3.  **Run Spatial Distance Assignment:** Watch the script measure the geometric distance of each unlabelled data point to find its closest gravity center.
4.  **Observe Centroid Adjustments:** Study how the centroids automatically recalculate their coordinates using localized class averages to expose illicit chemical variations.

---

## 🧠 Code Structure Highlights

### Distance Map Metric Matching
The program runs row-by-row matrix queries to evaluate straight-line coordinates separating fresh data arrays from structural centroid points.

```python
# Euclidean Distance Calculation to Centroid Coordinates
dist_to_c0 = math.sqrt((s[0] - centroid_0[0])**2 + (s[1] - centroid_0[1])**2)
dist_to_c1 = math.sqrt((s[0] - centroid_1[0])**2 + (s[1] - centroid_1[1])**2)

