from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

class Form(StatesGroup):
    phone = State()
    name = State()
    preferred_country = State()
    your_faculty = State()
    preferred_sphere = State()
