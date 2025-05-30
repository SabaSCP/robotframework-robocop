from tests.linter.utils import RuleAcceptance


class TestRuleAcceptance(RuleAcceptance):
    def test_rule(self):
        self.check_rule(src_files=["default_and_empty_tags.robot"], expected_file="expected_output.txt")

    def test_extended(self):
        self.check_rule(
            src_files=["default_and_empty_tags.robot"], expected_file="expected_extended.txt", output_format="extended"
        )
