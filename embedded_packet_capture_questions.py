import config_levels as cli

questions = [
    {
    "question": """
    Create a capture buffer to store our Packet Capture
    """,

    "about": """
    Creating a EPC; Add doc
    """,

    "sample": """
    monitor capture buffer BUF size 2048 max-size 1518 linear
    """,

    "answer_lines": [
        {"answer": "monitor capture buffer BUF size 2048 max-size 1518 linear",
        "level": cli.EXEC,
        "hint": "Create a capture buffer named BUF."},
    ]
    },
    {
    "question": """
    Attach an access-list BUF-FILTER to the buffer BUF
    """,

    "about": """
    PLACE DESCRIPTION HERE
    """,

    "sample": """
    PLACE SAMPLE HERE
    """,

    "answer_lines": [
        {"answer": "monitor capture buffer BUF filter access-list BUF-FILTER",
        "level": cli.EXEC,
        "hint": "cisco"},
    ]
    },
        {
    "question": """
    Create a capture point for ip cef traffic inbound and outbound on interface g0/1.
    """,

    "about": """
    PLACE DESCRIPTION HERE
    """,

    "sample": """
    monitor capture point ip cef POINT G0/1 both
    """,

    "answer_lines": [
        {"answer": "monitor capture point ip cef POINT G0/1 both",
        "level": cli.EXEC,
        "hint": "cisco"},
    ]
    },
        {
    "question": """
    PLACE QUESTION HERE
    """,

    "about": """
    PLACE DESCRIPTION HERE
    """,

    "sample": """
    PLACE SAMPLE HERE
    """,

    "answer_lines": [
        {"answer": "cisco",
        "level": cli.EXEC,
        "hint": "cisco"},
    ]
    },
        {
    "question": """
    Associate our capture point POINT with our buffer BUF.
    """,

    "about": """
    PLACE DESCRIPTION HERE
    """,

    "sample": """
    PLACE SAMPLE HERE
    """,

    "answer_lines": [
        {"answer": "monitor capture point associate POINT BUF",
        "level": cli.EXEC,
        "hint": "cisco"},
    ]
    },
        {
    "question": """
    Start our capture point POINT.
    """,

    "about": """
    PLACE DESCRIPTION HERE
    """,

    "sample": """
    monitor capture point start POINT
    """,

    "answer_lines": [
        {"answer": "monitor capture point start POINT",
        "level": cli.EXEC,
        "hint": "cisco"},
    ]
    },
        {
    "question": """
    Stop our capture point POINT.
    """,

    "about": """
    PLACE DESCRIPTION HERE
    """,

    "sample": """
    monitor capture point stop POINT
    """,

    "answer_lines": [
        {"answer": "monitor capture point stop POINT",
        "level": cli.EXEC,
        "hint": "cisco"},
    ]
    },
        {
    "question": """
    Export our EPC packet capture 
    """,

    "about": """
    PLACE DESCRIPTION HERE
    """,

    "sample": """
    monitor capture buffer BUF export tftp://1.2.3.4/my.pcap
    """,

    "answer_lines": [
        {"answer": "monitor capture buffer BUF export tftp://1.2.3.4/my.pcap",
        "level": cli.EXEC,
        "hint": "cisco"},
    ]
    },
]