import config_levels as cli

questions = [
        {
        "question": "Go ahead and make sure IP CEF is on. We need it for NetFlow",

        "about": "ip cef",

        "answer_lines": [
                {
                "answer": "ip cef",
                "indention": "0",
                "level": cli.CONFIG,
                "hint": "ip cef",
                },
        ],

        "sample":
"""
ip cef
""",
        },
        {
        "question": "Configure TnF with a 5 minute timeout for active flows:",

        "about": "ip flow-cache timeout active 5",

        "answer_lines": [
                {
                "answer": "ip flow-cache timeout active 5",
                "indention": "0",
                "level": cli.CONFIG,
                "hint": "ip flow-cache timeout active 5",
                },
        ],

        "sample":
"""
ip flow-cache timeout active 5
""",
        },
        {
        "question": "Configure TnF with a 30 second timeout for inactive flows:",

        "about": "ip flow-cache timeout inactive 30",

        "answer_lines": [
                {
                "answer": "ip flow-cache timeout inactive 30",
                "indention": "0",
                "level": cli.CONFIG,
                "hint": "ip flow-cache timeout inactive 30",
                },
        ],

        "sample":
"""
ip flow-cache timeout inactive 30
""",
        },
        {
        "question": "Go to interface g0/0 and turn on TnF",

        "about": "interface g0/0",

        "answer_lines": [
                {
                "answer": "interface g0/0",
                "indention": "0",
                "level": cli.CONFIG,
                "hint": "interface g0/0",
                },
                {
                "answer": "ip flow ingress",
                "indention": "1",
                "level": cli.CONFIG,
                "hint": "ip flow ingress",
                },
        ],

        "sample":
"""
interface g0/0
 ip flow ingress
""",
        },
        {
        "question": "Now run 'show ip flow interface'",

        "about": "show ip flow interface",

        "answer_lines": [
                {
                "answer": "show ip flow interface",
                "indention": "0",
                "level": cli.CONFIG,
                "hint": "show ip flow interface",
                },
        ],

        "sample":
"""
show ip flow interface
""",
        },
        {
        "question": "How do you configure show ip cache flow",

        "about": "show ip cache flow",

        "answer_lines": [
                {
                "answer": "show ip cache flow",
                "indention": "0",
                "level": cli.CONFIG,
                "hint": "show ip cache flow",
                },
        ],

        "sample":
"""
show ip cache flow
""",
        },
        {
        "question": "How do you configure show ip cache verbose flow",

        "about": "show ip cache verbose flow",

        "answer_lines": [
                {
                "answer": "show ip cache verbose flow",
                "indention": "0",
                "level": cli.CONFIG,
                "hint": "show ip cache verbose flow",
                },
        ],

        "sample":
"""
show ip cache verbose flow
""",
        },
        {
        "question": "How do you configure netflow-original can only be used for ingress flows",

        "about": "netflow-original can only be used for ingress flows",

        "answer_lines": [
                {
                "answer": "netflow-original can only be used for ingress flows",
                "indention": "0",
                "level": cli.CONFIG,
                "hint": "netflow-original can only be used for ingress flows",
                },
        ],

        "sample":
"""
netflow-original can only be used for ingress flows
""",
        },
        {
        "question": "Now it's time to configure FnF. How do you configure flow monitor BUNNY using the default record 'netflow-original'",

        "about": "flow monitor BUNNY",

        "answer_lines": [
                {
                "answer": "flow monitor BUNNY",
                "indention": "0",
                "level": cli.CONFIG,
                "hint": "flow monitor BUNNY",
                },
                {
                "answer": "record netflow-original",
                "indention": "1",
                "level": cli.CONFIG,
                "hint": "record netflow-original",
                },
        ],

        "sample":
"""
flow monitor BUNNY
 record netflow-original
""",
        },
        {
        "question": "Go to interface g0/0 and enable flow monitor BUNNY for ingress packets.",

        "about": "interface g0/0",

        "answer_lines": [
                {
                "answer": "interface g0/0",
                "indention": "0",
                "level": cli.CONFIG,
                "hint": "interface g0/0",
                },
                {
                "answer": "ip flow monitor BUNNY input",
                "indention": "1",
                "level": cli.CONFIG,
                "hint": "ip flow monitor BUNNY input",
                },
        ],

        "sample":
"""
interface g0/0
 ip flow monitor BUNNY input
""",
        },
        {
        "question": "How do you configure show flow monitor",

        "about": "show flow monitor",

        "answer_lines": [
                {
                "answer": "show flow monitor",
                "indention": "0",
                "level": cli.CONFIG,
                "hint": "show flow monitor",
                },
        ],

        "sample":
"""
show flow monitor
""",
        },
        {
        "question": "How do you configure show flow record netflow-original",

        "about": "show flow record netflow-original",

        "answer_lines": [
                {
                "answer": "show flow record netflow-original",
                "indention": "0",
                "level": cli.CONFIG,
                "hint": "show flow record netflow-original",
                },
        ],

        "sample":
"""
show flow record netflow-original
""",
        },
        {
        "question": "Create your own flow record, BUNNY-RECORD.",

        "about": "flow record BUNNY-RECORD",

        "answer_lines": [
                {
                "answer": "flow record BUNNY-RECORD",
                "indention": "0",
                "level": cli.CONFIG,
                "hint": "flow record BUNNY-RECORD",
                },
                {
                "answer": "description BUNNY-STUFF",
                "indention": "1",
                "level": cli.CONFIG,
                "hint": "description BUNNY-STUFF",
                },
                {
                "answer": "match ipv4 destination address",
                "indention": "1",
                "level": cli.CONFIG,
                "hint": "match ipv4 destination address",
                },
                {
                "answer": "match transport tcp destination-port",
                "indention": "1",
                "level": cli.CONFIG,
                "hint": "match transport tcp destination-port",
                },
                {
                "answer": "match transport udp destination-port",
                "indention": "1",
                "level": cli.CONFIG,
                "hint": "match transport udp destination-port",
                },
                {
                "answer": "collect counter packets",
                "indention": "1",
                "level": cli.CONFIG,
                "hint": "collect counter packets",
                },
                {
                "answer": "collect timestamp absolute first",
                "indention": "1",
                "level": cli.CONFIG,
                "hint": "collect timestamp absolute first",
                },
        ],

        "sample":
"""
flow record BUNNY-RECORD
 description BUNNY-STUFF
 match ipv4 destination address
 match transport tcp destination-port
 match transport udp destination-port
 collect counter packets
 collect timestamp absolute first
""",
        },
        {
        "question": "How do you configure flow monitor BUNNY-MONITOR",

        "about": "flow monitor BUNNY-MONITOR",

        "answer_lines": [
                {
                "answer": "flow monitor BUNNY-MONITOR",
                "indention": "0",
                "level": cli.CONFIG,
                "hint": "flow monitor BUNNY-MONITOR",
                },
                {
                "answer": "record BUNNY-RECORD",
                "indention": "1",
                "level": cli.CONFIG,
                "hint": "record BUNNY-RECORD",
                },
        ],

        "sample":
"""
flow monitor BUNNY-MONITOR
 record BUNNY-RECORD
""",
        },
        {
        "question": "How do you configure interface gigabitEthernet0/0",

        "about": "interface gigabitEthernet0/0",

        "answer_lines": [
                {
                "answer": "interface gigabitEthernet0/0",
                "indention": "0",
                "level": cli.CONFIG,
                "hint": "interface gigabitEthernet0/0",
                },
                {
                "answer": "ip flow monitor BUNNY-MONITOR input",
                "indention": "1",
                "level": cli.CONFIG,
                "hint": "ip flow monitor BUNNY-MONITOR input",
                },
        ],

        "sample":
"""
interface gigabitEthernet0/0
 ip flow monitor BUNNY-MONITOR input
""",
        },
]