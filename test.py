from _scd4x_driver import lib
from cffi import FFI
from time import sleep
from sensor_class import SCD4x

ffi = FFI()
sensor = SCD4x()

lib.sensirion_i2c_hal_init()

# Clean up potential SCD40 states
sensor.scd4x_wake_up()
sensor.scd4x_stop_periodic_measurement()
sensor.scd4x_reinit()

serial = sensor.scd4x_get_serial_number()
print(serial)

# Start Measurement
sensor.scd4x_start_periodic_measurement()

print("Waiting for first measurement... (5 sec)")

while True:
    # Read Measurement
    # TODO: sleep with native c method
    sleep(5)

    data_ready = sensor.scd4x_get_data_ready_status()

    print("Data ready: {}".format(data_ready))

    if (data_ready):
        co2, temperature, humidity = sensor.scd4x_read_measurement()

        print("CO2: {} ppm".format(co2))
        print("Temperature: {} °C".format(temperature))
        print("Humidity: {} RH".format(humidity))
