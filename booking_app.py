import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Booking & Cancellation Analysis",
    page_icon="📅"
)

st.title("📅 Booking & Cancellation Analysis")

st.write(
    "Análisis de reservas, booking window, pickup y cancelaciones."
)

# Datos de ejemplo
reservas = [
    {
        "booking_id": 1,
        "booking_date": "2026-09-01",
        "arrival_date": "2026-09-05",
        "status": "Confirmed",
        "room_revenue": 450
    },
    {
        "booking_id": 2,
        "booking_date": "2026-09-02",
        "arrival_date": "2026-09-06",
        "status": "Cancelled",
        "room_revenue": 300
    },
    {
        "booking_id": 3,
        "booking_date": "2026-09-03",
        "arrival_date": "2026-09-07",
        "status": "Confirmed",
        "room_revenue": 520
    },
    {
        "booking_id": 4,
        "booking_date": "2026-09-04",
        "arrival_date": "2026-09-08",
        "status": "Confirmed",
        "room_revenue": 600
    },
    {
        "booking_id": 5,
        "booking_date": "2026-09-05",
        "arrival_date": "2026-09-10",
        "status": "Cancelled",
        "room_revenue": 400
    },
    {
        "booking_id": 6,
        "booking_date": "2026-09-06",
        "arrival_date": "2026-09-11",
        "status": "Confirmed",
        "room_revenue": 750
    },
    {
        "booking_id": 7,
        "booking_date": "2026-09-07",
        "arrival_date": "2026-09-12",
        "status": "Confirmed",
        "room_revenue": 850
    },
    {
        "booking_id": 8,
        "booking_date": "2026-09-08",
        "arrival_date": "2026-09-13",
        "status": "Confirmed",
        "room_revenue": 900
    }
]

# Convertir los datos en un DataFrame
df = pd.DataFrame(reservas)

# Convertir las fechas
df["booking_date"] = pd.to_datetime(df["booking_date"])
df["arrival_date"] = pd.to_datetime(df["arrival_date"])

# Calcular booking window
df["booking_window"] = (
    df["arrival_date"] - df["booking_date"]
).dt.days

# Métricas principales
total_reservas = len(df)

reservas_canceladas = (
    df["status"] == "Cancelled"
).sum()

reservas_confirmadas = (
    df["status"] == "Confirmed"
).sum()

tasa_cancelacion = (
    reservas_canceladas / total_reservas
) * 100

booking_window_promedio = df["booking_window"].mean()

# Mostrar métricas
st.subheader("Key Metrics")

ingresos_confirmados = df[
    df["status"] == "Confirmed"
]["room_revenue"].sum()

ingresos_cancelados = df[
    df["status"] == "Cancelled"
]["room_revenue"].sum()

st.subheader("Revenue by Booking Status")

col1, col2 = st.columns(2)

col1.metric(
    "Confirmed Revenue",
    f"${ingresos_confirmados:,.2f}"
)

col2.metric(
    "Cancelled Revenue",
    f"${ingresos_cancelados:,.2f}"
)

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Bookings", total_reservas)
col2.metric("Confirmed", reservas_confirmadas)
col3.metric("Cancelled", reservas_canceladas)
col4.metric("Cancellation Rate", f"{tasa_cancelacion:.2f}%")

st.metric(
    "Average Booking Window",
    f"{booking_window_promedio:.1f} days"
)

# Mostrar tabla
st.subheader("Reservation Details")

# Filtro por estado de reserva
filtro_estado = st.selectbox(
    "Filter by booking status:",
    ["All", "Confirmed", "Cancelled"]
)

if filtro_estado == "All":
    df_filtrado = df.copy()
else:
    df_filtrado = df[df["status"] == filtro_estado].copy()

# Filtro por fecha de llegada
fecha_llegada = st.date_input(
    "Filter by arrival date:",
    value=None
)

if fecha_llegada is not None:
    df_filtrado = df_filtrado[
        df_filtrado["arrival_date"].dt.date == fecha_llegada
    ]

st.dataframe(
    df_filtrado,
    use_container_width=True
)

st.dataframe(
    df_filtrado,
    use_container_width=True
)

# Descargar datos filtrados
csv_filtrado = df_filtrado.to_csv(index=False).encode("utf-8")

st.download_button(
    label="Download Filtered Reservations",
    data=csv_filtrado,
    file_name="filtered_reservations.csv",
    mime="text/csv"
)

# Pickup por fecha de reserva
st.subheader("Pickup by Booking Date")

pickup = (
    df.groupby("booking_date")
    .size()
    .rename("bookings")
)

st.bar_chart(pickup)

# Distribución de estados
st.subheader("Booking Status Distribution")

status_counts = df["status"].value_counts()

st.bar_chart(status_counts)

# Conclusiones automáticas
st.subheader("Automatic Conclusions")

if tasa_cancelacion > 20:
    st.warning(
        "The cancellation rate is relatively high. "
        "The hotel should review cancellation policies "
        "and booking conditions."
    )
else:
    st.success(
        "The cancellation rate is relatively low."
    )

if booking_window_promedio < 5:
    st.info(
        "Guests are booking close to their arrival date. "
        "Short-term demand monitoring is important."
    )
else:
    st.info(
        "Guests are booking in advance. "
        "The hotel can use this information for forecasting."
    )