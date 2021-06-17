from datetime import datetime

class CurrentMonth:
    CURRENT_MONTH = datetime.now().strftime('%B')
    CURRENT_MONTH_INT = int(datetime.now().strftime('%m'))