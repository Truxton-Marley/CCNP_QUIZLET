R1 = {
  "show_ip_interface_brief":
  """
  
R1#show ip int br
Interface                  IP-Address      OK? Method Status                Protocol
GigabitEthernet0/0         unassigned      YES unset  administratively down down    
GigabitEthernet0/1         1.20.1.1        YES manual up                    up      
GigabitEthernet0/2         1.10.1.1        YES manual up                    up      
Loopback1                  1.1.1.1         YES manual up                    up      
Tunnel42                   42.42.42.1      YES manual up                    up   

  """,
  
  "show_ip_route":
  """
  
R1#show ip route
Codes: L - local, C - connected, S - static, R - RIP, M - mobile, B - BGP
       D - EIGRP, EX - EIGRP external, O - OSPF, IA - OSPF inter area 
       N1 - OSPF NSSA external type 1, N2 - OSPF NSSA external type 2
       E1 - OSPF external type 1, E2 - OSPF external type 2
       i - IS-IS, su - IS-IS summary, L1 - IS-IS level-1, L2 - IS-IS level-2
       ia - IS-IS inter area, * - candidate default, U - per-user static route
       o - ODR, P - periodic downloaded static route, H - NHRP, l - LISP
       a - application route
       + - replicated route, % - next hop override, p - overrides from PfR

Gateway of last resort is 1.20.1.20 to network 0.0.0.0

S*    0.0.0.0/0 [1/0] via 1.20.1.20
      1.0.0.0/8 is variably subnetted, 5 subnets, 2 masks
C        1.1.1.1/32 is directly connected, Loopback1
C        1.10.1.0/24 is directly connected, GigabitEthernet0/2
L        1.10.1.1/32 is directly connected, GigabitEthernet0/2
C        1.20.1.0/24 is directly connected, GigabitEthernet0/1
L        1.20.1.1/32 is directly connected, GigabitEthernet0/1
      20.0.0.0/32 is subnetted, 1 subnets
S        20.30.20.30 [1/0] via 1.20.1.20
      42.0.0.0/8 is variably subnetted, 2 subnets, 2 masks
C        42.42.42.0/24 is directly connected, Tunnel42
L        42.42.42.1/32 is directly connected, Tunnel42
  """,
  
  "show cdp neighbors":
  """
  
R1#show cdp neighbors 
Capability Codes: R - Router, T - Trans Bridge, B - Source Route Bridge
                  S - Switch, H - Host, I - IGMP, r - Repeater, P - Phone, 
                  D - Remote, C - CVTA, M - Two-port Mac Relay 

Device ID        Local Intrfce     Holdtme    Capability  Platform  Port ID
CLIENT           Gig 0/2           130              R B             Gig 0/1
INTERNET         Gig 0/1           134              R B             Gig 0/1
  """,
  
  "show arp": 

  """
R1#show arp      
Protocol  Address          Age (min)  Hardware Addr   Type   Interface
Internet  1.10.1.1                -   fa16.3e67.c28c  ARPA   GigabitEthernet0/2
Internet  1.10.1.10               0   fa16.3ed6.1666  ARPA   GigabitEthernet0/2
Internet  1.20.1.1                -   fa16.3e3f.e09a  ARPA   GigabitEthernet0/1
Internet  1.20.1.20             153   fa16.3e51.b67d  ARPA   GigabitEthernet0/1
  """
}
