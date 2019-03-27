#! /usr/bin/env python3

import unittest

class TestBaseClass(unittest.TestCase):
    def get_failure_message_conditions(self, function, key_word_args):
        message = (
                "\n\n"
                "Calling `{function_name}` with the following parameters:\n".format(
                        function_name = function.__name__)
                )
        for parameter_name, parameter_value in key_word_args.items():
            message += "\t{parameter_name} = {parameter_value!r}    {parameter_type}\n".format(
                    parameter_name = parameter_name,
                    parameter_value = parameter_value,
                    parameter_type = type(parameter_value))
        return message

    def get_failure_message_issue(self, expected_result, result):
        message = (
                "Expecting\n"
                "\t{expected_result!r}    {expected_type}\n"
                "to be returned, but got\n"
                "\t{result!r}    {returned_type}\n".format(
                        expected_result = expected_result,
                        expected_type = type(expected_result),
                        result = result,
                        returned_type = type(result))
                )
        return message

    def get_failure_message(self, function, key_word_args, expected_result,
            result):
        message = self.get_failure_message_conditions(function, key_word_args)
        message += self.get_failure_message_issue(expected_result, result)
        return message

    def get_raise_failure_message(self, function, key_word_args, expected_exception):
        message = self.get_failure_message_conditions(function, key_word_args)
        message += "Expecting `{0}` to be raised, but it was not.".format(
                expected_exception.__name__)
        return message

    def run_test_of_function(self, function, key_word_args, expected_result):
        result = function(**key_word_args)
        self.assertEqual(result, expected_result,
                self.get_failure_message(
                        function = function,
                        key_word_args = key_word_args,
                        expected_result = expected_result,
                        result = result))

    def run_test_of_function_raise(self, function, key_word_args, expected_exception):
        try:
            ret = function(**key_word_args)
            # self.assertFail()
        except expected_exception as e:
            pass
        else:
            message = self.get_raise_failure_message(function, key_word_args,
                    expected_exception)
            self.assertTrue(False, message)
