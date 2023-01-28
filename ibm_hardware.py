import qiskit
from qiskit import *
from qiskit import IBMQ
from qiskit.compiler import assemble, transpile
from qiskit.providers.fake_provider import FakeNairobiV2

""" 
Get account/backend (REAL)
"""
#Token = User's ID
#IBMQ.enable_account(TOKEN, hub='ibm-q-community', group='mit-hackathon', project='main')
#provider = IBMQ.get_provider(hub='ibm-q-community', group='mit-hackathon', project='main')
#backend = provider.get_backend('ibm-q-community')

"""
Get account/backend (Fake)
"""

backend = FakeNairobiV2

"""
Retrieving Job
"""

#Retriving the Job
job = backend.run()
result = job.result()

