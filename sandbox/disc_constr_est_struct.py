import json

from libpgm.nodedata import NodeData
from libpgm.graphskeleton import GraphSkeleton
from libpgm.discretebayesiannetwork import DiscreteBayesianNetwork
from libpgm.pgmlearner import PGMLearner

nd = NodeData()
nd.load("nodedata.json")
skel = GraphSkeleton()
skel.load("nodedata.json")
skel.toporder()

bn = DiscreteBayesianNetwork(skel,nd)
with open("manipulatedata.json") as fp:
    data = json.load(fp)

learner = PGMLearner()

# result = learner.discrete_constraint_estimatestruct(data)
result = learner.discrete_estimatebn(data)

print json.dumps(result.E, indent=2)
print json.dumps(result.Vdata, indent=2)
