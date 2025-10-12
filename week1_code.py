import pandas as pd
import matplotlib.pyplot as plt

# Analysing [Fe/H] vs. Age data for Krause dataset

# Obtaining data-set and taking each column separately
krause = pd.read_csv(r"C:\Users\HassanNoun\OneDrive - UNSW\Desktop\PHYS3116\Group Assessment\GitHubClone_PHYS3116\PHYS3116_Team\Krause21.csv")
ages = krause["Age"]        # cluster ages
feh  = krause["FeH"]        # metallicities
mass = krause["Mstar"]      # stellar mass
rh   = krause["rh"]         # half-light radius
c5   = krause["C5"]         # concentration
names = krause["Object"]    # cluster names

# Plotting as a scatter plot
plt.scatter(feh, ages, color='black')
plt.xlabel("[Fe/H]")
plt.ylabel("Age (Gyr)")
plt.title("Age–Metallicity Relation (Krause21)")
plt.show()