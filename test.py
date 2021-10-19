from _scd4x_driver import lib
from cffi import FFI
from time import sleep

ffi = FFI()

lib.sensirion_i2c_hal_init()

# Clean up potential SCD40 states
lib.scd4x_wake_up()
lib.scd4x_stop_periodic_measurement()
lib.scd4x_reinit()


serial_0 = ffi.new("uint16_t *")
serial_1 = ffi.new("uint16_t *")
serial_2 = ffi.new("uint16_t *")
result = lib.scd4x_get_serial_number(serial_0, serial_1, serial_2)
serial = hex(serial_0[0]) + hex(serial_1[0]).lstrip("0x") + hex(serial_2[0]).lstrip("0x")

if (result): 
    print("Error executing scd4x_get_serial_number(): {}".format(result))
else:
    print(serial)


# Start Measurement
result = lib.scd4x_start_periodic_measurement()
if (result):
    print("Error executing scd4x_start_periodic_measurement(): {}".format(result))

print("Waiting for first measurement... (5 sec)")

while True:
    # Read Measurement
    # TODO: sleep with native c method
    sleep(5)

    co2_1 =ffi.new("uint16_t *")
    temperature_1 = ffi.new("float *")
    humidity_1 = ffi.new("float *")
    error = lib.scd4x_read_measurement(co2_1, temperature_1, humidity_1)
    co2 = co2_1[0]
    temperature = temperature_1[0]
    humidity = humidity_1[0]

    if (error):
        print("Error executing scd4x_read_measurement(): {}".format(error))
    elif (co2 == 0):
        print("Invalid sample detected, skipping.")
    else:
        print("CO2:{} ppm".format(co2))
        print("Temperature: {} °C".format(temperature))
        print("Humidity: {} RH".format(humidity))
