

def get_text(temp: int, sky: tuple) -> str:
    emoji = ''
    for s in sky:
        if s['id'] == 800:
            emoji = '☀'
            break
        elif s['id'] == 801 or s['id'] == 802:
            emoji = '🌤'
            break
        elif s['id'] == 803 or s['id'] == 804:
            emoji = '☁'
            break
        elif 300 <= s['id'] <= 531:
            emoji = '⛈'
            break

    return '+' + str(temp) + emoji



