from aiogram.dispatcher.filters.state import StatesGroup, State


class QuestionParams (StatesGroup):
    """Машина состояний для Б/У"""

    start_bu = State()

    question_region = State()
    question_body = State()
    question_category = State()
    question_marka = State()
    question_model = State()
    question_year = State()
    question_price = State()
    question_fuel = State()
    question_kpp = State()
    question_volume = State()

    question_ended = State()

