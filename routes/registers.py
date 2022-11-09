from fastapi import APIRouter
from config.db import conn
from models.models import registers_table
from schemas.registers import Register

registers = APIRouter()

@registers.get("/registers")
def show_all_registers():
    return conn.execute(registers_table.select()).fetchall()


@registers.post("/registers", response_model=list[Register])
def create_register(register:Register):
    new_register = {"adress": register.adress, 
                    "amount": register.amount,
                    "operation": register.operation,
                    "creation_time": register.creation_time}
    result = conn.execute(registers_table.insert().values(new_register))
    print(result)