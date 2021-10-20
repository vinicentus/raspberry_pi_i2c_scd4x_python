from _scd4x_driver import lib
from cffi import FFI
from typing import Tuple

# TODO: report errors if return values for original functiosn aren't 0


class SCD4x:

    _ffi = FFI()

    def scd4x_start_periodic_measurement(self) -> None:
        lib.scd4x_start_periodic_measurement()

    def scd4x_read_measurement_ticks(self) -> Tuple[int, int, int]:
        co2 = self._ffi.new("uint16_t *")
        temperature = self._ffi.new("uint16_t *")
        humidity = self._ffi.new("uint16_t *")
        lib.scd4x_read_measurement_ticks(co2, temperature, humidity)

        return (co2, temperature, humidity)

    def scd4x_read_measurement(self) -> Tuple[int, float, float]:
        co2_1 = self._ffi.new("uint16_t *")
        temperature_1 = self._ffi.new("float *")
        humidity_1 = self._ffi.new("float *")
        lib.scd4x_read_measurement(co2_1, temperature_1, humidity_1)
        co2 = co2_1[0]
        temperature_deg_c = temperature_1[0]
        humidity_percent_rh = humidity_1[0]
        return (co2, temperature_deg_c, humidity_percent_rh)

    def scd4x_stop_periodic_measurement(self) -> None:
        lib.scd4x_stop_periodic_measurement()

    def scd4x_get_temperature_offset_ticks(self) -> int:
        offset_pointer = self._ffi.new("uint16_t *")
        lib.scd4x_get_temperature_offset_ticks(offset_pointer)
        return offset_pointer[0]

    def scd4x_get_temperature_offset(self) -> float:
        offset_pointer = self._ffi.new("float *")
        lib.scd4x_get_temperature_offset(offset_pointer)
        return offset_pointer[0]

    def scd4x_set_temperature_offset_ticks(self, t_offset: int) -> None:
        offset_uint16_t = self._ffi.new("uint16_t", t_offset)
        lib.scd4x_set_temperature_offset_ticks(offset_uint16_t)

    def scd4x_set_temperature_offset(self, t_offset_deg_c: float) -> None:
        offset_float = self._ffi.new("float", t_offset_deg_c)
        lib.scd4x_set_temperature_offset(offset_float)

    def scd4x_get_sensor_altitude(self) -> int:
        altitude_pointer = self._ffi.new("uint16_t *")
        lib.scd4x_get_sensor_altitude(altitude_pointer)
        return altitude_pointer[0]

    def scd4x_set_sensor_altitude(self, sensor_altitude: int) -> None:
        altitude_uint16_t = self._ffi.new("uint16_t", sensor_altitude)
        lib.scd4x_set_sensor_altitude(altitude_uint16_t)

    def scd4x_set_ambient_pressure(self, ambient_pressure: int) -> None:
        pressure_uint16_t = self._ffi.new("uint16_t", ambient_pressure)
        lib.scd4x_set_ambient_pressure(pressure_uint16_t)

    def scd4x_perform_forced_recalibration(self, target_co2_concentration: int) -> int:
        target_uint16_t = self._ffi.new("uint16_t", target_co2_concentration)
        frc_correction_pointer = self._ffi.new("uint16_t *")
        lib.scd4x_perform_forced_recalibration(
            target_uint16_t, frc_correction_pointer)
        return frc_correction_pointer[0]

    # The return type here deviates from the C libary!
    def scd4x_get_automatic_self_calibration(self) -> bool:
        asc_enabled_uint16_t = self._ffi.new("uint16_t *")
        lib.scd4x_get_automatic_self_calibration(asc_enabled_uint16_t)
        return bool(asc_enabled_uint16_t[0])

    def scd4x_set_automatic_self_calibration(self, asc_enabled: bool) -> None:
        asc_enabled_uint16_t = self._ffi.new("uint16_t", int(asc_enabled))
        lib.scd4x_set_automatic_self_calibration(asc_enabled_uint16_t)

    def scd4x_start_low_power_periodic_measurement(self) -> None:
        lib.scd4x_start_low_power_periodic_measurement()

    # The return type here deviates from the C libary!
    def scd4x_get_data_ready_status(self) -> bool:
        data_ready_uint16_t_pointer = self._ffi.new("uint16_t *")
        lib.scd4x_get_data_ready_status(data_ready_uint16_t_pointer)
        # Do some processing to get a boolean value
        data_ready_int = data_ready_uint16_t_pointer[0]
        # data_ready_int.bit_length() should be 16 because this integer is converted from a uint16_t
        # "If last 11 bits are 0 data not ready, else data ready"
        relevant_bits_bitmask = 0b0000111111111111
        relevant_bits = data_ready_int & relevant_bits_bitmask
        return relevant_bits != 0

    def scd4x_persist_settings(self) -> None:
        lib.scd4x_persist_settings()

    # The return type here deviates from the C libary!
    def scd4x_get_serial_number(self) -> int:
        serial_0 = self._ffi.new("uint16_t *")
        serial_1 = self._ffi.new("uint16_t *")
        serial_2 = self._ffi.new("uint16_t *")
        lib.scd4x_get_serial_number(serial_0, serial_1, serial_2)
        # This is ineficcient, but it will do for now
        serial = hex(serial_0[0]) + hex(serial_1[0]
                                        ).lstrip("0x") + hex(serial_2[0]).lstrip("0x")
        return int(serial, 16)

    def scd4x_perform_self_test(self) -> int:
        sensor_status_uint16_t = self._ffi.new("uint16_t *")
        lib.scd4x_perform_self_test(sensor_status_uint16_t)
        return sensor_status_uint16_t[0]

    def scd4x_perform_factory_reset(self) -> None:
        lib.scd4x_perform_factory_reset()

    def scd4x_reinit(self) -> None:
        lib.scd4x_reinit()

    def scd4x_measure_single_shot(self) -> None:
        lib.scd4x_measure_single_shot()

    def scd4x_measure_single_shot_rht_only(self) -> None:
        lib.scd4x_measure_single_shot_rht_only()

    def scd4x_power_down(self) -> None:
        lib.scd4x_power_down()

    def scd4x_wake_up(self) -> None:
        lib.scd4x_wake_up()
