from time import sleep
from i2c_class import I2C
from sensor_class import SCD4x

i2c = I2C()
sensor = SCD4x()

i2c.sensirion_i2c_hal_init()

# Clean up potential SCD40 states
sensor.scd4x_wake_up()
sensor.scd4x_stop_periodic_measurement()
sensor.scd4x_reinit()

serial = sensor.scd4x_get_serial_number()
print(f"Serial number: {hex(serial)}")

# Start Measurement
sensor.scd4x_start_periodic_measurement()

print("Waiting for first measurement... (5 sec)")

while True:
    # Read Measurement
    # TODO: sleep with native c method
    sleep(5)

    data_ready = sensor.scd4x_get_data_ready_status()

    print(f"Data ready: {data_ready}")

    if (data_ready):
        co2, temperature, humidity = sensor.scd4x_read_measurement()

        print(f"CO2: {co2} ppm")
        print(f"Temperature: {temperature} °C")
        print(f"Humidity: {humidity} RH")
