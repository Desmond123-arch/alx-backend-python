#!/usr/bin/env python3
""" Execute multiple coroutines"""

import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """ Calls wait_random n times"""
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    vals = [await task for task in asyncio.as_completed(tasks)]
    return vals
