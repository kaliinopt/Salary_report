import pytest 
from file_reader import parse_csv_file, parse_csv_files

class TestParseCSVFile:
    """Tests for reading a single file"""

    def test_return_correct_len(self, sample_csv):
        employees = parse_csv_file(sample_csv)
        assert len(employees) == 2
    
    def test_parse_correctly_for_alice(self, sample_csv):
        employees = parse_csv_file(sample_csv)
        assert employees[0]['name'] == 'Alice Johnson'
        assert employees[0]['hours_worked'] == 170
        assert employees[0]['hourly_rate'] == 53

    def test_parse_correctly_for_bob(self, sample_csv):
        employees = parse_csv_file(sample_csv)
        assert employees[1]['name'] == 'Bob Smith'
        assert employees[1]['hours_worked'] == 144
        assert employees[1]['hourly_rate'] == 43
    
    @pytest.mark.parametrize("rate_column", ["rate", "hourly_rate", "salary"])
    def test_support_diffrent_column_names(self, tmp_path, rate_column):
        some_content = f"""id,name,hours_worked,{rate_column}
1,Some User,100,25"""
        file_path = tmp_path / "temp.csv"
        file_path.write_text(some_content)

        employees = parse_csv_file(file_path)
        assert employees[0]['hourly_rate'] == 25
    
    def test_support_diffrent_columns_order(self, tmp_path, sample_csv):
        some_content = f"""name,id,hours_worked,rate
                            Some User,1,100,25"""
        file_path = tmp_path / "temp.csv"
        file_path.write_text(some_content)

        employees1 = parse_csv_file(file_path)
        employees2 = parse_csv_file(sample_csv)
        assert employees1[0]['hourly_rate'] == 25
        assert employees2[0]['hourly_rate'] == 53
        assert employees1[0]['name'] == 'Some User'
        assert employees2[0]['name'] == 'Alice Johnson'

class TestParseCSVFiles:
    """Tests for reading multiple files"""

    def test_combines_data_from_files(self, sample_csv, sample_csv2):
        employees = parse_csv_files([sample_csv, sample_csv2])
        assert len(employees) == 3
        names = [i['name'] for i in employees]
        assert names == ["Alice Johnson","Bob Smith", "Carol Williams"]

    def test_raises_file_not_found_error(self):
        with pytest.raises(FileNotFoundError):
            parse_csv_files(["somescvthatdoesntexists.csv"])
    
    def test_handles_empty_file_list(self):
        assert parse_csv_files([]) == []