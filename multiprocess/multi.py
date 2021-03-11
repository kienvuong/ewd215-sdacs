#module from https://github.com/PamelaM/mptools

from Workers import *

def main():
    with MainContext() as main_ctx:
        init_signals(main_ctx.shutdown_event, default_signal_handler, default_signal_handler)

        send_q = main_ctx.MPQueue()
        reply_q = main_ctx.MPQueue()

        main_ctx.Proc("SEND", SendWorker, send_q)
        main_ctx.Proc("LISTEN", ListenWorker, reply_q)
        main_ctx.Proc("STATUS", StatusWorker)
        main_ctx.Proc("OBSERVATION", ObservationWorker)

        while not main_ctx.shutdown_event.is_set():
            event = main_ctx.event_queue.safe_get()
            if not event:
                continue
            elif event.msg_type == "STATUS":
                send_q.put(event)
            elif event.msg_type == "OBSERVATION":
                send_q.put(event)
            elif event.msg_type == "ERROR":
                send_q.put(event)
            elif event.msg_type == "REQUEST":
                request_handler(event, reply_q, main_ctx)
            elif event.msg_type == "FATAL":
                main_ctx.log(logging.INFO, f"Fatal Event received: {event.msg}")
                break
            elif event.msg_type == "END":
                main_ctx.log(logging.INFO, f"Shutdown Event received: {event.msg}")
                break
            else:
                main_ctx.log(logging.ERROR, f"Unknown Event: {event}")