# Linux networking
A vast topic. This documentation only covers some of the basics, the rest is given as biblioographic pointers

## Important files
Everything is a file in Linux. But not all files are created equal. In particular, the files that contain configuration and information about the system are more sensitive. Protections against misconfiguration, such as read-only filesystems, root-only ownership, and more are there to keep the system in a coherent state. We are focusing on the files that manage network configuration and show network statistics. The Linux kernel considered is beyond version 2.6. 

### The /proc filesystem
It is a virtual filesystem that keeps live information about process-related activities. It contains runtime system configuration (memory, network, hardware) and current running processes each in a separate numbered folder. Examining each folder/file is out of scope. 

- `/proc/net` contains status information about network protocols. For example, for my system (Linux 4.10.0-32-generic #36~16.04.1-Ubuntu SMP Wed Aug 9 09:19:02 UTC 2017 x86_64 x86_64 x86_64 GNU/Linux), here is the content: 
```
anycast6   dev_snmp6     icmp6          ip6_mr_cache       ip_tables_names    mcfilter6  protocols  route      snmp          stat  udplite
arp        fib_trie      if_inet6       ip6_mr_vif         ip_tables_targets  netfilter  psched     rt6_stats  snmp6         tcp   udplite6
connector  fib_triestat  igmp           ip_mr_cache        ipv6_route         netlink    ptype      rt_acct    sockstat      tcp6  unix
dev        hci           igmp6          ip_mr_vif          l2cap              netstat    raw        rt_cache   sockstat6     udp   wireless
dev_mcast  icmp          ip6_flowlabel  ip_tables_matches  mcfilter           packet     raw6       sco        softnet_stat  udp6  xfrm_stat
```
The _route_ file content is:
```
face   Destination     Gateway         Flags   RefCnt  Use     Metric  Mask            MTU     Window  IRTT                                   
eno1    00000000        0167C00A        0003    0       0       0       00000000        0       0      0                                      
eno1    0067C00A        00000000        0001    0       0       0       00FFFFFF        0       0      0                                      
docker0 000011AC        00000000        0001    0       0       0       0000FFFF        0       0      0    
```

- `/proc/sys/net`

### The /sys filesystem
