import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import LinearSegmentedColormap

# Define a custom colormap that transitions from light blue to white to light coral (light red)
custom_cmap = LinearSegmentedColormap.from_list(
    'light_red_blue', 
    ['lightblue', 'white', 'lightcoral'], 
    N=256
)

# -------------------------------
# 1. Heatmap of ML Model Usage Across CKC Stages
# -------------------------------

# Define the ML model types and CKC stages
ml_models = ["Reinforcement Learning", "Machine Learning", "Large Language Models", "Hybrid", "Other"]
ckc_stages = ["Recon", "Weaponization", "Delivery", "Exploitation", "Installation", "Cmd & Ctrl", "Objectives"]

# Construct an assumed data matrix (rows: models, columns: CKC stages)
data = np.array([
    [1, 0, 0, 9, 2, 4, 3],   # Reinforcement Learning
    [2, 0, 0, 5, 1, 1, 2],   # Machine Learning
    [0, 0, 0, 3, 0, 1, 0],   # Large Language Models
    [0, 0, 0, 2, 0, 0, 1],   # Hybrid
    [3, 0, 0, 2, 0, 0, 0]    # Other
])

plt.figure(figsize=(8,6))
# Use the custom colormap
im = plt.imshow(data, cmap=custom_cmap, aspect="auto")
plt.colorbar(im)
plt.xticks(ticks=np.arange(len(ckc_stages)), labels=ckc_stages, rotation=45, ha="right")
plt.yticks(ticks=np.arange(len(ml_models)), labels=ml_models)
plt.title("Heatmap of ML Model Usage across CKC Stages")
plt.xlabel("Cyber Kill Chain Stages")
plt.ylabel("ML Model Types")

# Annotate each cell with the numeric value
for i in range(data.shape[0]):
    for j in range(data.shape[1]):
        text_color = "white" if data[i,j] > data.max()/2 else "black"
        plt.text(j, i, str(data[i,j]), ha="center", va="center", color=text_color)
plt.tight_layout()
plt.savefig("heatmap_ml_ckc.png")
plt.show()



# -------------------------------
# 2. Distribution of Performance Metrics Used
# -------------------------------

# Metrics data (assumed based on extracted study information):
# Metrics: Accuracy, Sensitivity, Detection Rate, Capture Rate, Session Length.
# Count indicates how many studies reported the metric.
# Average values (in percentage) are annotated where applicable.
metrics = ["Accuracy", "Sensitivity", "Detection Rate", "Capture Rate", "Session Length"]
metric_counts = [6, 2, 1, 1, 2]
average_values = [84, 87, 92, 90, None]  # For Session Length, average value is not applicable

plt.figure(figsize=(8,5))
bars = plt.bar(metrics, metric_counts, color="lightgreen")
plt.title("Distribution of Performance Metrics Reported")
plt.xlabel("Performance Metric")
plt.ylabel("Count of Studies")

# Annotate each bar with the average value (if available)
for bar, avg in zip(bars, average_values):
    if avg is not None:
        plt.text(bar.get_x() + bar.get_width()/2, bar.get_height(), f"Avg: {avg}%",
                 ha='center', va='bottom', fontsize=9)
    else:
        plt.text(bar.get_x() + bar.get_width()/2, bar.get_height(), "N/A",
                 ha='center', va='bottom', fontsize=9)
plt.tight_layout()
plt.savefig("metrics_distribution.png")
plt.show()