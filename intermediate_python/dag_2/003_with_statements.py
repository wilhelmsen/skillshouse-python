class controlled_execution:
    def __enter__(self):
        # set things up
        return thing

    def __exit__(self, type, value, traceback):
        #tear things down

with controlled_execution() as thing:
    # some code
