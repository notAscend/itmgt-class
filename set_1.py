#先苦後甜
import sys
from os import path
if(path.exists('input.txt')):
    sys.stdin = open("input.txt","r")
    sys.stdout = open("output.txt","w")
    
def savings(gross_pay, tax_rate, expenses):
    save = int((1-tax_rate)*gross_pay)
    save-=expenses
    return save

def material_waste(total_material, material_units, num_jobs, job_consumption):
    waste = total_material-(num_jobs*job_consumption)
    return (str(waste)+material_units)

def interest(principal, rate, periods):
    final = principal+principal*(rate*periods)
    return int(final)