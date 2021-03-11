# #bij multiprocessing kan het voorkomen dat er meerdere processen tegelijkertijd lopen
# #deze processen maken wellicht tegelijkertijd gebruik van een variabele of een bron
# #door de lock erop te gooien, is de variabele/bron voor even niet toegankelijk totdat het proces het weer toelaat
# #afhankelijk van het programma moet je zelf bepalen wanneer het proces dat toe laat
#
# import multiprocessing
# import time
#
# #CODE 1, hoe het niet moet (de code zonder de lock):
# #-----------------------------------------------------------
#
# def erbij(counter):
#     for i in range(100):
#         time.sleep(0.01)
#         counter.value = counter.value + 1
#
# def eraf(counter):
#     for i in range(100):
#         time.sleep(0.01)
#         counter.value = counter.value - 1
#
# if __name__ == '__main__':
#     counter = multiprocessing.Value('i', 200)
#     b = multiprocessing.Process(target=erbij, args=(counter, ))
#     a = multiprocessing.Process(target=eraf, args=(counter, ))
#     b.start()
#     a.start()
#     b.join()
#     a.join()
#     print(counter.value)
# #-----------------------------------------------------------
#
# #CODE 2, hoe het wel moet:
# #-----------------------------------------------------------
# def erbij(counter, lock):
#     for i in range(100):
#         time.sleep(0.01)
#         lock.acquire()
#         counter.value = counter.value + 1
#         lock.release()
#
# def eraf(counter, lock):
#     for i in range(100):
#         time.sleep(0.01)
#         lock.acquire()
#         counter.value = counter.value - 1
#         lock.release()
#
# if __name__ == '__main__':
#     counter = multiprocessing.Value('i', 200)
#     lock = multiprocessing.Lock()
#     b = multiprocessing.Process(target=erbij, args=(counter,lock))
#     a = multiprocessing.Process(target=eraf, args=(counter,lock))
#     b.start()
#     a.start()
#     b.join()
#     a.join()
#     print(counter.value)
# #-----------------------------------------------------------
