import logging, bisect
import homing

class PosLevel:
    def __init__(self, config):
        self.printer = config.get_printer()
        # Register commands
        self.gcode = self.printer.lookup_object('gcode')
        self.gcode.register_command('POS_LEVEL', self.cmd_POS_LEVEL,
                                    desc=self.cmd_POS_LEVEL_help)

    cmd_POS_LEVEL_help = "Setup config for only MIN/MAX bed positions"

    def cmd_POS_LEVEL(self, params):
        self.gcode.respond_info("Wooorks!")


def load_config(config):
    return PosLevel(config)
