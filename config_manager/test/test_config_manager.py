try:
    import unittest2 as unittest
except ImportError:
    import unittest
import sys
from io import BytesIO as StringIO

from mock import patch, mock_open

from config_manager.config_manager import ConfigManager

patch.object = patch.object


class ConfigurationManagerTest(unittest.TestCase):
    def setUp(self):
        sys.stdout = sys.__stdout__
        self.out = StringIO()
        sys.stdout = self.out

    def test_str_empty_default_empty_required(self):
        # Given
        config_man = ConfigManager()
        expected = "Default Configuration: Empty \n Required Configurations: Empty \n " \
                   "Configuration File Path: configs.yaml"
        # When
        actual = config_man.__str__()
        # Then
        self.assertEqual(actual, expected)

    def test_str_non_empty_default_non_empty_required(self):
        # Given
        config_man = ConfigManager(config_file_path="/path/to/config.yaml",
                                   defaults={'config_key': 'config_value'},
                                   required=['config_key'])
        expected = "Default Configuration: {'config_key': 'config_value'} \n Required Configurations: ['config_key'] " \
                   "\n Configuration File Path: /path/to/config.yaml"
        # When
        actual = config_man.__str__()
        # Then
        self.assertEqual(actual, expected)

    @staticmethod
    @patch.object(ConfigManager, 'load_yaml_file')
    def test_load_yaml_file_called_when_yaml_file_loaded(mocked_load_yaml_file):
        # Given
        config_file_path = "/path/to/config.yaml"
        # When
        ConfigManager(config_file_path=config_file_path)
        # Then
        mocked_load_yaml_file.assert_called_once_with()

    @patch.object(ConfigManager, 'load_file_data')
    def test_load_yaml_file_when_yaml_file_loaded_is_correct(self, mocked_load_file_data):
        # Given
        config_file_path = "/path/to/config.yaml"
        mocked_load_file_data.return_value = '{"config_key":"config_value", ' \
                                             ' "another_config_key":"another_config_value"}'
        # When
        config_man = ConfigManager(config_file_path=config_file_path)
        # Then
        self.assertDictEqual(config_man, {"config_key": "config_value", "another_config_key": "another_config_value"})

    @patch.object(ConfigManager, 'load_file_data')
    def test_load_yaml_file_when_yaml_file_loaded_is_faulty(self, mocked_load_file_data):
        # Given
        config_file_path = "/path/to/config.yaml"
        mocked_load_file_data.return_value = '{"config_key""config_value"}'
        # When
        ConfigManager(config_file_path=config_file_path)
        output = self.out.getvalue().strip()
        # Then
        self.assertIn("Error loading YAML file ", output)

    @patch.object(ConfigManager, 'load_file_data')
    def test_load_yaml_file_when_yaml_file_loaded_is_faulty_2(self, mocked_load_file_data):
        # Given
        config_file_path = "/path/to/config.json"
        mocked_load_file_data.return_value = '{"config_key"}'
        # When
        ConfigManager(config_file_path=config_file_path)
        output = self.out.getvalue().strip()
        # Then
        self.assertEqual(output, "Error loading Json file : Expecting : delimiter: line 1 column 14 (char 13)")

    @staticmethod
    @patch.object(ConfigManager, 'load_json_file')
    def test_load_json_file_called_when_json_file_loaded(mocked_load_json_file):
        # Given
        config_file_path = "/path/to/config.json"
        # When
        ConfigManager(config_file_path=config_file_path)
        # Then
        mocked_load_json_file.assert_called_once_with()

    @patch.object(ConfigManager, 'load_file_data')
    def test_load_json_file_when_json_file_loaded_is_correct(self, mocked_load_file_data):
        # Given
        config_file_path = "/path/to/config.json"
        mocked_load_file_data.return_value = '{"config_key":"config_value", ' \
                                             ' "another_config_key":"another_config_value"}'
        # When
        config_man = ConfigManager(config_file_path=config_file_path)
        # Then
        self.assertDictEqual(config_man, {"config_key": "config_value", "another_config_key": "another_config_value"})

    @patch.object(ConfigManager, 'load_file_data')
    def test_load_json_file_when_json_file_loaded_is_faulty(self, mocked_load_file_data):
        # Given
        config_file_path = "/path/to/config.json"
        mocked_load_file_data.return_value = '{"config_key":}'
        # When
        ConfigManager(config_file_path=config_file_path)
        output = self.out.getvalue().strip()
        # Then
        self.assertEqual(output, "Error loading Json file : No JSON object could be decoded")

    @patch.object(ConfigManager, 'load_file_data')
    def test_load_json_file_when_json_file_loaded_is_faulty_2(self, mocked_load_file_data):
        # Given
        config_file_path = "/path/to/config.json"
        mocked_load_file_data.return_value = '{"config_key"}'
        # When
        ConfigManager(config_file_path=config_file_path)
        output = self.out.getvalue().strip()
        # Then
        self.assertEqual(output, "Error loading Json file : Expecting : delimiter: line 1 column 14 (char 13)")

    def test_output_when_not_supported_format_file_loaded(self):
        # Given
        config_file_path = "/path/to/config.smth"
        # When
        ConfigManager(config_file_path=config_file_path)
        output = self.out.getvalue().strip()
        # Then
        self.assertEqual(output, "The given config file format is not supported by this module: /path/to/config.smth")

    def test_load_file_data_raise_error_when_incorrect_path(self):
        # Given
        config_man = ConfigManager(config_file_path="/incorrectPath/incorrectFile.json")
        expected = []
        # When
        output = self.out.getvalue().strip()
        # Then
        self.assertEqual(output,
                         "Error(2) reading the file '/incorrectPath/incorrectFile.json' : No such file or directory")
        self.assertEqual(config_man.load_file_data(), expected)

    @patch('__builtin__.open',
           mock_open(read_data="config_key: 'config_value'\nanother_config_key: 'another_config_value'"))
    def test_load_file_data_return_data(self):
        # Given
        config_man = ConfigManager()
        expected = "config_key: 'config_value'\nanother_config_key: 'another_config_value'"
        # When
        actual = config_man.load_file_data()
        # Then
        self.assertEqual(actual, expected)
