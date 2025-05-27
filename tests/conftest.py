import pytest

@pytest.fixture
def sample_csv(tmp_path):
    content = """id,email,name,department,hours_worked,rate
1,alice123@example.com,Alice Johnson,Marketing,170,53
2,bob123@example.com,Bob Smith,Design,144,43"""

    file_path = tmp_path / "some.csv"
    file_path.write_text(content)
    return file_path

@pytest.fixture
def sample_csv2(tmp_path):
    """Sample employee data with 'salary' column"""
    content = """id,email,name,department,hours_worked,salary
3,carol@example.com,Carol Williams,Design,170,60"""
    file_path = tmp_path / "sample2.csv"
    file_path.write_text(content)
    return file_path