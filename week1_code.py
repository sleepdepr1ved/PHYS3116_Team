# %%


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

# Plotting [Fe/H] for all data-sets.
# Harris datasets (Part I + Part III)
harris1 = pd.read_csv(r"C:\Users\HassanNoun\OneDrive - UNSW\Desktop\PHYS3116\Group Assessment\GitHubClone_PHYS3116\PHYS3116_Team\HarrisPartI.csv")
harris3 = pd.read_csv(r"C:\Users\HassanNoun\OneDrive - UNSW\Desktop\PHYS3116\Group Assessment\GitHubClone_PHYS3116\PHYS3116_Team\HarrisPartIII.csv")
harris = pd.concat([harris1, harris3], ignore_index=True)
ages_h = harris["Age"]
feh_h  = harris["FeH"]

# vandenBerg dataset
vberg = pd.read_csv(r"C:\Users\HassanNoun\OneDrive - UNSW\Desktop\PHYS3116\Group Assessment\GitHubClone_PHYS3116\PHYS3116_Team\vandenBerg_table2.csv")
ages_v = vberg["Age"]
feh_v  = vberg["FeH"]

# Combined scatter plot for all datasets
plt.figure(figsize=(8,6))
plt.scatter(feh,   ages,   color='black',     label="Krause (2021)", alpha=0.7)
plt.scatter(feh_h, ages_h, color='royalblue', label="Harris (1996, 2010 rev.)", alpha=0.7)
plt.scatter(feh_v, ages_v, color='crimson',   label="vandenBerg (2013)", alpha=0.7)

plt.gca().invert_xaxis()  # conventional in astronomy: metal-rich (high [Fe/H]) on left
plt.xlabel("[Fe/H]")
plt.ylabel("Age (Gyr)")
plt.title("Globular Cluster Age–Metallicity Relation (All Datasets)")
plt.legend()
plt.grid(True, linestyle="--", alpha=0.5)
plt.tight_layout()
plt.show()