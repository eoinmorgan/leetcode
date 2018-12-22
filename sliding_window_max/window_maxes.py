from monoqueue import Monoqueue

def window_maxes(nums, window_size):
    if len(nums) == 0:
        return []

    mq = Monoqueue()
    maxes = []

    for i in range(window_size-1):
        mq.push(nums[i])

    for i in range(window_size-1, len(nums)):
        mq.push(nums[i])
        maxes.append(mq.front())
        mq.pop(nums[i - window_size + 1])

    return maxes