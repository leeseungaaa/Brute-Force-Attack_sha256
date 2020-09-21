from sys import argv
from time import time
from functools import reduce
import hashlib
import itertools

TARGET_HASH = "78fe3f05768ff3a95c74ffafe366cc3474022d925ad5593af733bf8ac1ab0de6"                   
TARGET_LENGTH = 6                                                           

def timer(func):
    def wrapper(*args, **kwargs):
        timer_start = time()
        timer_return = func(*args, **kwargs)
        timer_diff = int(time()-timer_start)

        print("브루트포스 공격 완료")
        print("걸린 시간: {} 초".format(timer_diff))
              
        return timer_return
    return wrapper


@timer
def bruteforce():                                                         
    seed = "ketaonhisrdlumfcgwypbvxjqz"                     
    seed_bytes = list(map(ord, seed))

    attempts = 0
    for word_bytes in itertools.product(seed_bytes, repeat=TARGET_LENGTH):
        word_string = reduce(lambda x, y: x+y, map(chr, word_bytes)).encode("utf-8")        
        hash_ = hashlib.sha256(word_string).hexdigest()                    
                              
        if hash_ == TARGET_HASH:
            print("정답: %s " % (word_string))
            break

        attempts += 1


bruteforce()


