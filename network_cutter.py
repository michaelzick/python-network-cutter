#!/usr/bin/env python3

import netfilterqueue

queue = netfilterqueue.NetfilterQueue()
queue.bind(0, process_packet)