import pandas as pd
import matplotlib.pyplot as plt

# Load medical dataset
df = pd.read_csv('heart_disease_data.csv')

# Calculate basic health statistics
print("=== Medical Dataset Summary ===")
print(f"Total Patients Analyzed: {len(df)}")
print(f"Average Age: {df['Age'].mean():.1f} years")
print(f"Average Cholesterol Level: {df['Cholesterol'].mean():.1f} mg/dL")
print(f"Average Resting Blood Pressure: {df['RestingBP'].mean():.1f} mmHg")

# Generate visualization for Cholesterol vs Age
plt.figure(figsize=(8, 5))
plt.scatter(df['Age'], df['Cholesterol'], c=df['HeartDisease'], cmap='coolwarm', s=100, alpha=0.8)
plt.title('Medical Analysis: Age vs. Cholesterol Levels')
plt.xlabel('Age (Years)')
plt.ylabel('Cholesterol (mg/dL)')
plt.grid(True)
plt.savefig('cholesterol_vs_age.png')
print("\nPlot successfully generated and saved as 'cholesterol_vs_age.png'")