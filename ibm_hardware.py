import qiskit
from qiskit import IBMQ

#get account
IBMQ.enable_account(TOKEN, hub='ibm-q-community', group='mit-hackathon', project='main')

#get provider
provider = IBMQ.get_provider(hub='ibm-q-community', group='mit-hackathon', project='main')
provider.backends()