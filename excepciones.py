try:
    result = 10 / 0  #esto causa un error
except ZeroDivisionError as e:
    print(f"Ocurrio un error: {e}")