from typing import List, Dict, Any
import os

RATE_ALIASES = {'hourly_rate', 'rate', 'salary'}


def parse_csv_file(file_path: str) -> List[Dict[str, Any]]:
    """Read data from csv file"""
    employees = []

    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readline()
        if not lines:
            return employees
        
        headers = [i.strip() for i in lines[0].split(',')]

        for line in lines[1:]:
            if not line.strip():
                continue

            values = [i.strip() for i in line.split(',')]
            employee = dict[zip(headers, values)]

            rate_key = next()