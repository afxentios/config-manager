try:
    import unittest2 as unittest
except ImportError:
    import unittest

from config_manager.config_ruleset import ConfigRuleset


class ConfigurationRulesetTest(unittest.TestCase):
    def test_str_empty_default_empty_required(self):
        # Given
        rule_set = ConfigRuleset()
        expected = "Default Configuration: Empty \n Required Configurations: Empty"
        # When
        actual = rule_set.__str__()
        # Then
        self.assertEqual(actual, expected)

    def test_str_non_empty_default_non_empty_required(self):
        # Given
        rule_set = ConfigRuleset(defaults={'config_key': 'config_value'},
                                 required=['config_key'])
        expected = "Default Configuration: {'config_key': 'config_value'} \n Required Configurations: ['config_key']"
        # When
        actual = rule_set.__str__()
        # Then
        self.assertEqual(actual, expected)

    def test_validate_empty_config_does_not_raise_exception(self):
        # Given
        rule_set = ConfigRuleset()
        try:  # When
            rule_set.validate()
        except KeyError:  # Then
            self.fail("validate() raised KeyError: The following required config keys are missing")

    def test_validate_a_non_empty_correct_config_does_not_raise_exception(self):
        # Given
        rule_set = ConfigRuleset(defaults={'config_key': 'config_value'},
                                 required=['config_key'])
        try:  # When
            rule_set.validate()
        except KeyError:  # Then
            self.fail("validate() raised KeyError: The following required config keys are missing")

    def test_validate_a_non_empty_incorrect_config_raises_exception_for_a_missing_key(self):
        # Given
        rule_set = ConfigRuleset(defaults={'config_key': 'config_value'},
                                 required=['another_config_key'])
        # When - Then
        self.assertRaisesRegexp(KeyError, r"The following required config keys are missing: \['another_config_key'\]",
                                rule_set.validate)

    def test_validate_a_non_empty_incorrect_config_raises_exception_for_multiple_missing_keys(self):
        # Given
        rule_set = ConfigRuleset(defaults={'config_key': 'config_value'},
                                 required=['first_config_key', 'second_config_key'])
        # When - Then
        self.assertRaisesRegexp(KeyError,
                                r"The following required config keys are missing: \['first_config_key', "
                                r"'second_config_key'\]", rule_set.validate)
