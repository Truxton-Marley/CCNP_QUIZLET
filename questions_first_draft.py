import config_levels as cli

questions = [
    {
    "question": """
    Please create a policy for ISAKMP. Policy Number 10. The ISAKMP policy shoud use AES for encryption,
    Diffie-Hellmen group 5, and something just slightly more secure than MD5 for hashing. The password will be cisco.
    Type 'Hint' for a clue.\n
    """,

    "about": """
    ISAKMP stands for the INTERNET SECURITY AND KEY MANAGEMENT PROTOCOL. If builds two tunnels.
    The first tunnel is the IKE tunnel. Here we are practicing IKEv1. We will then use this tunnel
    to build the IPsec tunnel itself. The ISAKMP POLICY should contain:
    H -> Hash: make sure the data hasn't been changed or corrupted.
    A -> Authention: make sure the peer is really who they say they are.
    G -> Group: used to negotiate keys between the peers.
    L -> Lifetime: cisco provides a default of 24 hours.
    E -> Encryption: encrypt the data for secrecy.
    """,

    "sample": """
    crypto isakmp policy 10
      authentication pre-share
      encryption aes
      hash sha
      group 5
    """,

    "answer_lines": [
        {
          "answer": "crypto isakmp policy 10",
          "level": cli.CONFIG,
          "hint": "You need to create a policy for isakmp. It should be #10"
        },
        {
          "answer": "authentication pre-share",
          "level": cli.CRYPTO_POLICY,
          "hint": "We're going to use a password"
        },
        {
          "answer": "encryption aes",
          "level": cli.CRYPTO_POLICY,
          "hint": "We want to use AES"
        },
        {"answer": "hash sha", "level": cli.CRYPTO_POLICY, "hint": "Hashing will be SHA"},
        {"answer": "group 5", "level": cli.CRYPTO_POLICY, "hint": "We want to use Diffie-Hellmen group 5"},
    ]
    },

    {
    "question": """
    You will now need to configure the password itself. Remember, it will be "cisco"
    The address for its peer is going to be 1.2.1.2. You can still type "hint" for a hint, or "sample" for an example.\n\n\n""",

    "about": """PLACE DESCRIPTION OF ISAKMP KEY HERE""",

    "sample": """
    crypto isakmp key cisco address 1.2.1.2 no-xauth
    """,

    "answer_lines": [
        {"answer": "crypto isakmp key cisco address 1.2.1.2 no-xauth", "level": cli.CONFIG,
        "hint": "Setup the password cisco for address 1.2.1.2. Type 'sample' if you want to see how to do it."},
    ]
    },
    {
    "question": """
    Up next is setting up the transform-set. This is for Phase II negotiation for the IPsec tunnel. We're going to use
    ESP with aes 256 and sha hmac. This will use 'tunnel mode' which is the default. Name your transform-set TSET. Remember
    you can type 'sample' to see the solution and 'about' for more info on the subject. Using 'about' is highly recommended
    the first time learning about a subject!\n
    """,

    "about": """
    PLACE DESCRIPTION HERE
    """,

    "sample": """
    crypto ipsec transform-set TSET 256 esp-aes esp-sha-hmac
    """,

    "answer_lines": [
        {"answer": "crypto ipsec transform-set TSET esp-aes 256 esp-sha-hmac", 
        "level": cli.CONFIG,
        "hint": "Type sample to see the solution"},
    ]
    },
    {
    "question": """
    And now we need to cap it off with an IPsec profile to which we will tie the transform-set. Create a profile named PROF.
    """,

    "about": """
    PLACE DESCRIPTION HERE
    """,

    "sample": """
    crypto ipsec profile PROF
      set transform-set TSET
    """,

    "answer_lines": [
        {"answer": "crypto ipsec profile PROF", "level": cli.CONFIG, "hint": "cisco"},
        {"answer": "set transform-set TSET", "level": cli.CRYPTO_IPSEC_PROFILE, "hint": "cisco"},
    ]
    },
    {
    "question": """
    Now apply the IPsec profile to tunnel 42
    """,

    "about": """
    PLACE DESCRIPTION HERE
    """,

    "sample": """
    interface tunnel 42
      tunnel protection ipsec profile PROF
    """,

    "answer_lines": [
        {"answer": "interface tunnel 42", "level": cli.CONFIG, "hint": "we need to go to the interface level for tunnel 42"},
        {"answer": "tunnel protection ipsec profile PROF", "level": cli.CRYPTO_IPSEC_PROFILE, "hint": "apply the IPsec profile PROF"},
    ]
    },
]
