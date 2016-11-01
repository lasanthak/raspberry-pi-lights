from bit_packing import pack_bits, unpack_bits


class PinPattern8:
    def __init__(self, state_ints_array, loop_count):
        self.loop_count = loop_count
        self.states = []
        for state_int in state_ints_array:
            self.states.append(state_int)


class PatternAlgorithm:
    def __init__(self, loop_count):
        self.prev_pattern_int = None
        self.cur_pattern = None
        self.cur_pattern_id = -1
        self.cur_pos_in_pattern = -1
        self.cur_pattern_loops_remaining = 0
        self.patterns = []
        # Organize patterns
        # -----------------------------------------------------------
        self.patterns.append(PinPattern8(PatternAlgorithm.INITIAL_STATE_PATTERN, 1))
        self.patterns.append(PinPattern8(PatternAlgorithm.ON, int(0.5 * loop_count)))
        self.patterns.append(PinPattern8(PatternAlgorithm.ON_OFF, int(0.3 * loop_count)))
        self.patterns.append(PinPattern8(PatternAlgorithm.FKR_IKR, loop_count))
        self.patterns.append(PinPattern8(PatternAlgorithm.CH_SW, int(0.85 * loop_count)))
        self.patterns.append(PinPattern8(PatternAlgorithm.RAND_ON, int(1.3 * loop_count)))
        self.patterns.append(PinPattern8(PatternAlgorithm.KR_KR, int(1.3 * loop_count)))
        self.patterns.append(PinPattern8(PatternAlgorithm.IKR_RAND, loop_count))
        self.patterns.append(PinPattern8(PatternAlgorithm.FKR, int(0.7 * loop_count)))
        self.patterns.append(PinPattern8(PatternAlgorithm.ON_PR, int(1.5 * loop_count)))
        self.patterns.append(PinPattern8(PatternAlgorithm.KR, int(0.7 * loop_count)))
        # -----------------------------------------------------------

    def _next_pattern_int(self):
        if self.cur_pattern_loops_remaining > 0:
            self.cur_pos_in_pattern += 1
            if self.cur_pos_in_pattern >= len(self.cur_pattern.states):
                self.cur_pos_in_pattern = 0
                self.cur_pattern_loops_remaining -= 1

        if self.cur_pattern_loops_remaining <= 0:
            self.cur_pos_in_pattern = 0
            self.cur_pattern_id = (self.cur_pattern_id + 1) % len(self.patterns)
            self.cur_pattern = self.patterns[self.cur_pattern_id]
            self.cur_pattern_loops_remaining = self.cur_pattern.loop_count

        return self.cur_pattern.states[self.cur_pos_in_pattern]

    def next(self):
        self.prev_pattern_int = self._next_pattern_int()
        return unpack_bits(self.prev_pattern_int)

    @staticmethod
    def inverse_initial_state():
        return unpack_bits(PatternAlgorithm.INVERSE_INITIAL_STATE)

    # Initial state of the pins
    INITIAL_STATE_PATTERN = [pack_bits([0, 0, 0, 0, 0, 0, 0, 0])]
    # Inverse of initial state
    INVERSE_INITIAL_STATE = pack_bits([1, 1, 1, 1, 1, 1, 1, 1])

    # All On
    ON = [
        pack_bits([1, 1, 1, 1, 1, 1, 1, 1])
    ]

    # On - Off
    ON_OFF = [
        pack_bits([1, 1, 1, 1, 1, 1, 1, 1]),
        pack_bits([1, 1, 1, 1, 1, 1, 1, 1]),
        pack_bits([1, 1, 1, 1, 1, 1, 1, 1]),
        pack_bits([0, 0, 0, 0, 0, 0, 0, 0]),
        pack_bits([0, 0, 0, 0, 0, 0, 0, 0]),
        pack_bits([0, 0, 0, 0, 0, 0, 0, 0]),
        pack_bits([1, 1, 1, 1, 1, 1, 1, 1]),
        pack_bits([1, 1, 1, 1, 1, 1, 1, 1]),
        pack_bits([1, 1, 1, 1, 1, 1, 1, 1]),
        pack_bits([0, 0, 0, 0, 0, 0, 0, 0]),
        pack_bits([0, 0, 0, 0, 0, 0, 0, 0]),
        pack_bits([0, 0, 0, 0, 0, 0, 0, 0]),
        pack_bits([1, 1, 1, 1, 1, 1, 1, 1]),
        pack_bits([1, 1, 1, 1, 1, 1, 1, 1]),
        pack_bits([0, 0, 0, 0, 0, 0, 0, 0]),
        pack_bits([0, 0, 0, 0, 0, 0, 0, 0]),
        pack_bits([1, 1, 1, 1, 1, 1, 1, 1]),
        pack_bits([1, 1, 1, 1, 1, 1, 1, 1]),
        pack_bits([0, 0, 0, 0, 0, 0, 0, 0]),
        pack_bits([0, 0, 0, 0, 0, 0, 0, 0]),
        pack_bits([1, 1, 1, 1, 1, 1, 1, 1]),
        pack_bits([1, 1, 1, 1, 1, 1, 1, 1]),
        pack_bits([0, 0, 0, 0, 0, 0, 0, 0]),
        pack_bits([0, 0, 0, 0, 0, 0, 0, 0]),
        pack_bits([1, 1, 1, 1, 1, 1, 1, 1]),
        pack_bits([1, 1, 1, 1, 1, 1, 1, 1]),
        pack_bits([0, 0, 0, 0, 0, 0, 0, 0]),
        pack_bits([0, 0, 0, 0, 0, 0, 0, 0]),
        pack_bits([1, 1, 1, 1, 1, 1, 1, 1]),
        pack_bits([0, 0, 0, 0, 0, 0, 0, 0]),
        pack_bits([1, 1, 1, 1, 1, 1, 1, 1]),
        pack_bits([0, 0, 0, 0, 0, 0, 0, 0]),
        pack_bits([1, 1, 1, 1, 1, 1, 1, 1]),
        pack_bits([0, 0, 0, 0, 0, 0, 0, 0]),
        pack_bits([1, 1, 1, 1, 1, 1, 1, 1]),
        pack_bits([0, 0, 0, 0, 0, 0, 0, 0]),
        pack_bits([1, 1, 1, 1, 1, 1, 1, 1]),
        pack_bits([0, 0, 0, 0, 0, 0, 0, 0])
    ]

    # Knight Riders - Knight Riders
    KR_KR = [
        pack_bits([1, 0, 0, 0, 0, 0, 0, 1]),
        pack_bits([1, 0, 0, 0, 0, 0, 0, 1]),
        pack_bits([0, 1, 0, 0, 0, 0, 1, 0]),
        pack_bits([0, 1, 0, 0, 0, 0, 1, 0]),
        pack_bits([0, 0, 1, 0, 0, 1, 0, 0]),
        pack_bits([0, 0, 1, 0, 0, 1, 0, 0]),
        pack_bits([0, 0, 0, 1, 1, 0, 0, 0]),
        pack_bits([0, 0, 0, 1, 1, 0, 0, 0]),
        pack_bits([0, 0, 1, 0, 0, 1, 0, 0]),
        pack_bits([0, 0, 1, 0, 0, 1, 0, 0]),
        pack_bits([0, 1, 0, 0, 0, 0, 1, 0]),
        pack_bits([0, 1, 0, 0, 0, 0, 1, 0])
    ]

    # Inverse Knight Riders - Random
    IKR_RAND = [
        pack_bits([0, 1, 1, 1, 1, 0, 0, 0]),
        pack_bits([0, 1, 1, 1, 0, 0, 1, 0]),
        pack_bits([1, 0, 1, 1, 0, 0, 0, 1]),
        pack_bits([1, 0, 1, 1, 0, 1, 0, 0]),
        pack_bits([1, 1, 0, 1, 0, 0, 1, 0]),
        pack_bits([1, 1, 0, 1, 1, 0, 0, 0]),
        pack_bits([1, 1, 1, 0, 0, 0, 0, 1]),
        pack_bits([1, 1, 1, 0, 1, 0, 0, 0]),
        pack_bits([1, 1, 0, 1, 0, 1, 0, 0]),
        pack_bits([1, 1, 0, 1, 0, 0, 0, 1]),
        pack_bits([1, 0, 1, 1, 0, 0, 1, 0]),
        pack_bits([1, 0, 1, 1, 0, 1, 0, 0])
    ]

    # Chain - Swipe
    CH_SW = [
        pack_bits([1, 0, 0, 0, 1, 1, 0, 1]),
        pack_bits([1, 0, 0, 0, 1, 0, 1, 1]),
        pack_bits([0, 1, 0, 0, 1, 1, 0, 1]),
        pack_bits([0, 1, 0, 0, 1, 0, 0, 1]),
        pack_bits([0, 0, 1, 0, 1, 1, 0, 1]),
        pack_bits([0, 0, 1, 0, 1, 0, 1, 1]),
        pack_bits([0, 0, 0, 1, 1, 1, 0, 1]),
        pack_bits([0, 0, 0, 1, 1, 0, 0, 1]),
        pack_bits([1, 0, 0, 0, 1, 1, 1, 0]),
        pack_bits([1, 0, 0, 0, 0, 1, 1, 1]),
        pack_bits([0, 1, 0, 0, 1, 1, 1, 0]),
        pack_bits([0, 1, 0, 0, 0, 1, 1, 1]),
        pack_bits([0, 0, 1, 0, 1, 1, 1, 0]),
        pack_bits([0, 0, 1, 0, 0, 1, 1, 1]),
        pack_bits([0, 0, 0, 1, 1, 1, 1, 0]),
        pack_bits([0, 0, 0, 1, 0, 1, 1, 1])
    ]

    # Knight Riders
    KR = [
        pack_bits([1, 0, 0, 0, 0, 0, 0, 0]),
        pack_bits([0, 1, 0, 0, 0, 0, 0, 0]),
        pack_bits([0, 0, 1, 0, 0, 0, 0, 0]),
        pack_bits([0, 0, 0, 1, 0, 0, 0, 0]),
        pack_bits([0, 0, 0, 0, 1, 0, 0, 0]),
        pack_bits([0, 0, 0, 0, 0, 1, 0, 0]),
        pack_bits([0, 0, 0, 0, 0, 0, 1, 0]),
        pack_bits([0, 0, 0, 0, 0, 0, 0, 1]),
        pack_bits([0, 0, 0, 0, 0, 0, 1, 0]),
        pack_bits([0, 0, 0, 0, 0, 1, 0, 0]),
        pack_bits([0, 0, 0, 0, 1, 0, 0, 0]),
        pack_bits([0, 0, 0, 1, 0, 0, 0, 0]),
        pack_bits([0, 0, 1, 0, 0, 0, 0, 0]),
        pack_bits([0, 1, 0, 0, 0, 0, 0, 0])
    ]

    # Fully On - Progress
    ON_PR = [
        pack_bits([1, 1, 1, 1, 1, 0, 0, 0]),
        pack_bits([1, 1, 1, 1, 0, 1, 0, 0]),
        pack_bits([1, 1, 1, 1, 0, 0, 1, 0]),
        pack_bits([1, 1, 1, 1, 0, 0, 0, 1])
    ]

    # Random - Fully On
    RAND_ON = [
        pack_bits([0, 0, 0, 1, 1, 1, 1, 1]),
        pack_bits([1, 0, 0, 0, 1, 1, 1, 1]),
        pack_bits([0, 0, 1, 0, 1, 1, 1, 1]),
        pack_bits([1, 0, 0, 0, 1, 1, 1, 1]),
        pack_bits([0, 1, 0, 0, 1, 1, 1, 1]),
        pack_bits([0, 0, 0, 1, 1, 1, 1, 1]),
        pack_bits([0, 1, 0, 0, 1, 1, 1, 1]),
        pack_bits([0, 0, 1, 0, 1, 1, 1, 1])
    ]

    # Filling Knight Riders
    FKR = [
        pack_bits([0, 0, 0, 0, 0, 0, 0, 0]),
        pack_bits([1, 0, 0, 0, 0, 0, 0, 0]),
        pack_bits([1, 1, 0, 0, 0, 0, 0, 0]),
        pack_bits([1, 1, 1, 0, 0, 0, 0, 0]),
        pack_bits([1, 1, 1, 1, 0, 0, 0, 0]),
        pack_bits([1, 1, 1, 1, 1, 0, 0, 0]),
        pack_bits([1, 1, 1, 1, 1, 1, 0, 0]),
        pack_bits([1, 1, 1, 1, 1, 1, 1, 0]),
        pack_bits([1, 1, 1, 1, 1, 1, 1, 1]),
        pack_bits([1, 1, 1, 1, 1, 1, 1, 0]),
        pack_bits([1, 1, 1, 1, 1, 1, 0, 0]),
        pack_bits([1, 1, 1, 1, 1, 0, 0, 0]),
        pack_bits([1, 1, 1, 1, 0, 0, 0, 0]),
        pack_bits([1, 1, 1, 0, 0, 0, 0, 0]),
        pack_bits([1, 1, 0, 0, 0, 0, 0, 0]),
        pack_bits([1, 0, 0, 0, 0, 0, 0, 0])
    ]

    # Filling Knight Riders - Inverse Knight Riders
    FKR_IKR = [
        pack_bits([1, 0, 0, 0, 0, 1, 1, 1]),
        pack_bits([1, 0, 0, 0, 0, 1, 1, 1]),
        pack_bits([1, 1, 0, 0, 1, 0, 1, 1]),
        pack_bits([1, 1, 0, 0, 1, 0, 1, 1]),
        pack_bits([1, 1, 1, 0, 1, 1, 0, 1]),
        pack_bits([1, 1, 1, 0, 1, 1, 0, 1]),
        pack_bits([1, 1, 1, 1, 1, 1, 1, 0]),
        pack_bits([1, 1, 1, 1, 1, 1, 1, 0]),
        pack_bits([1, 1, 1, 0, 1, 1, 0, 1]),
        pack_bits([1, 1, 1, 0, 1, 1, 0, 1]),
        pack_bits([1, 1, 0, 0, 1, 0, 1, 1]),
        pack_bits([1, 1, 0, 0, 1, 0, 1, 1]),
        pack_bits([1, 0, 0, 0, 0, 1, 1, 1]),
        pack_bits([1, 0, 0, 0, 0, 1, 1, 1]),
        pack_bits([0, 0, 0, 0, 1, 1, 1, 1])
    ]
