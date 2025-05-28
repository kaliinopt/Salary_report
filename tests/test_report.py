import pytest
import json
from report import PayoutJsonReport, PayoutReport, get_report


class TestPayoutJsonReport:
    """Tests for getting json report"""

    def test_generate_json_report(self, sample_user_data):
        report = PayoutJsonReport().generate(sample_user_data)
        report_data = json.loads(report)
        assert "employees" in report_data
        assert report_data["type"] == "payout"
        assert len(report_data["employees"]) == 5

    def test_if_empty_data_json(self, empty):
        report = PayoutJsonReport().generate(empty)
        print(report)
        report_data = json.loads(report)
        assert report_data == {"type": "payout", "employees": []}


class TestPayoutReport:
    """Tests for getting report"""

    def test_report_table(self, sample_user_data):
        report = PayoutReport().generate(sample_user_data)
        print(report)
        assert "Marketing" in report
        assert "Hours" in report
        assert "$8000" in report
        assert "Company Total" in report

    def test_report_empty(self, empty):
        report = PayoutReport().generate(empty)
        print(report)
        assert report == f"\nCompany Total " + "-" * 24 + f"> ${0:>7.2f}"


class TestGetReport:
    """Test for generator"""

    def test_get_report(self):

        some_value = "payout"

        report = get_report(some_value)

        assert isinstance(report, PayoutReport)

    def test_ivalid_type(self):
        some_invalid_value = "invalid"
        with pytest.raises(
            ValueError, match=f"Unknown report type: {some_invalid_value}"
        ):
            get_report(some_invalid_value)
