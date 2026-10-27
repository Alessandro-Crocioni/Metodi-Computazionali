import pandas as pd
import matplotlib.pyplot as plt

file_name = 'kplr010666592-2011240104155_slc.csv'
df = pd.read_csv(file_name)
print("Colonne del DataFrame:")
print(df.columns)


time = df["TIME"]
flux = df["SAP_FLUX"]
error_flux = df["SAP_FLUX_ERR"]
plt.figure(figsize=(12, 5))
plt.errorbar(time, flux, yerr = error_flux, fmt = "o")
plt.xlabel("tempo[BJD-2454833]")
plt.ylabel("flusso[e/s]")
plt.title("flusso in funzione del tempo")
plt.savefig('image1', dpi=300)



t_min = 940.0
t_max = 942.5
df_zoom = df.loc[(df['TIME'] >= t_min) & (df['TIME'] <= t_max)]
plt.figure(figsize=(12, 5))
plt.errorbar(df_zoom["TIME"], df_zoom["SAP_FLUX"], yerr = df_zoom["SAP_FLUX_ERR"])
plt.xlabel("tempo[BJD-2454833]")
plt.ylabel("flusso[e/s]")
plt.title("flusso in funzione del tempo (zoom tra 120_125)")
plt.savefig('image2', dpi=300)




fig, ax = plt.subplots(figsize=(10, 6))
ax.errorbar(time, flux, yerr=df['SAP_FLUX_ERR'], fmt='.', elinewidth=0.5)
ax.set_xlabel('Tempo')
ax.set_ylabel('Flusso')
ax.set_title('Grafico con riquadro di zoom (Inset)')
ins_ax = ax.inset_axes([0.75, 0.70, 0.30, 0.30])
ins_ax.errorbar(df_zoom['TIME'], df_zoom['SAP_FLUX'], yerr=df_zoom['SAP_FLUX_ERR'], fmt='.',elinewidth=0.5,  color='orange')
ins_ax.set_title('Zoom minimo', fontsize=9)
plt.savefig("image3")
plt.show()

