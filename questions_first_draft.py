###CONFIGURATION LEVELS
CONFIG = "R1(config)#"
CRYPTO_POLICY = "R1(config-crypto-policy)#"

questions = [
    {
    "question": """Please create a policy for ISAKMP. Policy Number 10. The ISAKMP policy shoud use AES for encryption,
    Diffie-Hellemen group 5, and something just slightly more secure than MD5 for hashing. The password will be cisco.
    Type 'Hint' for a clue.\n""",

    "about": """PLACE DESCRIPTION OF ISAKMP HERE""",

    "answer_lines": [
        {"answer": "crypto isakmp policy 10", "level": CONFIG, "hint": "hint"},
        {"answer": "authentication pre-share", "level": CRYPTO_POLICY, "hint": "The password should be cisco"},
        {"answer": "encryption aes", "level": CRYPTO_POLICY, "hint": "We want to use AES"},
        {"answer": "hash sha", "level": CRYPTO_POLICY, "hint": "Hashing will be SHA"},
        {"answer": "group 5", "level": CRYPTO_POLICY, "hint": "We want to use Diffie-Hellemen group 5"},
    ]
    },
    {
    "question": """You will now need to configure the password itself. Remember, it will be "cisco"
    The neighbor is going to be 1.2.1.2. You can still type "hint" for a hint, or "sample" for an example.\n\n\n""",

    "about": """PLACE DESCRIPTION OF ISAKMP KEY HERE""",

    "answer_lines": [
        {"answer": "crypto isakmp key cisco neighbor 1.2.1.2", "level": CONFIG, "hint": "hint"},
    ]
    },
]