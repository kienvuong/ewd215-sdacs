# # queue maakt het mogelijk om data uit te wisselen tussen processen
# # je hebt meerdere processen als je multiprocessing toepast.

# # CODE 1: de data "result" is niet meer van buitenaf
# # benaderbaar nadat het multiproces p is afgelopen
# # ----------------------------------------
# import multiprocessing
#
# list = []
#
# def totDeMacht(numbers):
#     global list
#     for n in numbers:
#         list.append(n*n)
#     print('inside process' + str(list))
#
# # if __name__ == "__main__":
# numbers = [2, 3, 5]
# p = multiprocessing.Process(target=totDeMacht, args=(numbers, ))
# p.start()
# p.join()
#
# print('outside process' + str(list))
# # ----------------------------------------


# # code 2: is wel van buitenaf benaderbaar door queue put() en get() te gebruiken
# # ----------------------------------------
# import multiprocessing
# def totDeMacht(numbers, q):
#     for n in numbers:
#         q.put(n*n)
#
# numbers = [2, 3, 5]
# q = multiprocessing.Queue()
# p = multiprocessing.Process(target=totDeMacht, args=(numbers, q))
# p.start()
# p.join()
#
# #de data is nu wel van buitenaf te benaderen:
# while q.empty() is False:
#     print(q.get())
# # ----------------------------------------