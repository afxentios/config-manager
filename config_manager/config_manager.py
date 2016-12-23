from __future__ import with_statement

try:
    import yaml
except ImportError:
    print ("[-] The yaml module is needed to use encrypted yaml.\nGo to http://pyyaml.org or `pip install PyYaml`")
    raise

try:
    import json
except ImportError:
    import simplejson as json

from config_ruleset import ConfigRuleset


class ConfigManager(ConfigRuleset):
    default_source_file = 'configs.yaml'
    cfg_path = None

    def __init__(self, config_file_path=default_source_file, defaults=None, required=None):
        """Create and initialize a ConfigManager object.

            parameters:
                config_file_path - Path of the configuration file
                defaults - Dictionary with the default values for the config files
                required - List with the required config keys which they need to exist in the config file.
        """

        super(ConfigManager, self).__init__(defaults, required)
        self.cfg_path = config_file_path
        self.load_config()
        self.validate()

    def __str__(self):
        defaults = self.defaults if self.defaults else "Empty"
        required = self.required if self.required else "Empty"
        return "Default Configuration: {0} \n Required Configurations: {1} \n Configuration File Path: {2}".format(
            str(defaults), str(required), self.cfg_path)

    def load_config(self):
        if self.cfg_path.endswith(".yaml"):
            self.load_yaml_file()
        elif self.cfg_path.endswith(".json"):
            self.load_json_file()
        else:
            print("The given config file format is not supported by this module: %s" % self.cfg_path)

    def load_yaml_file(self):
        try:
            entries = yaml.load(self.load_file_data()) if self.load_file_data() else None
            if entries:
                self.update(entries)
        except yaml.YAMLError as exception:
            print ("Error loading YAML file : {0}".format(exception))

    def load_json_file(self):
        try:
            entries = json.loads(self.load_file_data()) if self.load_file_data() else None
            if entries:
                self.update(entries)
        except ValueError as exception:
            print ("Error loading Json file : {0}".format(exception))

    def load_file_data(self):
        data = []
        try:
            with open(self.cfg_path, 'r') as config_file:
                data = config_file.read()
        except (OSError, IOError) as exception:
            print ("Error({0}) reading the file '{1}' : {2}".format(exception.errno, self.cfg_path, exception.strerror))
        return data
