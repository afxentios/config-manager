EMPTY_DICT = {}
EMPTY_LIST = []


class ConfigRuleset(dict):
    """
    Based on: https://code.google.com/archive/p/escservesconfig/
    """

    def __init__(self, defaults=None, required=None):
        """Create and initialize a ConfigRuleset object.

            parameters:
                defaults - Dictionary with the default values for the config files
                required - List with the required config keys which they need to exist in the config file.
        """

        defaults = defaults if defaults else EMPTY_DICT
        required = required if required else EMPTY_LIST

        super(ConfigRuleset, self).__init__()
        self.defaults = defaults
        self.required = required
        self.update(defaults)

    def __str__(self):
        defaults = self.defaults if self.defaults else "Empty"
        required = self.required if self.required else "Empty"
        return "Default Configuration: {0} \n Required Configurations: {1}".format(str(defaults), str(required))

    def validate(self):
        missing = []
        for key in self.required:
            if key not in self:
                missing.append(key)
        if len(missing):
            raise KeyError("The following required config keys are missing: {0}".format(str(missing)))
