import config_levels as cli

questions = [
        {
        "question": "How do you configure ip sla 10",

        "about": "ip sla 10",

        "answer_lines": [
                {
                "answer": "ip sla 10",
                "indention": "0",
                "level": cli.CONFIG,
                "hint": "ip sla 10",
                },
                {
                "answer": "icmp-echo 1.3.1.3 source-ip 1.3.1.1",
                "indention": "1",
                "level": cli.CONFIG,
                "hint": "icmp-echo 1.3.1.3 source-ip 1.3.1.1",
                },
                {
                "answer": "frequency 30",
                "indention": "1",
                "level": cli.CONFIG,
                "hint": "frequency 30",
                },
        ],

        "sample":
"""
ip sla 10
 icmp-echo 1.3.1.3 source-ip 1.3.1.1
 frequency 30
""",
        },
        {
        "question": "How do you configure ip sla schedule 10 life forever start-time now",

        "about": "ip sla schedule 10 life forever start-time now",

        "answer_lines": [
                {
                "answer": "ip sla schedule 10 life forever start-time now",
                "indention": "0",
                "level": cli.CONFIG,
                "hint": "ip sla schedule 10 life forever start-time now",
                },
        ],

        "sample":
"""
ip sla schedule 10 life forever start-time now
""",
        },
        {
        "question": "How do you configure track 123 ip sla 10 reachability",

        "about": "track 123 ip sla 10 reachability",

        "answer_lines": [
                {
                "answer": "track 123 ip sla 10 reachability",
                "indention": "0",
                "level": cli.CONFIG,
                "hint": "track 123 ip sla 10 reachability",
                },
                {
                "answer": "delay down 65 up 180",
                "indention": "1",
                "level": cli.CONFIG,
                "hint": "delay down 65 up 180",
                },
        ],

        "sample":
"""
track 123 ip sla 10 reachability
 delay down 65 up 180
""",
        },
        {
        "question": "How do you configure track 124 interface g0/1 line-protocol",

        "about": "track 124 interface g0/1 line-protocol",

        "answer_lines": [
                {
                "answer": "track 124 interface g0/1 line-protocol",
                "indention": "0",
                "level": cli.CONFIG,
                "hint": "track 124 interface g0/1 line-protocol",
                },
                {
                "answer": "delay down 1 up 180",
                "indention": "1",
                "level": cli.CONFIG,
                "hint": "delay down 1 up 180",
                },
        ],

        "sample":
"""
track 124 interface g0/1 line-protocol
 delay down 1 up 180
""",
        },
        {
        "question": "How do you configure track 125 list threshold weight",

        "about": "track 125 list threshold weight",

        "answer_lines": [
                {
                "answer": "track 125 list threshold weight",
                "indention": "0",
                "level": cli.CONFIG,
                "hint": "track 125 list threshold weight",
                },
                {
                "answer": "object 123 weight 50",
                "indention": "1",
                "level": cli.CONFIG,
                "hint": "object 123 weight 50",
                },
                {
                "answer": "object 124 weight 50",
                "indention": "1",
                "level": cli.CONFIG,
                "hint": "object 124 weight 50",
                },
                {
                "answer": "threshold weight up 51 down 50",
                "indention": "1",
                "level": cli.CONFIG,
                "hint": "threshold weight up 51 down 50",
                },
                {
                "answer": "delay down 1 up 180",
                "indention": "1",
                "level": cli.CONFIG,
                "hint": "delay down 1 up 180",
                },
        ],

        "sample":
"""
track 125 list treshold weight
 object 123 weight 50
 object 124 weight 50
 threshold weight up 51 down 50
 delay down 1 up 180
""",
        },
        {
        "question": "How do you configure ip route 0.0.0.0 0.0.0.0 1.3.1.3 name default track 125",

        "about": "ip route 0.0.0.0 0.0.0.0 1.3.1.3 name default track 125",

        "answer_lines": [
                {
                "answer": "ip route 0.0.0.0 0.0.0.0 1.3.1.3 name default track 125",
                "indention": "0",
                "level": cli.CONFIG,
                "hint": "ip route 0.0.0.0 0.0.0.0 1.3.1.3 name default track 125",
                },
        ],

        "sample":
"""
ip route 0.0.0.0 0.0.0.0 1.3.1.3 name default track 125
""",
        },
        {
        "question": "How do you configure ip access-list extended IP-SLA",

        "about": "ip access-list extended IP-SLA",

        "answer_lines": [
                {
                "answer": "ip access-list extended IP-SLA",
                "indention": "0",
                "level": cli.CONFIG,
                "hint": "ip access-list extended IP-SLA",
                },
                {
                "answer": "permit ip any host 1.3.1.3",
                "indention": "1",
                "level": cli.CONFIG,
                "hint": "permit ip any host 1.3.1.3",
                },
        ],

        "sample":
"""
ip access-list extended IP-SLA
 permit ip any host 1.3.1.3
""",
        },
        {
        "question": "How do you configure route-map ROUTING-SLA permit 10",

        "about": "route-map ROUTING-SLA permit 10",

        "answer_lines": [
                {
                "answer": "route-map ROUTING-SLA permit 10",
                "indention": "0",
                "level": cli.CONFIG,
                "hint": "route-map ROUTING-SLA permit 10",
                },
                {
                "answer": "match ip address IP-SLA",
                "indention": "1",
                "level": cli.CONFIG,
                "hint": "match ip address IP-SLA",
                },
                {
                "answer": "set ip next-hop 1.3.1.3",
                "indention": "1",
                "level": cli.CONFIG,
                "hint": "set ip next-hop 1.3.1.3",
                },
                {
                "answer": "set interface Null0",
                "indention": "1",
                "level": cli.CONFIG,
                "hint": "set interface Null0",
                },
        ],

        "sample":
"""
route-map ROUTING-SLA permit 10
 match ip address IP-SLA
 set ip next-hop 1.3.1.3
 set interface Null0
""",
        },
        {
        "question": "How do you configure ip local policy route-map ROUTING-SLA",

        "about": "ip local policy route-map ROUTING-SLA",

        "answer_lines": [
                {
                "answer": "ip local policy route-map ROUTING-SLA",
                "indention": "0",
                "level": cli.CONFIG,
                "hint": "ip local policy route-map ROUTING-SLA",
                },
        ],

        "sample":
"""
ip local policy route-map ROUTING-SLA
""",
        },
        {
        "question": "How do you configure ip prefix-list DEFAULT seq 10 permit 0.0.0.0/0",

        "about": "ip prefix-list DEFAULT seq 10 permit 0.0.0.0/0",

        "answer_lines": [
                {
                "answer": "ip prefix-list DEFAULT seq 10 permit 0.0.0.0/0",
                "indention": "0",
                "level": cli.CONFIG,
                "hint": "ip prefix-list DEFAULT seq 10 permit 0.0.0.0/0",
                },
        ],

        "sample":
"""
ip prefix-list DEFAULT seq 10 permit 0.0.0.0/0
""",
        },
        {
        "question": "How do you configure route-map STATIC-TO-EIGRP permit 10",

        "about": "route-map STATIC-TO-EIGRP permit 10",

        "answer_lines": [
                {
                "answer": "route-map STATIC-TO-EIGRP permit 10",
                "indention": "0",
                "level": cli.CONFIG,
                "hint": "route-map STATIC-TO-EIGRP permit 10",
                },
                {
                "answer": "match ip address prefix DEFAULT",
                "indention": "1",
                "level": cli.CONFIG,
                "hint": "match ip address prefix DEFAULT",
                },
        ],

        "sample":
"""
route-map STATIC-TO-EIGRP permit 10
 match ip address prefix DEFAULT
""",
        },
        {
        "question": "How do you configure router eigrp 42",

        "about": "router eigrp 42",

        "answer_lines": [
                {
                "answer": "router eigrp 42",
                "indention": "0",
                "level": cli.CONFIG,
                "hint": "router eigrp 42",
                },
                {
                "answer": "redistribute static route-map STATIC-TO-EIGRP",
                "indention": "1",
                "level": cli.CONFIG,
                "hint": "redistribute static route-map STATIC-TO-EIGRP",
                },
        ],

        "sample":
"""
router eigrp 42
 redistribute static route-map STATIC-TO-EIGRP
""",
        },
        {
        "question": "How do you configure ip route 0.0.0.0 0.0.0.0 2.3.2.3 name default 171",

        "about": "ip route 0.0.0.0 0.0.0.0 2.3.2.3 name default 171",

        "answer_lines": [
                {
                "answer": "ip route 0.0.0.0 0.0.0.0 2.3.2.3 name default 171",
                "indention": "0",
                "level": cli.CONFIG,
                "hint": "ip route 0.0.0.0 0.0.0.0 2.3.2.3 name default 171",
                },
        ],

        "sample":
"""
ip route 0.0.0.0 0.0.0.0 2.3.2.3 name default 171
""",
        },
        {
        "question": "How do you configure ip prefix-list DEFAULT seq 10 permit 0.0.0.0/0",

        "about": "ip prefix-list DEFAULT seq 10 permit 0.0.0.0/0",

        "answer_lines": [
                {
                "answer": "ip prefix-list DEFAULT seq 10 permit 0.0.0.0/0",
                "indention": "0",
                "level": cli.CONFIG,
                "hint": "ip prefix-list DEFAULT seq 10 permit 0.0.0.0/0",
                },
        ],

        "sample":
"""
ip prefix-list DEFAULT seq 10 permit 0.0.0.0/0
""",
        },
        {
        "question": "How do you configure route-map STATIC-TO-EIGRP permit 10",

        "about": "route-map STATIC-TO-EIGRP permit 10",

        "answer_lines": [
                {
                "answer": "route-map STATIC-TO-EIGRP permit 10",
                "indention": "0",
                "level": cli.CONFIG,
                "hint": "route-map STATIC-TO-EIGRP permit 10",
                },
                {
                "answer": "match ip address prefix-list DEFAULT",
                "indention": "1",
                "level": cli.CONFIG,
                "hint": "match ip address prefix-list DEFAULT",
                },
        ],

        "sample":
"""
route-map STATIC-TO-EIGRP permit 10
 match ip address prefix-list DEFAULT
""",
        },
        {
        "question": "How do you configure router eigrp 42",

        "about": "router eigrp 42",

        "answer_lines": [
                {
                "answer": "router eigrp 42",
                "indention": "0",
                "level": cli.CONFIG,
                "hint": "router eigrp 42",
                },
                {
                "answer": "redistribute static route-map STATIC-TO-EIGRP",
                "indention": "1",
                "level": cli.CONFIG,
                "hint": "redistribute static route-map STATIC-TO-EIGRP",
                },
        ],

        "sample":
"""
router eigrp 42
 redistribute static route-map STATIC-TO-EIGRP
""",
        },
]