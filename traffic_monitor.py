import psutil
import time
import random

USE_TEST_MODE = False
CURRENT_MODE = "normal"
SWITCH_COUNTER = 0
SWITCH_EVERY = random.randint(3, 7)  # каждые 3-7 вызовов меняем режим

def set_mode(test_mode):
    global USE_TEST_MODE
    USE_TEST_MODE = test_mode

def get_traffic_stats():
    global CURRENT_MODE, SWITCH_COUNTER, SWITCH_EVERY

    if USE_TEST_MODE:
        SWITCH_COUNTER += 1
        if SWITCH_COUNTER >= SWITCH_EVERY:
            # Переключаем режим
            CURRENT_MODE = "attack" if CURRENT_MODE == "normal" else "normal"
            SWITCH_COUNTER = 0
            SWITCH_EVERY = random.randint(3, 7)

        # Возвращаем симулированный трафик
        if CURRENT_MODE == "normal":
            packets = random.randint(100, 250)
        else:
            packets = random.randint(400, 800)

        return {
            "bytes_recv": packets * 100,
            "packets_recv": packets
        }

    # Реальный режим
    net1 = psutil.net_io_counters()
    time.sleep(1)
    net2 = psutil.net_io_counters()

    bytes_recv = net2.bytes_recv - net1.bytes_recv
    packets_recv = net2.packets_recv - net1.packets_recv

    return {
        "bytes_recv": bytes_recv,
        "packets_recv": packets_recv
    }

def get_current_mode():
    return "test" if USE_TEST_MODE else "real"
