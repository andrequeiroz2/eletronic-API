

def resistance_series(circuit_series):
    num_r = []
    for x in circuit_series:
        num = x[0]
        grant = x[1]
        if grant == 'G' or grant == 'g':
            num_r.append(num * 1000000000)
        elif grant == 'M' or grant == 'm':
            num_r.append(num * 1000000)
        elif grant == 'K' or grant == 'k':
            num_r.append(num * 1000)
        elif grant == 'O' or grant == 'o':
            num_r.append(num)
    result = sum(num_r)
    return result


def resistance_parallel(circuit_parallel):
    num_len = len(circuit_parallel)
    print(num_len)
    num_r = []
    result_r = []
    for x in range(0, num_len):
        new_list = circuit_parallel[x]
        for x in new_list:
            num = x[0]
            grant = x[1]
            if grant == 'G' or grant == 'g':
                num_r.append(1 / (num * 1000000000))
            elif grant == 'M' or grant == 'm':
                num_r.append(1 / (num * 1000000))
            elif grant == 'K' or grant == 'k':
                num_r.append(1 / (num * 1000))
            elif grant == 'O' or grant == 'o':
                num_r.append(1 / num)
        result_r.append(1 / (sum(num_r)))
        num_r.clear()
    result = sum(result_r)
    return result


def circuit(circuit):
    if 'serie' in circuit:
        circuit_series = circuit.get('serie')
        result = resistance_series(circuit_series)

    elif 'paralelo' in circuit:
        circuit_parallel = circuit.get('paralelo')
        result = resistance_parallel(circuit_parallel)

    elif 'misto' in circuit:
        circuit_misto = circuit.get('misto')
        #circuit_misto_p = circuit_misto()
    else:
        circuit_misto = "null"
    return  result
