import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Define the number of samples
n_samples = 5000  

# Set a random seed for reproducibility
np.random.seed(42)

# Generate random variables simulating operational conditions
temperatura = np.random.normal(loc=80, scale=10, size=n_samples)  # Mean 80°C, std 10°C
pressao = np.random.normal(loc=200, scale=30, size=n_samples)  # Mean 200 kPa, std 30 kPa
vibracao = np.random.normal(loc=5, scale=1.5, size=n_samples)  # Mean 5 mm/s, std 1.5 mm/s
horas_uso = np.random.randint(100, 10000, size=n_samples)  # Between 100 and 10,000 hours
tensao_mecanica = np.random.normal(loc=50, scale=15, size=n_samples)  # Mean 50 MPa, std 15 MPa
material = np.random.choice(['Titanium', 'Aluminum', 'Composite'], size=n_samples)  # Material type

# Define the target variable (failure: 1 = occurred, 0 = did not occur)
falha = (temperatura > 90) | (pressao > 250) | (vibracao > 7) | (horas_uso > 8000)
falha = falha.astype(int)  # Convert boolean to 0 or 1

# Create DataFrame
df = pd.DataFrame({
    'Temperature': temperatura,
    'Pressure': pressao,
    'Vibration': vibracao,
    'Usage_Hours': horas_uso,
    'Mechanical_Stress': tensao_mecanica,
    'Material': material,
    'Failure': falha
})

# Save as CSV file
df.to_csv('aerospace_failure_data.csv', index=False)

print("File generated: aerospace_failure_data.csv")