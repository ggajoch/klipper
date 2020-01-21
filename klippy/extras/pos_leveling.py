import logging, bisect
import homing

class PosLevel:
    def __init__(self, config):
        self.printer = config.get_printer()
        # Register commands
        self.gcode = self.printer.lookup_object('gcode')
        self.gcode.register_command('POS_LEVEL', self.cmd_POS_LEVEL,
                                    desc=self.cmd_POS_LEVEL_help)
        self.gcode.register_command('MINX', self.cmd_MINX,
                                    desc=self.cmd_MINX_help)

    cmd_POS_LEVEL_help = "Setup config for only MIN/MAX bed positions"
    cmd_MINX_help = "/MAX bed positions"

    def cmd_POS_LEVEL(self, params):
        self.gcode.respond_info("Wooorks!")

    def cmd_MINX(self, params):
        val = self.gcode.get_float('_', params, None)
        if val is not None:
            self.gcode.respond_info("MINX Woorks! {}".format(val))

        # with open('/home/pi/test', 'w') as f:
        #     f.write('dupa')
        


def load_config(config):
    return PosLevel(config)
