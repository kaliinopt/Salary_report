from typing import List, Dict, Any
import os

RATE_ALIASES = {'hourly_rate', 'rate', 'salary'}

def parse_csv_file(file_path: str) -> List[Dict[str, Any]]:
    """Read data from csv file"""
    employees = []
    
    with open(file_path, 'r') as f:
        lines = f.readlines()
        if not lines:
            return employees
            
        headers = [h.strip() for h in lines[0].split(',')]
        
        for line in lines[1:]:
            if not line.strip():
                continue
                
            values = [val.strip() for val in line.split(',')]
            employee = dict(zip(headers, values))
            
            rate_key = next((k for k in employee.keys() if k in RATE_ALIASES), None)
            if not rate_key:
                raise ValueError(f"No valid rate column found in {file_path}")
                
            try:
                employee['hours_worked'] = float(employee['hours_worked'])
                employee[rate_key] = float(employee[rate_key])
            except ValueError:
                raise ValueError(f"Invalid value type in {file_path}")
                
            employee['hourly_rate'] = employee.pop(rate_key)
            employees.append(employee)
    
    return employees

def parse_csv_files(file_paths: List[str]) -> List[Dict[str, Any]]:
    """Read from multiplie files"""
    employees = []
    
    for file_path in file_paths:
        if not os.path.exists(file_path) : # test for existing
            raise FileNotFoundError(f"File not found: {file_path}")
        employees.extend(parse_csv_file(file_path))
    
    return employees