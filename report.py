from typing import List, Dict, Any
from abc import ABC, abstractmethod
import json

class Report(ABC):
    @abstractmethod
    def generate(self, employees: List[Dict]) -> Dict:
        pass


class PayoutReport(Report):
    def generate(self, employees: List[Dict[str, Any]]) -> str:
    
        departments = {}
        for emp in employees:
            dept = emp['department']
            if dept not in departments:
                departments[dept] = []
            departments[dept].append(emp)
        
        table = []
        total_company = 0
        
        for dept, emps in departments.items():
            table.append(f"\n{dept}")
            table.append("-" * 55)
            table.append(f"{'Name':<20} | {'Hours':>6} | "
                         f"{'Rate':>4} | {'Payout':>6}"
            )
            table.append("-" * 55)
            dept_total = 0
            
            for emp in emps:
                payout = emp['hours_worked'] * emp['hourly_rate']
                table.append(
                    f"{emp['name']:<20} | {emp['hours_worked']:>6} | "
                    f"${emp['hourly_rate']:>4} | ${payout:>6.2f}"
                )
                dept_total += payout
            table.append("-" * 55)
            table.append(f"{'Total':<20} | {sum(e['hours_worked'] for e in emps):>6} | "
                        f"{'':>5} | ${dept_total:>7.2f}")
            total_company += dept_total
        
        table.append("\nCompany Total " + "-" * 24 + f"> ${total_company:>7.2f}")
        return "\n".join(table)


class PayoutJsonReport(Report):
    """This function returns json_data about"""
    def generate(self, employees: List[Dict]) -> Dict:
        payouts = []
        for emp in employees:
            payout = emp["hours_worked"] * emp["hourly_rate"]
            payouts.append({
                "name": emp.get("name"),
                "email": emp.get("email"),
                "department": emp.get("department"),
                "hours": emp.get("hours_worked"),
                "rate": f"{emp.get("hourly_rate")}$",
                "payout": f"{round(payout, 2)}$",
            })
            json_form = {"type": "payout", "employees": payouts}

            result = json.dumps(json_form, indent=2)
        return result
    

def get_report(report_type: str):
    """
    Function that returns a report generator instance based on the requested type.
    """
    reports = {
        "payout": PayoutReport,
        "payout_json": PayoutJsonReport
    }

    report_class = reports.get(report_type)
    if not report_class:
        raise ValueError(f"Unknown report type: {report_type}")
    
    return report_class()