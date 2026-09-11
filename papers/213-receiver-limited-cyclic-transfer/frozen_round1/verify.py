"""P213 source-only author verifier. Execution requires a separate gate.

No imports, file access, command line, environment access or subprocesses.
Fixed scope: n = 1..6, N = 0..4; 461 labelled states in 30 full carriers.
This code is independently authored from the comparison-word proof.
It does not read or import candidate, gate or canonical data.
"""

N_MIN = 1
N_MAX = 6
MASS_MIN = 0
MASS_MAX = 4
EXPECTED_CARRIERS = 30
EXPECTED_STATES = 461
STATUS_ORDER = (
    "ACCEPTED", "PARITY", "NEGATIVE_DESCENT", "NONSTRICT_DESCENT",
    "SHORT_PEAK", "ASCENT_EQUALITY", "ASCENT_ORDER", "EMPTY_INTERVAL",
)
SHAPE_ORDER = ("R1", "R2", "RGE3", "WRAP")
CHECKS = 0


def require(condition, label):
    global CHECKS
    CHECKS += 1
    if not condition:
        raise AssertionError(label)


def compositions(length, mass):
    if length == 1:
        return [(mass,)]
    out = []
    for head in range(mass + 1):
        for tail in compositions(length - 1, mass - head):
            out.append((head,) + tail)
    return out


def choose(total, selected):
    selected = min(selected, total - selected)
    value = 1
    for j in range(1, selected + 1):
        value = value * (total - selected + j) // j
    return value


def forward(a):
    size = len(a)
    currents = [min(a[i], a[(i + 1) % size]) for i in range(size)]
    return tuple(a[i] - currents[i] + currents[(i - 1) % size]
                 for i in range(size))


def isolated(a):
    baseline = min(a)
    size = len(a)
    return all((a[i] - baseline) * (a[(i + 1) % size] - baseline) == 0
               for i in range(size))


def endpoint_terminal(a):
    size = len(a)
    baseline = min(a)
    residual = [value - baseline for value in a]
    terminal = [baseline] * size
    for endpoint in range(size):
        if residual[endpoint] > 0 and residual[(endpoint + 1) % size] == 0:
            cursor = endpoint
            run_mass = 0
            while residual[cursor] > 0:
                run_mass += residual[cursor]
                cursor = (cursor - 1) % size
            terminal[endpoint] += run_mass
    return tuple(terminal)


def direct_orbit(a, successors):
    seen = set()
    path = []
    current = a
    while True:
        require(current not in seen, "nonfixed cycle")
        seen.add(current)
        path.append(current)
        following = successors[current]
        if following == current:
            return path
        current = following


def comparison_mask(a):
    return sum(1 << i for i in range(len(a))
               if a[i] <= a[(i + 1) % len(a)])


def word_text(mask, size):
    return "".join(str((mask >> i) & 1) for i in range(size))


def blocks_for(mask, size):
    bits = [(mask >> i) & 1 for i in range(size)]
    valleys = [i for i in range(size) if bits[(i - 1) % size] == 0
               and bits[i] == 1]
    blocks = []
    for valley in valleys:
        peak = valley
        while bits[peak % size] == 1:
            peak += 1
        following_valley = peak
        while bits[following_valley % size] == 0:
            following_valley += 1
        blocks.append((valley, peak, following_valley))
    return valleys, blocks


def word_sources(y, mask):
    """Return first-failure certificate and all sources, without forward()."""
    size = len(y)
    valleys, blocks = blocks_for(mask, size)
    values = [None] * size
    for valley in valleys:
        values[valley] = y[valley]
    intervals = []

    def rejected(status):
        return {
            "status": status, "weight": 0, "intervals": tuple(intervals),
            "sources": [], "blocks": tuple(blocks),
        }

    # The same order as the proof: all descent interiors, then all ascents.
    for valley, peak, following_valley in blocks:
        for unwrapped in range(following_valley - 1, peak, -1):
            index = unwrapped % size
            following = (unwrapped + 1) % size
            numerator = y[index] + values[following]
            if numerator % 2:
                return rejected("PARITY")
            forced = numerator // 2
            if forced < 0:
                return rejected("NEGATIVE_DESCENT")
            if forced <= values[following]:
                return rejected("NONSTRICT_DESCENT")
            values[index] = forced

    for valley, peak, following_valley in blocks:
        rise = peak - valley
        peak_index = peak % size
        following = (peak + 1) % size
        if rise == 1:
            forced = y[peak_index] - values[valley] + values[following]
            if not (values[valley] <= forced and forced > values[following]):
                return rejected("SHORT_PEAK")
            values[peak_index] = forced
            continue
        if y[(valley + 1) % size] != y[valley]:
            return rejected("ASCENT_EQUALITY")
        if any(y[j % size] > y[(j + 1) % size]
               for j in range(valley + 1, peak - 1)):
            return rejected("ASCENT_ORDER")
        for j in range(valley, peak - 1):
            values[j % size] = y[(j + 1) % size]
        prepeak = (peak - 1) % size
        total_pair = y[peak_index] + values[following]
        lower = y[prepeak]
        upper = min(total_pair // 2, y[peak_index] - 1)
        intervals.append((prepeak, peak_index, lower, upper, total_pair))
        if lower > upper:
            return rejected("EMPTY_INTERVAL")

    sources = []

    def fill(which):
        if which == len(intervals):
            require(all(value is not None and value >= 0 for value in values),
                    "atlas missing or negative coordinate")
            source = tuple(values)
            require(sum(source) == sum(y), "atlas automatic mass")
            require(comparison_mask(source) == mask, "atlas exact tie word")
            sources.append(source)
            return
        prepeak, peak, lower, upper, total_pair = intervals[which]
        for free in range(lower, upper + 1):
            values[prepeak] = free
            values[peak] = total_pair - free
            fill(which + 1)

    fill(0)
    weight = 1
    for prepeak, peak, lower, upper, total_pair in intervals:
        weight *= upper - lower + 1
    require(weight == len(sources), "interval product count")
    require(len(sources) == len(set(sources)), "duplicate within word")
    return {
        "status": "ACCEPTED", "weight": weight, "intervals": tuple(intervals),
        "sources": sorted(sources), "blocks": tuple(blocks),
    }


def fixed_product(y):
    baseline = min(y)
    residual = [value - baseline for value in y]
    if max(residual) == 0:
        return 1
    value = 1
    size = len(y)
    for endpoint in range(size):
        if residual[endpoint] == 0:
            continue
        gap = 0
        cursor = (endpoint - 1) % size
        while residual[cursor] == 0:
            gap += 1
            cursor = (cursor - 1) % size
        if gap >= 2:
            value *= residual[endpoint] // 2 + 1
    return value


def height_formula(size, mass):
    if size <= 2 or mass == 0:
        return 0
    if size == 3:
        return (mass - 1).bit_length()
    return mass - 1


def height_witness(size, mass):
    if size <= 2 or mass <= 1:
        return (mass,) + (0,) * (size - 1)
    if size == 3:
        return (mass - 1, 1, 0)
    if mass == 2:
        return (1, 1) + (0,) * (size - 2)
    return (mass - 2, 1, 1) + (0,) * (size - 3)


def check_two_site_clock(a, path):
    if len(a) != 3:
        return 0
    baseline = min(a)
    residual = [value - baseline for value in a]
    if sum(value > 0 for value in residual) != 2:
        return 0
    head = next(i for i in range(3)
                if residual[i] > 0 and residual[(i - 1) % 3] == 0)
    endpoint = (head + 1) % 3
    total = residual[head] + residual[endpoint]
    initial_receiver = residual[endpoint]
    for time in range(len(path) + 1):
        state = path[time] if time < len(path) else path[-1]
        require(state[head] - baseline == max(total - (1 << time) *
                                             initial_receiver, 0),
                "two-site head clock")
        require(state[endpoint] - baseline == min((1 << time) *
                                                  initial_receiver, total),
                "two-site receiver clock")
    return 1


def state_text(a):
    return ",".join(str(value) for value in a)


def states_text(states):
    return ";".join(state_text(a) for a in states) if states else "-"


def tuple_list_text(values):
    return ";".join(",".join(str(entry) for entry in value)
                    for value in values) if values else "-"


def census_text(census, order):
    return ",".join(key + ":" + str(census[key]) for key in order)


def main():
    output = [
        "P213_VERIFY_V1",
        "PARAM n_min=1 n_max=6 mass_min=0 mass_max=4 carriers=30 states=461",
    ]
    carrier_count = 0
    state_count = 0
    word_count = 0
    two_site_count = 0
    degree_two_count = 0
    global_status = {key: 0 for key in STATUS_ORDER}
    global_shape = {key: 0 for key in SHAPE_ORDER}
    global_accepted_shape = {key: 0 for key in SHAPE_ORDER}

    for size in range(N_MIN, N_MAX + 1):
        for mass in range(MASS_MIN, MASS_MAX + 1):
            carrier_count += 1
            states = compositions(size, mass)
            require(len(states) == choose(mass + size - 1, size - 1),
                    "full composition cardinality")
            require(states == sorted(set(states)), "unique lexicographic carrier")
            require(all(len(a) == size and sum(a) == mass
                        and min(a) >= 0 for a in states), "carrier membership")
            state_count += len(states)
            successors = {a: forward(a) for a in states}
            predecessors = {a: [] for a in states}
            for a in states:
                following = successors[a]
                require(following in predecessors, "forward carrier closure")
                require(min(a) == min(following), "minimum preservation")
                baseline = min(a)
                require(all(a[i] != baseline or following[i] == baseline
                            for i in range(size)), "residual zero permanence")
                require((following == a) == isolated(a), "fixed classification")
                if size <= 2:
                    require(following == a, "short-cycle identity")
                predecessors[following].append(a)

            depths = {}
            terminals = {}
            paths = {}
            for a in states:
                path = direct_orbit(a, successors)
                paths[a] = path
                depths[a] = len(path) - 1
                terminals[a] = path[-1]
                require(path[-1] == endpoint_terminal(a), "original endpoint terminal")
                require(depths[a] <= max(0, mass - 1), "global temporal bound")
                two_site_count += check_two_site_clock(a, path)
            actual_height = max(depths.values())
            require(actual_height == height_formula(size, mass), "sharp carrier height")
            require(depths[height_witness(size, mass)] == actual_height,
                    "attained height witness")

            status = {key: 0 for key in STATUS_ORDER}
            shape = {key: 0 for key in SHAPE_ORDER}
            accepted_shape = {key: 0 for key in SHAPE_ORDER}
            carrier_degree_two = 0
            for y in states:
                if size <= 2:
                    atlas = [y]
                else:
                    atlas = [y] if min(y) == max(y) else []
                    for mask in range(1, (1 << size) - 1):
                        word_count += 1
                        result = word_sources(y, mask)
                        status[result["status"]] += 1
                        block_shapes = []
                        for valley, peak, following_valley in result["blocks"]:
                            rise = peak - valley
                            kind = "R1" if rise == 1 else "R2" if rise == 2 else "RGE3"
                            block_shapes.append(kind)
                            if following_valley >= size:
                                block_shapes.append("WRAP")
                        for kind in block_shapes:
                            shape[kind] += 1
                            if result["status"] == "ACCEPTED":
                                accepted_shape[kind] += 1
                        if result["status"] == "ACCEPTED" and len(result["intervals"]) >= 2:
                            carrier_degree_two += 1
                        expected_word_sources = [
                            source for source in predecessors[y]
                            if comparison_mask(source) == mask
                        ]
                        require(result["sources"] == expected_word_sources,
                                "exact sources in comparison word")
                        atlas.extend(result["sources"])
                        output.append(
                            "WORD n=" + str(size) + " N=" + str(mass) +
                            " y=" + state_text(y) + " s=" + word_text(mask, size) +
                            " status=" + result["status"] +
                            " weight=" + str(result["weight"]) +
                            " intervals=" + tuple_list_text(result["intervals"]) +
                            " sources=" + states_text(result["sources"])
                        )
                require(len(atlas) == len(set(atlas)), "disjoint word union")
                require(sorted(atlas) == predecessors[y], "all-target exact source set")
                product_text = "-"
                if isolated(y):
                    product = fixed_product(y)
                    require(product == len(predecessors[y]), "fixed-target exact product")
                    product_text = str(product)
                output.append(
                    "TARGET n=" + str(size) + " N=" + str(mass) +
                    " y=" + state_text(y) + " next=" + state_text(successors[y]) +
                    " tau=" + str(depths[y]) + " terminal=" + state_text(terminals[y]) +
                    " indegree=" + str(len(predecessors[y])) +
                    " fixed_product=" + product_text +
                    " sources=" + states_text(predecessors[y])
                )

            maximum = max(len(predecessors[y]) for y in states)
            maximizers = [y for y in states if len(predecessors[y]) == maximum]
            if size >= 3:
                degree = size // 3
                require(maximum <= ((1 << size) - 1) * (mass + 1) ** degree,
                        "finite upper-bound instance")
                if mass >= 2 * degree:
                    quotient = mass // (2 * degree)
                    spaced = [0] * size
                    for index in range(degree):
                        spaced[3 * index + 2] = 2 * quotient
                    spaced[2] += mass - 2 * degree * quotient
                    spaced = tuple(spaced)
                    require(isolated(spaced), "spaced-spike fixed witness")
                    require(len(predecessors[spaced]) >= (quotient + 1) ** degree,
                            "spaced-spike fibre lower witness")
                    require(maximum * (2 * degree) ** degree >= mass ** degree,
                            "finite rational lower-bound instance")
            else:
                require(maximum == 1, "identity fibre")
            for key in STATUS_ORDER:
                global_status[key] += status[key]
            for key in SHAPE_ORDER:
                global_shape[key] += shape[key]
                global_accepted_shape[key] += accepted_shape[key]
            degree_two_count += carrier_degree_two
            output.append(
                "CARRIER n=" + str(size) + " N=" + str(mass) +
                " states=" + str(len(states)) + " height=" + str(actual_height) +
                " max_indegree=" + str(maximum) +
                " maximizers=" + states_text(maximizers) +
                " status=" + census_text(status, STATUS_ORDER) +
                " shapes=" + census_text(shape, SHAPE_ORDER) +
                " accepted_shapes=" + census_text(accepted_shape, SHAPE_ORDER) +
                " degree_two=" + str(carrier_degree_two)
            )
    require(carrier_count == EXPECTED_CARRIERS, "declared carrier coverage")
    require(state_count == EXPECTED_STATES, "declared state coverage")
    for key in STATUS_ORDER:
        if key != "NEGATIVE_DESCENT":
            require(global_status[key] > 0, "retained branch coverage " + key)
    require(global_status["NEGATIVE_DESCENT"] == 0, "nonnegative target recursion")
    for key in SHAPE_ORDER:
        require(global_accepted_shape[key] > 0, "accepted shape coverage " + key)
    require(degree_two_count > 0, "accepted degree-two chambers")
    require(two_site_count > 0, "two-site pointwise clock coverage")
    output.append(
        "TOTAL carriers=" + str(carrier_count) + " states=" + str(state_count) +
        " words=" + str(word_count) +
        " two_site=" + str(two_site_count) + " degree_two=" + str(degree_two_count) +
        " status=" + census_text(global_status, STATUS_ORDER) +
        " shapes=" + census_text(global_shape, SHAPE_ORDER) +
        " accepted_shapes=" + census_text(global_accepted_shape, SHAPE_ORDER)
    )
    output.append("PASS checks=" + str(CHECKS))
    # The entire scientific result is constructed before the first write.
    print("\n".join(output))


if __name__ == "__main__":
    main()

