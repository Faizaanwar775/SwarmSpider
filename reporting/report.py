import time


class Report:

    def __init__(self):

        self.start = time.perf_counter()

        self.requested = 0
        self.fetched = 0
        self.saved = 0
        self.failed = 0

    def finish(self):

        end = time.perf_counter()

        print("\n========== SUMMARY ==========")

        print(f"Requested : {self.requested}")
        print(f"Validated : {self.fetched}")
        print(f"Saved     : {self.saved}")
        print(f"Failed    : {self.failed}")

        print(
            f"Execution : {end-self.start:.2f} sec"
        )

        print("=============================")