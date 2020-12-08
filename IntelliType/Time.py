

def str_to_seconds(value: str):
    try:
        if value.endswith('ms'):
            value = value.replace('ms','')
            denum = 1000
        elif value.endswith('s'):
            value = value.replace('s', '')
            denum = 1
        elif value.endswith('m'):
            value = value.replace('m', '')
            denum = 1/60
        elif value.endswith('h'):
            value = value.replace('h', '')
            denum = 1/3600
        else:
            print("Not valid time format " + value + "! Fallback to notime")
            return 0
        return int(value)/denum
    except ValueError:
        print("Not valid time format "+value +"! Fallback to notime")
        return 0


class Time:
    def __init__(self,time : str):
        self.t = str_to_seconds(time)

    def get_time_in_seconds(self):
        return self.t