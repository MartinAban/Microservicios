from tenacity import retry, stop_after_attempt, wait_fixed, RetryError
import time

# Circuit Breaker simple
CIRCUIT_OPEN = False
CIRCUIT_OPEN_TIME = 0
CIRCUIT_TIMEOUT = 30  # segundos

def is_circuit_open():
    global CIRCUIT_OPEN, CIRCUIT_OPEN_TIME
    if CIRCUIT_OPEN and (time.time() - CIRCUIT_OPEN_TIME < CIRCUIT_TIMEOUT):
        return True
    else:
        CIRCUIT_OPEN = False
        return False

def open_circuit():
    global CIRCUIT_OPEN, CIRCUIT_OPEN_TIME
    CIRCUIT_OPEN = True
    CIRCUIT_OPEN_TIME = time.time()

# Decorador que combina Retry y Circuit Breaker
def retry_and_circuit_breaker():
    def decorator(fn):
        @retry(stop=stop_after_attempt(3), wait=wait_fixed(2))
        def wrapped(*args, **kwargs):
            if is_circuit_open():
                raise Exception("Circuito abierto: evitando llamadas por falla previa.")
            try:
                return fn(*args, **kwargs)
            except Exception as e:
                open_circuit()
                raise e
        return wrapped
    return decorator