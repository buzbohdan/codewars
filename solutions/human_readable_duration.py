"""https://www.codewars.com/kata/52742f58faf5485cae000b9a/train/python"""
def format_section(section):
    multiple = 's' if section[1] > 1 else ''
    return f'{section[1]} {section[0]}{multiple}'

def format_duration(seconds):
    if seconds == 0:
        return 'now'

    durations: list[tuple[str, int]] = []

    sections = (('second', 60), ('minute', 60), ('hour', 24), ('day', 365))
    for duration_type, length in sections:
        durations.append((duration_type, seconds % length))
        seconds //= length
    durations.append(('year', seconds))

    formatted_sections = [format_section(i) for i in durations if i[1] > 0]
    if len(formatted_sections) == 1:
        return formatted_sections[0]
    return f"{', '.join(formatted_sections[-1:0:-1])} and {formatted_sections[0]}"

res = format_duration(373500000)