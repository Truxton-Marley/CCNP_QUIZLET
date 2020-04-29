import config_levels as cli

questions = [
        {
        "question": "How do you configure ip sla 20",

        "about": "ip sla 20",

        "answer_lines": [
                {
                "answer": "ip sla 20",
                "indention": "0",
                "level": cli.CONFIG,
                "hint": "ip sla 20",
                },
                {
                "answer": "icmp-echo 1.3.1.3 source-ip 1.3.1.1",
                "indention": "1",
                "level": cli.CONFIG,
                "hint": "icmp-echo 1.3.1.3 source-ip 1.3.1.1",
                },
                {
                "answer": "frequency 10",
                "indention": "1",
                "level": cli.CONFIG,
                "hint": "frequency 10 <----measured in seconds",
                },
        ],

        "sample":
"""
ip sla 20
 icmp-echo 1.3.1.3 source-ip 1.3.1.1
 frequency 10 <----measured in seconds
""",
        },
        {
        "question": "How do you configure ip sla schedule 20 life forever start-time now",

        "about": "ip sla schedule 20 life forever start-time now",

        "answer_lines": [
                {
                "answer": "ip sla schedule 20 life forever start-time now",
                "indention": "0",
                "level": cli.CONFIG,
                "hint": "ip sla schedule 20 life forever start-time now",
                },
        ],

        "sample":
"""
ip sla schedule 20 life forever start-time now
""",
        },
        {
        "question": "How do you configure access-list 101 permit ip host 4.4.4.4 host 5.5.5.5",

        "about": "access-list 101 permit ip host 4.4.4.4 host 5.5.5.5",

        "answer_lines": [
                {
                "answer": "access-list 101 permit ip host 4.4.4.4 host 5.5.5.5",
                "indention": "0",
                "level": cli.CONFIG,
                "hint": "access-list 101 permit ip host 4.4.4.4 host 5.5.5.5",
                },
        ],

        "sample":
"""
access-list 101 permit ip host 4.4.4.4 host 5.5.5.5
""",
        },
        {
        "question": "How do you configure route-map PBR permit 10",

        "about": "route-map PBR permit 10",

        "answer_lines": [
                {
                "answer": "route-map PBR permit 10",
                "indention": "0",
                "level": cli.CONFIG,
                "hint": "route-map PBR permit 10",
                },
                {
                "answer": "match address 101",
                "indention": "1",
                "level": cli.CONFIG,
                "hint": "match address 101",
                },
                {
                "answer": "set ip next-hop 1.3.1.3",
                "indention": "1",
                "level": cli.CONFIG,
                "hint": "set ip next-hop 1.3.1.3",
                },
        ],

        "sample":
"""
route-map PBR permit 10
 match address 101
 match ip next-hop 1.3.1.3
""",
        },
        {
        "question": "How do you configure interface g0/0",

        "about": "interface g0/0",

        "answer_lines": [
                {
                "answer": "interface g0/0",
                "indention": "0",
                "level": cli.CONFIG,
                "hint": "interface g0/0",
                },
                {
                "answer": "ip policy route-map PBR",
                "indention": "1",
                "level": cli.CONFIG,
                "hint": "ip policy route-map PBR",
                },
        ],

        "sample":
"""
interface g0/0
 ip policy route-map PBR
""",
        },
        {
        "question": "How do you configure show ip sla configuration",

        "about": "show ip sla configuration",

        "answer_lines": [
                {
                "answer": "show ip sla configuration",
                "indention": "0",
                "level": cli.CONFIG,
                "hint": "show ip sla configuration",
                },
        ],

        "sample":
"""
show ip sla configuration
""",
        },
        {
        "question": "How do you configure show ip sla statistics",

        "about": "show ip sla statistics",

        "answer_lines": [
                {
                "answer": "show ip sla statistics",
                "indention": "0",
                "level": cli.CONFIG,
                "hint": "show ip sla statistics",
                },
        ],

        "sample":
"""
show ip sla statistics
""",
        },
        {
        "question": "How do you configure track 99 ip sla 20",

        "about": "track 99 ip sla 20",

        "answer_lines": [
                {
                "answer": "track 99 ip sla 20",
                "indention": "0",
                "level": cli.CONFIG,
                "hint": "track 99 ip sla 20",
                },
                {
                "answer": "delay down 60 up 180",
                "indention": "1",
                "level": cli.CONFIG,
                "hint": "delay down 60 up 180",
                },
        ],

        "sample":
"""
track 99 ip sla 20
 delay down 60 up 180
""",
        },
        {
        "question": "How do you configure ip route 0.0.0.0 0 0.0.0.0 1.3.1.3 name default track 99",

        "about": "ip route 0.0.0.0 0 0.0.0.0 1.3.1.3 name default track 99",

        "answer_lines": [
                {
                "answer": "ip route 0.0.0.0 0 0.0.0.0 1.3.1.3 name default track 99",
                "indention": "0",
                "level": cli.CONFIG,
                "hint": "ip route 0.0.0.0 0 0.0.0.0 1.3.1.3 name default track 99",
                },
        ],

        "sample":
"""
ip route 0.0.0.0 0 0.0.0.0 1.3.1.3 name default track 99
""",
        },
        {
        "question": "How do you configure route-map PBR permit 10",

        "about": "route-map PBR permit 10",

        "answer_lines": [
                {
                "answer": "route-map PBR permit 10",
                "indention": "0",
                "level": cli.CONFIG,
                "hint": "route-map PBR permit 10",
                },
                {
                "answer": "match address 101",
                "indention": "1",
                "level": cli.CONFIG,
                "hint": "match address 101",
                },
                {
                "answer": "match ip next-hop verify-availability 1.3.1.3 10 track 99",
                "indention": "1",
                "level": cli.CONFIG,
                "hint": "match ip next-hop verify-availability 1.3.1.3 10 track 99",
                },
        ],

        "sample":
"""
route-map PBR permit 10
 match address 101
 match ip next-hop verify-availability 1.3.1.3 10 track 99
""",
        },
        {
        "question": "How do you configure show ip policy",

        "about": "show ip policy",

        "answer_lines": [
                {
                "answer": "show ip policy",
                "indention": "0",
                "level": cli.CONFIG,
                "hint": "show ip policy",
                },
        ],

        "sample":
"""
show ip policy
""",
        },
        {
        "question": "How do you configure show track",

        "about": "show track",

        "answer_lines": [
                {
                "answer": "show track",
                "indention": "0",
                "level": cli.CONFIG,
                "hint": "show track",
                },
        ],

        "sample":
"""
show track
""",
        },
]