



import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns



# Load the dataset
bikehour_df = pd.read_csv("data_terpakai.csv")

# st.write(bikehour_df.columns.tolist())

try:
    bikehour_df = pd.read_csv("data_terpakai.csv", delimiter=';')
    bikehour_df.columns = bikehour_df.columns.str.strip()  # Remove any whitespace from column names
except Exception as e:
    st.error(f"Error loading data: {e}")


# Sidebar untuk memilih rentang waktu tahun
st.sidebar.title("Filter Rentang Tahun")
year_range = st.sidebar.slider("Pilih Tahun", min_value=int(bikehour_df["Year"].min()), 
                               max_value=int(bikehour_df["Year"].max()), value=(2011, 2012))

# Hanya menggunakan satu metode untuk menampilkan gambar di sidebar
st.sidebar.image('Dashboard/sepeda.png', width=250)

# Filter berdasarkan tahun yang dipilih
filtered_df = bikehour_df[(bikehour_df["Year"] >= year_range[0]) & (bikehour_df["Year"] <= year_range[1])]


    

# 1. Total Penyewaan Sepeda Berdasarkan Musim
st.header("Perbandingan Penyewaan Sepeda Berdasarkan Musim")

total_sewa_per_musim = filtered_df.groupby(["Season", "Year"])["cnt"].sum().reset_index()

fig, ax = plt.subplots()
sns.barplot(data=total_sewa_per_musim, x="Season", y="cnt", hue="Year", palette="magma", ax=ax)
ax.set_ylabel("Total Jumlah Penyewaan")
ax.set_title("Total Penyewaan Sepeda Berdasarkan Musim dan Tahun")
plt.tight_layout()
st.pyplot(fig)



# 2. Total Penyewaan Sepeda Berdasarkan Cuaca
st.header("Perbandingan Penyewaan Sepeda Berdasarkan Kondisi Cuaca")

total_sewa_per_cuaca = filtered_df.groupby(["WeatherSituation", "Year"])["cnt"].sum().reset_index()

fig, ax = plt.subplots()
sns.barplot(data=total_sewa_per_cuaca, x="WeatherSituation", y="cnt", hue="Year", palette="magma", ax=ax)
ax.set_ylabel("Total Jumlah Penyewaan")
ax.set_title("Total Penyewaan Sepeda Berdasarkan Kondisi Cuaca")
plt.tight_layout()
st.pyplot(fig)

# 3. Analisa Penyewaan Pada Tiap Hari
st.header("Analisa Penyewaan Pada Tiap Hari")

jumlah_rental_weekday = filtered_df.groupby(["Weekday", "Year"])["cnt"].sum().reset_index()

fig, ax = plt.subplots()
sns.lineplot(data=jumlah_rental_weekday, x="Weekday", y="cnt", hue="Year", palette="viridis", marker="o", ax=ax)
ax.set_ylabel("Total Jumlah Penyewaan")
ax.set_title("Analisa Penyewaan Pada Tiap Hari")
plt.tight_layout()
st.pyplot(fig)

# 4. Perbandingan Pengguna Casual dan Terdaftar
st.header("Perbandingan Pengguna Casual dan Terdaftar")

casual_counts = filtered_df.groupby("Year")["casual"].sum().reset_index()
casual_counts.columns = ["Year", "Total_Casual"]

registered_counts = filtered_df.groupby("Year")["registered"].sum().reset_index()
registered_counts.columns = ["Year", "Total_Registered"]

fig, ax = plt.subplots()
bar_width = 0.35
index = casual_counts["Year"]

ax.bar(index, casual_counts["Total_Casual"], bar_width, label="Casual Users", color="pink")
ax.bar(index + bar_width, registered_counts["Total_Registered"], bar_width, label="Registered Users", color="purple")
ax.set_xlabel("Year")
ax.set_ylabel("Total Counts")
ax.set_title("Casual vs Registered Users by Year")
ax.legend()
plt.tight_layout()
st.pyplot(fig)

# 5. Total Penyewaan Sepeda Berdasarkan Bulan
st.header("Total Penyewaan Sepeda Berdasarkan Bulan")

jumlah_rental_bulanan = filtered_df.groupby(["Month", "Year"])["cnt"].sum().reset_index()

fig, ax = plt.subplots()
sns.lineplot(data=jumlah_rental_bulanan, x="Month", y="cnt", hue="Year", palette="viridis", marker="o", ax=ax)
ax.set_ylabel("Total Jumlah Penyewaan")
ax.set_title("Total Penyewaan Sepeda Berdasarkan Bulan")
plt.tight_layout()
st.pyplot(fig)

# 6. Total Penyewaan Sepeda Berdasarkan Jam
st.header("Total Penyewaan Sepeda Berdasarkan Jam")

jumlah_rental_jam = filtered_df.groupby(["hr", "Year"])["cnt"].sum().reset_index()

fig, ax = plt.subplots()
sns.lineplot(data=jumlah_rental_jam, x="hr", y="cnt", hue="Year", palette="viridis", marker="o", ax=ax)
ax.set_ylabel("Total Jumlah Penyewaan")
ax.set_xlabel("Jam")
ax.set_title("Total Penyewaan Sepeda Berdasarkan Jam")
plt.tight_layout()
st.pyplot(fig)
