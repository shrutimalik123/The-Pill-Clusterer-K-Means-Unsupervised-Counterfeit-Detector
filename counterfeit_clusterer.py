import math

def kmeans_pharmacy_game():
    # 1. Scenario: Forensic Pharmaceutical Border Analytics
    print("--- 🕵️ THE PILL CLUSTERER: K-MEANS FRAUD DETECTOR 🕵️ ---")
    print("Mission: Group unlabelled pill batches to isolate illicit counterfeit rings.")
    print("Goal: Partition continuous chemical metrics into distinct, optimized clusters.")

    # 2. Raw Intercepted Sample Matrix (Unlabelled Continuous Profiles)
    # Features: [Active Ingredient Mass (mg), Dissolution Rate (sec)]
    # Note: There are no target labels here! This is Unsupervised Learning.
    samples = [
        [48.0, 120.0],  # Sample A
        [51.0, 115.0],  # Sample B
        [49.0, 122.0],  # Sample C
        [22.0, 310.0],  # Sample D
        [25.0, 295.0],  # Sample E
    ]

    print("\n--- 🖥️ RAW LABORATORY TELEMETRY (UNLABELLED SAMPLES) ---")
    for idx, s in enumerate(samples):
        print(f"Pill Box {idx+1}: Active Mass = {s[0]} mg | Dissolution Rate = {s[1]} seconds")

    # 3. Algorithm Initialization: Setting up K Centroids
    # We suspect two distinct sources (Genuine vs. Counterfeit), so we set K = 2
    k = 2
    print(f"\n--- STEP 1: INITIALIZE STRUCTURAL CLUSTER CENTROIDS (K = {k}) ---")
    print("Centroids act as the mathematical 'gravity centers' for each discovered group.")
    
    # Manually seeding initial coordinates for Centroid 0 and Centroid 1
    centroid_0 = [30.0, 200.0]
    centroid_1 = [45.0, 150.0]
    
    print(f"Initial Position Centroid 0: Mass={centroid_0[0]}, Dissolution={centroid_0[1]}")
    print(f"Initial Position Centroid 1: Mass={centroid_1[0]}, Dissolution={centroid_1[1]}")

    # 4. Iteration Phase: Assigning Samples to the Nearest Centroid
    print("\n--- 🔄 ITERATION 1: COMPUTING EUCLIDEAN DISTANCE MAPS ---")
    
    cluster_0_points = []
    cluster_1_points = []

    for idx, s in enumerate(samples):
        # Calculate straight-line Euclidean distance to Centroid 0
        dist_to_c0 = math.sqrt((s[0] - centroid_0[0])**2 + (s[1] - centroid_0[1])**2)
        # Calculate straight-line Euclidean distance to Centroid 1
        dist_to_c1 = math.sqrt((s[0] - centroid_1[0])**2 + (s[1] - centroid_1[1])**2)
        
        print(f"Pill Box {idx+1} -> Distance to C0: {dist_to_c0:.1f} | Distance to C1: {dist_to_c1:.1f}")
        
        # Assignment step: Place point into the cluster of the closest centroid
        if dist_to_c0 < dist_to_c1:
            cluster_0_points.append(s)
            print(f"   👉 Assigned to Cluster 0")
        else:
            cluster_1_points.append(s)
            print(f"   👉 Assigned to Cluster 1")

    # 5. Optimization Step: Re-computing the New Centroids (The Mean)
    print("\n--- 📊 STEP 2: RE-CENTERING THE CENTROIDS (MEAN AGGREGATION) ---")
    print("The centroids shift to the exact geometric center of their assigned members.")

    if cluster_0_points:
        new_c0_mass = sum(p[0] for p in cluster_0_points) / len(cluster_0_points)
        new_c0_dissolve = sum(p[1] for p in cluster_0_points) / len(cluster_0_points)
        centroid_0 = [new_c0_mass, new_c0_dissolve]

    if cluster_1_points:
        new_c1_mass = sum(p[0] for p in cluster_1_points) / len(cluster_1_points)
        new_c1_dissolve = sum(p[1] for p in cluster_1_points) / len(cluster_1_points)
        centroid_1 = [new_c1_mass, new_c1_dissolve]

    print(f"Optimized Position Centroid 0: Mass={centroid_0[0]:.1f}, Dissolution={centroid_0[1]:.1f}")
    print(f"Optimized Position Centroid 1: Mass={centroid_1[0]:.1f}, Dissolution={centroid_1[1]:.1f}")

    # 6. Final Fraud Assessment Output
    print("\n--- 🚨 FORENSIC CONGLOMERATE CLASSIFICATION ---")
    print(f"Cluster 0 contains {len(cluster_0_points)} pill configurations.")
    print(f"Cluster 1 contains {len(cluster_1_points)} pill configurations.")
    
    # In a real environment, the chemist analyzes the centroids: 
    # High dissolving time with low active mass indicates a chalk-based counterfeit.
    if centroid_0[1] > centroid_1[1]:
        print("\nVerdict: Cluster 0 isolated the COUNTERFEITS. Cluster 1 isolated GENUINE assets.")
    else:
        print("\nVerdict: Cluster 1 isolated the COUNTERFEITS. Cluster 0 isolated GENUINE assets.")

    print("\n🏆 SUCCESS: Your unsupervised clustering loop isolated the distinct manufacturing variances!")
    print("The counterfeit shipment has been successfully seized before hitting hospital pharmacies.")

if __name__ == "__main__":
    kmeans_pharmacy_game()
