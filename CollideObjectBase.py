"""
Collider classes that the higher level classes in SpaceJamClasses inherit from
"""

from panda3d.core import PandaNode, Loader, NodePath, CollisionNode, CollisionSphere, CollisionInvSphere, CollisionCapsule, Vec3


class PlacedObject(PandaNode):
    """Generic node for Placed object"""
    def __init__(self, loader: Loader, parentNode: NodePath, nodeName: str, modelPath: str):
        self.modelNode: NodePath = loader.loadModel(modelPath)
        self.modelNode.reparentTo(parentNode)
        self.modelNode.setName(nodeName)
               
class CollidableObject(PlacedObject):
    """adds colliders to PlacedObject"""
    def __init__(self, loader: Loader, parentNode: NodePath, nodeName: str, modelPath: str):
        super(CollidableObject, self).__init__(loader, parentNode, nodeName, modelPath)
        
        self.collisionNode = self.modelNode.attachNewNode(CollisionNode(nodeName + "_Cnode"))#Adds a collider to the object

class InverseSphereCollideObj(CollidableObject):
    def __init__(self, loader: Loader , parentNode: NodePath, nodeName: str, modelPath: str, colPositionVec: Vec3, colRadius: float):
        super(InverseSphereCollideObj, self).__init__(loader, parentNode, nodeName, modelPath)
        self.collisionNode.node().addSolid(CollisionInvSphere(colPositionVec, colRadius))

class SphereCollideObj(CollidableObject):
    def __init__(self, loader: Loader , parentNode: NodePath, nodeName: str, modelPath: str, colPositionVec: Vec3, colRadius: float):
        super(SphereCollideObj, self).__init__(loader, parentNode, nodeName, modelPath)
        self.collisionNode.node().addSolid(CollisionSphere(colPositionVec, colRadius))
       
class CapsuleCollidableObject(CollidableObject):
    def __init__(self, loader: Loader, parentNode: NodePath, nodeName: str, modelPath: str, ax:float, ay:float, az:float, bx:float, by:float, bz:float, r:float):
        super(CapsuleCollidableObject, self).__init__(loader, parentNode, nodeName, modelPath)
        self.collisionNode.node().add_solid(CollisionCapsule(ax,ay,az,bx,by,bz,r))
        
             