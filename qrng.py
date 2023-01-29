from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit, execute,IBMQ
from qiskit.tools.monitor import job_monitor

def qrng(n:int, api_token, provider='ibm-q'):
  IBMQ.enable_account(api_token)
  provider = IBMQ.get_provider(hub=provider)
  
  q = QuantumRegister(16,'q')
  c = ClassicalRegister(16,'c')
  circuit = QuantumCircuit(q,c)
  circuit.h(q) # Applies hadamard gate to all qubits
  circuit.measure(q,c) # Measures all qubits 

  backend = provider.get_backend('ibmq_qasm_simulator')
  job = execute(circuit, backend, shots=1)

  print('Executing Job...\n')                 
  job_monitor(job)
  counts = job.result().get_counts()

  return counts
