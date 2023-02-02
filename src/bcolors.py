class bcolors:
    HEADER = '\033[95m'
    ENDC = '\033[0m'

    def disable(self):
        self.HEADER = ''
        self.ENDC = ''

