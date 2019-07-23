from worker import add

r = add.delay(4, 5).get()
print(r)  # 9