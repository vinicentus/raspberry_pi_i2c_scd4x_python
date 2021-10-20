from _scd4x_driver import lib


class I2C:
    def sensirion_i2c_hal_init(self):
        lib.sensirion_i2c_hal_init()

    def sensirion_i2c_hal_free(self):
        lib.sensirion_i2c_hal_free()
