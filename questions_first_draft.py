import config_levels as cli

questions = [
    {
    "question": """
    Please create a policy for ISAKMP. Policy Number 10. The ISAKMP policy shoud use AES for encryption,
    Diffie-Hellmen group 5, and something just slightly more secure than MD5 for hashing. The password will be cisco.
    Type 'Hint' for a clue.\n
    """,

    "about": """
    ISAKMP stands for the INTERNET SECURITY AND KEY MANAGEMENT PROTOCOL. It builds two tunnels.
    The first tunnel is the IKE tunnel. Here we are practicing IKEv1. We will then use this tunnel
    to build the IPsec tunnel itself, the second tunnel. The ISAKMP POLICY should contain:
    
    H -> Hash: make sure the data hasn't been changed or corrupted.
    A -> Authention: make sure the peer is really who they say they are.
    G -> Group: used to negotiate keys between the peers.
    L -> Lifetime: cisco provides a default of 24 hours.
    E -> Encryption: encrypt the data for secrecy.
    
    A tunnel can also be referred to as an SA (Security Assocation) and
    you will see this in troubleshooting. Really, it's the two tunnels/SAs
    together that we think of when we talk about the IPsec connection.
    
    You can have multiple policies on a device. They will be processed
    starting from the lowest first until a match is found or all options
    have been exhausted.

    P.S. It's a good idea to start at 10 and not 1 in case you need
    to add an more-preferred policy later.
    
    Brief:
    IKEv1 -> SA 1, used for management of the tunnels between the routers.
    IPsec -> SA 2, used to send the client data.
    
    You need both tunnels to form the IPsec tunnel used for sharing client data.
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
          "hint": "You need to create a policy for isakmp. It should be #10. Follow the order in the 'sample"
        },
        {
          "answer": "authentication pre-share",
          "level": cli.CONFIG_ISAKMP,
          "hint": "We're going to use a password",
          "about": """Options are: pre-share, rsa-encr, and rsa-sig.
          Pre-share is for shared passwords. RSA-SIG uses digital certificates
          and PKI trustpoints. We are going to use a password, i.e. pre-share,
          in this module."""
        },
        {
          "answer": "encryption aes",
          "level": cli.CONFIG_ISAKMP,
          "hint": "We want to use AES for this module",
          "about": """
          AES stands for the Advanced Encryption Standard. It replaces the
          older DES (Data Encryption Standard) and 3 DES, both of which are
          not considered secure. We can use a 128, 192, or 256 bit key with AES.
          The larger the key, the stronger the encryption, but this also means
          more work for the CPU. Security will need to be balanced with performance
          based on business needs.
          """
          
        },
        {
        "answer": "hash sha",
        "level": cli.CONFIG_ISAKMP,
        "hint": "Hashing will be SHA",
        "about": """
        Hashes ensure that the our data has not been changed mid-stream. That we send
        someone $100, no one can add any extra 0s. Options include MD5 (Message Digest 5),
        SHA (Secure Hashing Algorithm), and SHA 2 (SHA256, SHA2384, SHA512). SHA 2 should
        be used for security in the real world, but this example uses SHA, that's just plan
        SHA 1."""
        },
        {
        "answer": "group 5",
        "level": cli.CONFIG_ISAKMP,
        "hint": "We want to use Diffie-Hellmen group 5",
        "about": """
        Diffie-Hellmen, configured with the "group" keyword, is used by
        isakmp to create the shared keys that will be used for encryption.
        They are assigned with numbers, with higher numbers being newer and
        providing more security.
        """
        },
    ]
    },

    {
    "question": """
    You will now need to configure the password itself. Remember, it will be "cisco"
    The neighbor is going to be 20.30.20.30. You can still type "hint" for a hint, or "sample" for an example.\n\n\n""",

    "about": """
    We don't configure the ISAKMP key/password under the policy directly, but
    here with this configuration-level command. We use the neighbor statement
    to limit who we use the key with, but we can also take advantage of a quad-zero
    address to use the password with anyone. No-xauth prevents the router from
    prompting the peer for Xauth information (username and password). This would
    cause issues if the crypto map was used for both router-to-router IPsec and
    client-to-IOS IPsec.
    """,

    "sample": """
    crypto isakmp key cisco neighbor 20.30.20.30 no-xauth
    """,

    "answer_lines": [
        {
        "answer": "crypto isakmp key cisco neighbor 20.30.20.30 no-xauth", 
        "level": cli.CONFIG,
        "hint": "Setup the password cisco for neighbor 20.30.20.30. Type 'sample' if you want to see how to do it."}
    ]
    },
    {
    "question": """
    Up next is setting up the transform-set. This is for Phase II negotiation
    for the IPsec tunnel. We're going to use ESP with aes 256 and sha hmac. This
    will use 'tunnel mode' which is the default. Name your transform-set TSET.
    Remember you can type 'sample' to see the solution and 'about' for more info
    on the subject. Using 'about' is highly recommended the first time learning 
    about a subject!\n
    """,

    "about": """
    This is for phase II of ISAKMP, the so-called IPSEC tunnel itself. This is the tunnel
    that the router will use to send client data.
    
    We don't just set an encryption method and hashing algorithm here. We also decide
    between AH (Authentication Header) and ESP (Encapsulating Security Payload). AH is very
    rarely used as it does not provide encryption. You'll mostly see ESP.
    
    ESP is IP protocol 50. AH is IP protocol 51.
    
    HMAC stands for Hashed Message Authentication Code. It adds a shared
    key prior to hashing the payload. This can help prevent man-in-the-middle
    attacks. Otherwise, our hashing options are the same.
    """,

    "sample": """
    crypto ipsec transform-set TSET esp-aes 256 esp-sha-hmac
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
        {"answer": "set transform-set TSET", "level": cli.IPSEC_PROFILE, "hint": "cisco"},
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
        {"answer": "tunnel protection ipsec profile PROF", "level": cli.IPSEC_PROFILE, "hint": "apply the IPsec profile PROF"},
    ]
    },
]
