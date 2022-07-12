from aiogram.dispatcher.filters.state import StatesGroup, State


class QuestionParams (StatesGroup):
    """Машина состояний для Б/У"""

    question_category  = State()
    question_marka = State()
    question_model = State()
    question_from_year = State()
    question_to_year = State()
    question_from_price = State()
    question_to_price = State()
    question_ended = State()

