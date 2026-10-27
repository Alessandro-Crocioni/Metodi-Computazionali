import pandas as pd
import matplotlib.pyplot as plt

mydf = pd.DataFrame( columns=["periodo", "massa", "massa_solare", "orbita" ])
c1 = [87.97, 224.70, 365.26, 686.98, 4332.59, 10759.22, 30685.40, 60189.24 ]
c2 = [0.000175, 0.002565, 0.003146, 0.000338, 1.0, 0.299526, 0.045753, 0.053952]
c3 = [1, 1, 1, 1, 1, 1, 1, 1]
c4 = [0.39, 0.72, 1.00, 1.52, 5.20, 9.58, 19.22, 30.05]
mydf["periodo"] = c1
mydf["massa"] = c2
mydf["massa_solare"] = c3
mydf["orbita"] = c4

file_name = "ExoplanetsPars_2025.csv"
df = pd.read_csv(file_name, comment = "#")
print("colonne del dataframe")
print(df.columns)

dati = df[["pl_orbper", "pl_bmassj", "pl_orbsmax", "st_mass", "discoverymethod"]]
print(dati.columns)

plt.figure(figsize=(8, 6))
plt.scatter(df["pl_orbper"], df["pl_bmassj"], alpha=0.4, s=10, label ="Exoplanets")
plt.scatter(mydf["periodo"], mydf["massa"], alpha=0.5, s=20, color = "green", label ="Solar System")
plt.xscale("log")
plt.yscale("log")
plt.xlabel("Periodo Orbitale [days] (pl_orbper)")
plt.ylabel("Massa del pianeta [Jupiter Mass] (pl_bmassj)")
plt.title("Massa del pianeta vs Periodo Orbitale")
plt.grid(True, which="both", ls="--", alpha=0.5)
plt.legend()
plt.savefig('image1', dpi=300)



R_max = df["pl_orbsmax"]
Mass = df["st_mass"]
R_max2 = mydf["orbita"]
Mass2 = mydf["massa_solare"]
Periodo = df["pl_orbper"]
y_val = (R_max**2)/Mass
y_val2 = (R_max2**2)/Mass2
plt.figure(figsize=(8, 6))
plt.scatter(df["pl_orbper"], y_val, alpha=0.4, s=10, color="orange", label= "Exoplanets")
plt.scatter(mydf["periodo"],y_val2, alpha=0.5, s=20, color="green", label = "Solar System" )
plt.xscale("log")
plt.yscale("log")
plt.xlabel("Periodo Orbitale [days]")
plt.ylabel(r"$R_{max}^2 / m_*$")
plt.title("Grandezza derivata vs Periodo Orbitale")
plt.grid(True, which="both", ls="--", alpha=0.5)
plt.legend()
plt.savefig('image2', dpi=300)


T_ex = df.loc[df["discoverymethod"] == "Transit"]
Rv_ex = df.loc[df["discoverymethod"] == "Radial Velocity"]
plt.figure(figsize=(8, 6))
plt.scatter(T_ex["pl_orbper"], T_ex["pl_bmassj"], alpha=0.4, s = 10, color="orange", label = "Transit" )
plt.scatter(Rv_ex["pl_orbper"], Rv_ex["pl_bmassj"], alpha=0.4, s = 10, color="blue", label = "Radial Velocity" )
plt.scatter(mydf["periodo"], mydf["massa"], alpha=0.5, s=20, color = "green", label ="Solar System")
plt.xscale("log")
plt.yscale("log")
plt.xlabel("Periodo orbitale")
plt.ylabel("Massa pianeta")
plt.title("confrento tra diversi metodi di acquisizione")
plt.grid(True, which="both", ls="--", alpha=0.5)
plt.legend()
plt.savefig('image3', dpi=300)



plt.figure(figsize=(8, 6))
plt.hist(T_ex["pl_bmassj"], bins = 100, alpha=0.3, label = "Transit", density = True, range = (0, 3), color = "orange")
plt.hist(Rv_ex["pl_bmassj"], bins = 100, alpha=0.3, label = "Radial Velocity", density = True, range = (0, 3), color = "blue")
plt.hist(mydf["massa"], bins = 100, alpha=0.3, label = "Solar System", density = True, range = (0, 3), color = "green")
plt.xlabel("Planet Mass")
plt.ylabel("Density")
plt.title("Istogramma sovrapposto delle masse")
plt.savefig('image4', dpi=300)



plt.figure(figsize=(8, 6))
plt.hist(T_ex["pl_bmassj"], bins = 100, alpha=0.3, label = "Transit", density = True, range = (0, 5), color = "orange")
plt.hist(Rv_ex["pl_bmassj"], bins = 100, alpha=0.3, label = "Radial Velocity", density = True, range = (0, 5), color = "blue")
plt.hist(mydf["massa"], bins = 100, alpha=0.3, label = "Solar System", density = True, range = (0, 5), color = "green")
plt.xscale("log")
plt.xlabel("Planet Mass")
plt.ylabel("Density")
plt.title("Istogramma sovrapposto delle masse")
plt.savefig('image5', dpi=300)
plt.show()

