languages = {1: "french", 2: "spanish"}
homework_list = {
    "french":
        ["Page 3/4", "Page 4/6"],
    "spanish":
        ["Page 13/14", "Page 14/16"],
            }


def get_key(lang):
    for key, value in languages.items():
        if value == lang:
            return key


def add_homework(lang=None, text=None):
    if lang and text:

        lang_hwork = homework_list[lang]

        lang_hwork.append(text)
