import re


class Map:
    _possible_motions = ('START', 'TURN_RIGHT', 'TURN_LEFT', 'GO')
    route = []

    def is_valid(self, data):
        """
        Basic route validation
        """
        return True if all(any((self._possible_motions[i] in line)
                               for i in range(0, len(self._possible_motions)))
                           for line in data) else False

    def interpret(self, data):
        """
        Route interpreter
        """
        for line in data:
            if 'START' in line:
                self.route.append(('START', re.findall('[\d]+', line)))
            elif 'TURN_RIGHT' in line:
                self.route.append(('TURN_RIGHT', None))
            elif 'TURN_LEFT' in line:
                self.route.append(('TURN_LEFT', None))
            elif 'GO' in line:
                self.route.append(('GO', re.findall('[\d]+', line)))
        return self.route
