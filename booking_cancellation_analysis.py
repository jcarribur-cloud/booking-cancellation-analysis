# Booking & Cancellation Analysis

from datetime import datetime

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

print("Booking & Cancellation Analysis")
print("--------------------------------")
print(f"Total bookings: {len(reservas)}")

# Calcular booking window
for reserva in reservas:
    fecha_reserva = datetime.strptime(
        reserva["booking_date"],
        "%Y-%m-%d"
    )

    fecha_llegada = datetime.strptime(
        reserva["arrival_date"],
        "%Y-%m-%d"
    )

    booking_window = (
        fecha_llegada - fecha_reserva
    ).days

    reserva["booking_window"] = booking_window

print("\nBooking Window")
print("--------------")

for reserva in reservas:
    print(
        f"Booking {reserva['booking_id']}: "
        f"{reserva['booking_window']} days"
    )

    # Analizar cancelaciones

total_reservas = len(reservas)

reservas_canceladas = 0
reservas_confirmadas = 0

for reserva in reservas:
    if reserva["status"] == "Cancelled":
        reservas_canceladas += 1
    else:
        reservas_confirmadas += 1

tasa_cancelacion = (
    reservas_canceladas / total_reservas
) * 100

print("\nCancellation Analysis")
print("---------------------")

print(f"Confirmed bookings: {reservas_confirmadas}")
print(f"Cancelled bookings: {reservas_canceladas}")
print(f"Cancellation rate: {tasa_cancelacion:.2f}%")


# Analizar pickup

pickup_por_fecha = {}

for reserva in reservas:
    fecha_reserva = reserva["booking_date"]

    if fecha_reserva in pickup_por_fecha:
        pickup_por_fecha[fecha_reserva] += 1
    else:
        pickup_por_fecha[fecha_reserva] = 1

print("\nPickup Analysis")
print("---------------")

for fecha, cantidad in pickup_por_fecha.items():
    print(
        f"{fecha}: {cantidad} booking(s)"
    )

