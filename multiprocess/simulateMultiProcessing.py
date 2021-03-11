#bij meerdere processen hoeft de ene niet te wachten op de andere waardoor het proces sneller verloopt
#meerdere processen worden tegelijkertijd gestart

import time
import concurrent.futures

start = time.perf_counter()


def do_somthing(seconds):
    print(f'Sleeping {seconds} second')
    time.sleep(seconds)
    print (f'Done Sleeping {seconds}')

with concurrent.futures.ProcessPoolExecutor() as executor:
    seconds = [5, 4, 3, 2, 1]
    executor.map(do_somthing, seconds)
# --------------------------------------------------------------------
    # for f in concurrent.futures.as_completed(results):
    #     print(f.result())

    # f1 = executor.submit(do_somthing, 1)
    # f2 = executor.submit(do_somthing, 1)
    #
    # print(f1.result())
    # print(f2.result())
# --------------------------------------------------------------------
# processes = []
#
# #start 10 times the do_something function
# for _ in range(10):
#     p = multiprocessing.Process(target=do_somthing, args=[5])
#     p.start()
#     processes.append(p)
#
# #wait for all process finished and then execute the rest of the code
# for process in processes:
#     process.join()
# --------------------------------------------------------------------

finish = time.perf_counter()

print(f'Finished in {round(finish-start, 3)} seconds')