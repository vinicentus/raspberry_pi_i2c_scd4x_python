from cffi import FFI

ffibuilder = FFI()


ffibuilder.cdef(
    """
int16_t scd4x_start_periodic_measurement(void);
int16_t scd4x_read_measurement_ticks(uint16_t* co2, uint16_t* temperature,
                                     uint16_t* humidity);
int16_t scd4x_read_measurement(uint16_t* co2, float* temperature_deg_c,
                               float* humidity_percent_rh);
int16_t scd4x_stop_periodic_measurement(void);
int16_t scd4x_get_temperature_offset_ticks(uint16_t* t_offset);
int16_t scd4x_get_temperature_offset(float* t_offset_deg_c);
int16_t scd4x_set_temperature_offset_ticks(uint16_t t_offset);
int16_t scd4x_set_temperature_offset(float t_offset_deg_c);
int16_t scd4x_get_sensor_altitude(uint16_t* sensor_altitude);
int16_t scd4x_set_sensor_altitude(uint16_t sensor_altitude);
int16_t scd4x_set_ambient_pressure(uint16_t ambient_pressure);
int16_t scd4x_perform_forced_recalibration(uint16_t target_co2_concentration,
                                           uint16_t* frc_correction);
int16_t scd4x_get_automatic_self_calibration(uint16_t* asc_enabled);
int16_t scd4x_set_automatic_self_calibration(uint16_t asc_enabled);
int16_t scd4x_start_low_power_periodic_measurement(void);
int16_t scd4x_get_data_ready_status(uint16_t* data_ready);
int16_t scd4x_persist_settings(void);
int16_t scd4x_get_serial_number(uint16_t* serial_0, uint16_t* serial_1,
                                uint16_t* serial_2);
int16_t scd4x_perform_self_test(uint16_t* sensor_status);
int16_t scd4x_perform_factory_reset(void);
int16_t scd4x_reinit(void);
int16_t scd4x_measure_single_shot(void);
int16_t scd4x_measure_single_shot_rht_only(void);
int16_t scd4x_power_down(void);
int16_t scd4x_wake_up(void);


void sensirion_i2c_hal_init(void);
void sensirion_i2c_hal_free(void);
""")

ffibuilder.set_source('_scd4x_driver',  # name of the output C extension
                      """
#include "raspberry-pi-i2c-scd4x/scd4x_i2c.h"
#include "raspberry-pi-i2c-scd4x/sensirion_i2c_hal.h"
""",
                      sources=['raspberry-pi-i2c-scd4x/scd4x_i2c.c', 'raspberry-pi-i2c-scd4x/sensirion_common.c',
                               'raspberry-pi-i2c-scd4x/sensirion_i2c.c', 'raspberry-pi-i2c-scd4x/sensirion_i2c_hal.c', ],   # includes pi.c as additional sources
                      )

if __name__ == "__main__":
    ffibuilder.compile(verbose=True)
