import os
from dotenv import load_dotenv

load_dotenv()

# Токен бота
BOT_TOKEN = os.getenv('BOT_TOKEN', 'YOUR_BOT_TOKEN_HERE')

# Хранилище данных о сообщениях (всё в памяти, как раньше)
messages_storage = {
    'scheduled_text': 'Ваше первое сообщение',
    'scheduled_time': '09:00',
    'send_message_text': 'Стандартное сообщение',
    'group_id': None,
    'weekly_schedule': {
        'monday': {},
        'tuesday': {},
        'wednesday': {},
        'thursday': {},
        'friday': {},
        'saturday': {},
        'sunday': {}
    }
}

def save_schedule(data):
    """Сохраняет расписание (пока только логирует)"""
    # Для Railway.app данные хранятся в памяти во время работы
    # При перезагрузке нужно будет переподобавлять расписание
    pass
