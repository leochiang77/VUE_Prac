from datetime import datetime

def recordTime(func):
    def wrapper(**kwargs):
        start_time = datetime.now()
        result = func(**kwargs)
        print("--- %s seconds ---" % (datetime.now() - start_time))
        return result
    return wrapper