
def predict_trouble(parameters = [0.8683269 , 0.39393166, 0.47681407, 0.30033276, 0.97830805, 0.52097628, 0.99194506, 0.92128744, 0.57695905, 0.36047569,0.83097868, 0.47035325], 
                    example):
    qc = QuantumCircuit(3)
    embed_example(qc, example)
    apply_parameters(qc, parameters)
    result = run_circuit(qc, Aer.get_backend("aer_simulator"))
    return make_prediction(result)
                        

def embed_example(circuit, example):
    circuit.rx(np.pi * example[0], 0)
    circuit.rx(np.pi * example[1], 1)
    circuit.rx(np.pi * example[2], 2)

def apply_parameters(circuit, parameters):
    # TODO: use full range
    layers = np.reshape(parameters, (int(len(parameters)/3), 3))
    layer_count = 1
    for layer in layers:
        for gate in range(len(layer)):
            if layer_count % 3 == 0:
                circuit.rx(np.pi * layer[gate], gate)
            elif layer_count % 3 == 1:
                circuit.ry(np.pi * layer[gate], gate)
            else:
                circuit.rz(np.pi * layer[gate], gate)
        circuit.cx(0,1)
        circuit.cx(1,2)
        circuit.cx(2,0)
        layer_count += 1
        circuit.barrier()
    circuit.measure_all()

def run_circuit(circuit, backend):

    num_shots = 500
    job = execute(circuit,
                  shots=num_shots,
                  backend=backend)

    # Return the measured counts
    return job.result().get_counts()

def make_prediction(result):
    count_0 = 0
    count_1 = 0
    for measurement in result:
        # Determine vote
        if measurement.count('1') > measurement.count('0'):
            count_1 += result[measurement]
        else:
            count0 += result[measurement]
    if count_1 > count_0:
        return 1
    else:
        return 0
