#!/user/bin/env python3
# -*- coding: utf-8 -*-
#第一种方法(推荐)
import random
class Add_call():
    def random_str(self,slen):
        seed = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        sa = []
        for i in range(slen):
            sa.append(random.choice(seed))
        return ''.join(sa)
        # random_str(8)运行结果：l7VSbNEG


