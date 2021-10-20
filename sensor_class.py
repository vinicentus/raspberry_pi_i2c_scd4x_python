from _scd4x_driver import lib
from cffi import FFI
from typing import Tuple

# TODO: report errors if return values for original functiosn aren't 0


class SCD4x:

    _ffi = FFI()

    def scd4x_start_periodic_measurement(self) -> None:
        lib.scd4x_start_periodic_measurement()

    # TODO: check float type
    def scd4x_read_measurement_ticks(self) -> Tuple[int, int, int]:
        raise NotImplementedError

    def scd4x_read_measurement(self) -> Tuple[int, float, float]:
        co2_1 = self._ffi.new("uint16_t *")
        temperature_1 = self._ffi.new("float *")
        humidity_1 = self._ffi.new("float *")
        result = lib.scd4x_read_measurement(co2_1, temperature_1, humidity_1)
        co2 = co2_1[0]
        temperature_deg_c = temperature_1[0]
        humidity_percent_rh = humidity_1[0]
        return (co2, temperature_deg_c, humidity_percent_rh)

    def scd4x_stop_periodic_measurement(self) -> None:
        lib.scd4x_stop_periodic_measurement()

    def scd4x_get_temperature_offset_ticks(self) -> int:
        raise NotImplementedError

    def scd4x_get_temperature_offset(self) -> float:
        raise NotImplementedError

    def scd4x_set_temperature_offset_ticks(self, t_offset: int) -> None:
        raise NotImplementedError

    def scd4x_set_temperature_offset(self, t_offset_deg_c: float) -> None:
        raise NotImplementedError

    def scd4x_get_sensor_altitude(self) -> int:
        raise NotImplementedError

    def scd4x_set_sensor_altitude(self, sensor_altitude: int) -> None:
        raise NotImplementedError

    def scd4x_set_ambient_pressure(self, ambient_pressure: int) -> None:
        raise NotImplementedError

    def scd4x_perform_forced_recalibration(self, target_co2_concentration: int) -> int:
        raise NotImplementedError

    def scd4x_get_automatic_self_calibration(self) -> bool:
        raise NotImplementedError

    def scd4x_set_automatic_self_calibration(self,asc_enabled: bool) -> None:
        raise NotImplementedError

    def scd4x_start_low_power_periodic_measurement(self) -> None:
        lib.scd4x_start_low_power_periodic_measurement()

    # TODO: convert into mor useful return type of bool
    # instead of using the original implementation
    def scd4x_get_data_ready_status(self) -> int:
        raise NotImplementedError

    def scd4x_persist_settings(self) -> None:
        lib.scd4x_persist_settings()

    # The return type here deviates from the C libary!
    def scd4x_get_serial_number(self) -> str:
        serial_0 = self._ffi.new("uint16_t *")
        serial_1 = self._ffi.new("uint16_t *")
        serial_2 = self._ffi.new("uint16_t *")
        result = lib.scd4x_get_serial_number(serial_0, serial_1, serial_2)
        serial = hex(serial_0[0]) + hex(serial_1[0]
                                        ).lstrip("0x") + hex(serial_2[0]).lstrip("0x")
        return serial

    def scd4x_perform_self_test(self) -> int:
        raise NotImplementedError

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
