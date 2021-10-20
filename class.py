from _scd4x_driver import lib
from cffi import FFI
from typing import Tuple

# TODO: fix return types


class SCD4x:

    _ffi = FFI()

    def scd4x_start_periodic_measurement() -> None:
        lib.scd4x_start_periodic_measurement()

    # TODO: check float type
    def scd4x_read_measurement_ticks() -> Tuple[int, int, int]:
        raise NotImplementedError

    def scd4x_read_measurement() -> Tuple[int, float, float]:
        # co2: int
        # temperature_deg_c: float
        # humidity_percent_rh: float
        raise NotImplementedError

    def scd4x_stop_periodic_measurement() -> None:
        lib.scd4x_stop_periodic_measurement()

    def scd4x_get_temperature_offset_ticks() -> int:
        raise NotImplementedError

    def scd4x_get_temperature_offset() -> float:
        raise NotImplementedError

    def scd4x_set_temperature_offset_ticks(t_offset: int) -> None:
        raise NotImplementedError

    def scd4x_set_temperature_offset(t_offset_deg_c: float) -> None:
        raise NotImplementedError

    def scd4x_get_sensor_altitude() -> int:
        raise NotImplementedError

    def scd4x_set_sensor_altitude(sensor_altitude: int) -> None:
        raise NotImplementedError

    def scd4x_set_ambient_pressure(ambient_pressure: int) -> None:
        raise NotImplementedError

    def scd4x_perform_forced_recalibration(target_co2_concentration: int) -> int:
        raise NotImplementedError

    def scd4x_get_automatic_self_calibration() -> bool:
        raise NotImplementedError

    def scd4x_set_automatic_self_calibration(asc_enabled: bool) -> None:
        raise NotImplementedError

    def scd4x_start_low_power_periodic_measurement() -> None:
        lib.scd4x_start_low_power_periodic_measurement()

    # TODO: convert into mor useful return type of bool
    # instead of using the original implementation
    def scd4x_get_data_ready_status() -> int:
        raise NotImplementedError

    def scd4x_persist_settings() -> None:
        lib.scd4x_persist_settings()

    # The return type here deviates from the C libary!
    def scd4x_get_serial_number() -> str:
        raise NotImplementedError

    def scd4x_perform_self_test() -> int:
        raise NotImplementedError

    def scd4x_perform_factory_reset() -> None:
        lib.scd4x_perform_factory_reset()

    def scd4x_reinit() -> None:
        lib.scd4x_reinit()

    def scd4x_measure_single_shot() -> None:
        lib.scd4x_measure_single_shot()

    def scd4x_measure_single_shot_rht_only() -> None:
        lib.scd4x_measure_single_shot_rht_only()

    def scd4x_power_down() -> None:
        lib.scd4x_power_down()

    def scd4x_wake_up() -> None:
        lib.scd4x_wake_up()
