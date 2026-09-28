# IoT-Based-Energy-Meter
import time
import csv
import random
from datetime import datetime

# -----------------------------
# IoT-Based Energy Meter
# -----------------------------

VOLTAGE = 230.0       # Supply voltage in volts
SAMPLE_TIME = 1       # Sampling interval in seconds

# Create CSV file and write header
with open("energy_data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow([
        "Date",
        "Time",
        "Voltage (V)",
        "Current (A)",
        "Power (W)",
        "Energy (kWh)"
    ])

total_energy = 0.0

print("=" * 55)
print("       IoT-BASED ENERGY METER")
print("=" * 55)
print("Monitoring started...\n")

try:
    while True:

        # Simulate current sensor reading
        current = random.uniform(0.5, 5.0)

        # Calculate power
        power = VOLTAGE * current

        # Calculate energy consumed
        # Power(W) × time(hours)
        energy = power * (SAMPLE_TIME / 3600)

        total_energy += energy / 1000

        # Current date and time
        now = datetime.now()

        date = now.strftime("%Y-%m-%d")
        current_time = now.strftime("%H:%M:%S")

        # Display readings
        print("-" * 55)
        print(f"Date       : {date}")
        print(f"Time       : {current_time}")
        print(f"Voltage    : {VOLTAGE:.2f} V")
        print(f"Current    : {current:.2f} A")
        print(f"Power      : {power:.2f} W")
        print(f"Energy     : {total_energy:.6f} kWh")

        # Save data to CSV
        with open("energy_data.csv", "a", newline="") as file:
            writer = csv.writer(file)

            writer.writerow([
                date,
                current_time,
                f"{VOLTAGE:.2f}",
                f"{current:.2f}",
                f"{power:.2f}",
                f"{total_energy:.6f}"
            ])

        time.sleep(SAMPLE_TIME)

except KeyboardInterrupt:

    print("\n\nMonitoring stopped.")
    print(f"Total Energy Consumed: {total_energy:.6f} kWh")
    print("Data saved to energy_data.csv")
