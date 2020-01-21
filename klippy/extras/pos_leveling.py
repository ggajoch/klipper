import logging, bisect
import homing

class PosLevel:
    def __init__(self, config):
        self.printer = config.get_printer()
        # Register commands
        self.gcode = self.printer.lookup_object('gcode')
        self.gcode.register_command('POS_LEVEL', self.cmd_POS_LEVEL,
                                    desc=self.cmd_POS_LEVEL_help)
        self.gcode.register_command('MINX', self.MINX,
                                    desc=self.cmd_POS_LEVEL_help)

    cmd_POS_LEVEL_help = "Setup config for only MIN/MAX bed positions"

    def cmd_POS_LEVEL(self, params):
        self.gcode.respond_info("Wooorks!")

    def MINX(self, params):

        self.gcode.respond_info("MINX Woorks!")


def load_config(config):
    return PosLevel(config)
