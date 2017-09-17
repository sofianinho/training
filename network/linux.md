# Linux networking
A vast topic. This documentation only covers some of the basics, the rest is given as biblioographic pointers

## Important files
Everything is a file in Linux. But not all files are created equal. In particular, the files that contain configuration and information about the system are more sensitive. Protections against misconfiguration, such as read-only filesystems, root-only ownership, and more are there to keep the system in a coherent state. We are focusing on the files that manage network configuration and show network statistics. The Linux kernel considered is beyond version 2.6. 

### The /proc filesystem
It is a virtual filesystem that keeps live information about process-related activities. It contains runtime system configuration (memory, network, hardware) and current running processes each in a separate numbered folder. Examining each folder/file is out of scope. Many programs provided by default with the GNU/Linux are wrappers around these files that show the content and update the configuration if requested.

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
We can see that the `ip route` utility has taken the content of the previous file and converted the IP addresses and prefixes to decimal from hexadecimal for our liking and readbility.

- `/proc/sys/net` is the source of information and configuration for the kernel without recompilation or reboot. This folder contains the part related to the networking part. 
```
bridge  core  ipv4  ipv6  netfilter  nf_conntrack_max  unix
```
For instance, the content of the IPv6 folder is:
```
anycast_src_echo_reply     conf                    idgen_delay              ip6frag_time      route
auto_flowlabels            flowlabel_consistency   idgen_retries            ip_nonlocal_bind  xfrm6_gc_thresh
bindv6only                 flowlabel_state_ranges  ip6frag_high_thresh      mld_max_msf
calipso_cache_bucket_size  fwmark_reflect          ip6frag_low_thresh       mld_qrv
calipso_cache_enable       icmp                    ip6frag_secret_interval  neigh
```
You can disable the IPv6 protocol on the whole system, by putting 1 in the file `/proc/sys/net/ipv6/conf/all/disable_ipv6` 

### The /sys filesystem (sysfs)
It is an interface to the kernel and contains information about hardware, network interfaces, bus ...etc. More formally:
```
From: https://www.kernel.org/doc/Documentation/filesystems/sysfs.txt

sysfs is a ram-based filesystem initially based on ramfs. It provides
a means to export kernel data structures, their attributes, and the 
linkages between them to userspace.
```
The networking part of this filesystem is under `/sys/class/net` where you find information about your interfaces: wireless or not, driver used, mtu, up or down ...
This information is presented in user friendly way by tools like `ifconfig` and `ip addr`
