phone = "+79569899977"
text = ("Vel consequatur temporibus illum. Laudantium eligendi"
        " eos et placeat blanditiis. Eum delectus possimus aut. "
        "Minus at similique est sed ab exercitationem.")
email = "ttt@ttt.com"
date_1 = "11.01.2000"
date_2 = "2020-03-17"

phone_text = "+795698999779"  # 12 чисел в строке
email_text = "ttt@t@t.com"
date_text_1 = "31.02.2022"
date_text_2 = "2020-013-17"

phone_bad = 79569899979


templates = [
    {
        "name": "Шаблон 1",
        "field_name_1": "phone",
    },
    {
        "name": "Шаблон 2",
        "field_name_1": "phone",
        "field_name_2": "email",
        "field_name_3": "text",
    },
    {
        "name": "Шаблон 3",
        "field_name_1": "phone",
        "field_name_2": "email",
        "field_name_3": "text",
        "field_name_4": "date",
    },
    {
        "name": "Шаблон 4",
        "field_name_1": "phone",
        "field_name_2": "email",
        "field_name_3": "text",
        "field_name_4": "date",
        "field_name_5": "phone",
    },
    {
        "name": "Шаблон 5",
        "field_name_1": "phone",
        "field_name_2": "email",
        "field_name_3": "text",
        "field_name_4": "date",
        "field_name_5": "phone",
        "field_name_6": "email",
    },
    {
        "name": "Шаблон 6",
        "field_name_1": "phone",
        "field_name_2": "email",
        "field_name_3": "text",
        "field_name_4": "date",
        "field_name_5": "phone",
        "field_name_6": "email",
        "field_name_7": "text",
    },
    {
        "name": "Шаблон 7",
        "field_name_1": "phone",
        "field_name_2": "email",
        "field_name_3": "text",
        "field_name_4": "date",
        "field_name_5": "phone",
        "field_name_6": "email",
        "field_name_7": "text",
        "field_name_8": "date",
    },
    {
        "name": "Шаблон 8",
        "field_name_1": "phone",
        "field_name_2": "email",
        "field_name_3": "text",
        "field_name_4": "date",
        "field_name_5": "phone",
        "field_name_6": "email",
        "field_name_7": "text",
        "field_name_8": "date",
        "field_name_9": "email",
    },
    {
        "name": "Шаблон 9",
        "field_name_1": "phone",
        "field_name_2": "email",
        "field_name_3": "text",
        "field_name_4": "date",
        "field_name_5": "phone",
        "field_name_6": "email",
        "field_name_7": "text",
        "field_name_8": "date",
        "field_name_9": "email",
        "field_name_10": "text",
    },
    {
        "name": "Шаблон 10",
        "field_name_1": "phone",
        "field_name_2": "email",
        "field_name_3": "text",
        "field_name_4": "date",
        "field_name_5": "phone",
        "field_name_6": "email",
        "field_name_7": "text",
        "field_name_8": "date",
        "field_name_9": "email",
        "field_name_10": "text",
        "field_name_11": "date",
    },
    {
        "name": "Плохой шаблон",
        "field_name_1": "phone",
        "field_name_2": "email",
        "field_name_3": "text",
        "field_name_4": "date",
        "field_name_5": "phone",
        "field_name_6": "email",
        "field_name_7": "text",
        "field_name_8": "date",
        "field_name_9": "email",
        "field_name_10": "text",
        "field_name_11": "date",
        "bad_field_name_1": "text",
    },
]

forms_for_template = {
    'good_template': [
        (
            {
                "field_name_1": phone,
            },
            templates[0],
        ),
        (
            {
                "field_name_1": phone,
                "field_name_2": email,
                "field_name_3": text,
                "new_name_1": email_text,
            },
            templates[1],
        ),
        (
            {
                "field_name_1": phone,
                "field_name_2": email,
                "field_name_3": text,
                "field_name_4": date_1,
                "field_name_5": phone,
                "field_name_6": email,
                "field_name_7": email_text,
            },
            templates[5]
        ),
        (
            {
                "field_name_1": phone,
                "field_name_2": email,
                "field_name_3": phone_text,
                "field_name_4": date_1,
                "field_name_5": phone,
                "field_name_6": email,
                "field_name_7": text,
                "field_name_8": date_2,
                "field_name_9": email,
                "field_name_10": date_text_1,
                "field_name_11": "date",
                "new_name_2": date_text_2,
            },
            templates[8],
        ),

    ],
    'new_template': [
        (
            {
                "new_name_1": phone,
                "new_name_2": email,
                "new_name_3": date_text_2,
            },
            {
                "new_name_1": "phone",
                "new_name_2": "email",
                "new_name_3": "text",
            },
        ),
        (
            {
                "field_name_1": text,
                "field_name_2": email,
                "field_name_3": date_text_2,
                "field_name_4": date_2,
                "field_name_5": phone,
                "field_name_6": email,
                "field_name_7": phone_text,
            },
            {
                "field_name_1": "text",
                "field_name_2": "email",
                "field_name_3": "text",
                "field_name_4": "date",
                "field_name_5": "phone",
                "field_name_6": "email",
                "field_name_7": "text",
            },
        )

    ],
    'bad_template': [
        (
            {
                "_id": "phone",
                "field_name_1": phone,
                "field_name_2": email,
                "field_name_3": email_text,
            },
            None
        ),
        (
            {
                "name": "Шаблон 1",
                "field_name_1":phone,
            },
            None
        ),
        (
            {
                "field_name_1": phone_bad,
            },
            None
        ),
        (
            {
                "field_name_1": {"field_name_1": phone},
            },
            None
        ),
        (
            {
                "field_name_1": ["field_name_1"],
            },
            None
        )
    ]
}
