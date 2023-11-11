import ifcopenshell
import ifcopenshell.api

model = ifcopenshell.open(r"C:\Users\Clara\Desktop\Main Folder\ifcopenshell-python-311-v0.7.0-dadcbe6-win64 (1)\model\LLYN - ARK.ifc")
import ifcopenshell.util.element

space = model.by_type("IfcSpace")[1]
print(ifcopenshell.util.element.get_psets(space))

#Spaces - adding "Qto_SpaceBaseQuantites" and "GrossFloorArea" to all IfcSpace
spaces = model.by_type("IfcSpace")
for space in spaces:

    psets = ifcopenshell.util.element.get_psets(space)

    qto = ifcopenshell.api.run("pset.add_qto",model, product=space, name ="Qto_SpaceBaseQuantities")
    
    ifcopenshell.api.run("pset.edit_qto", model, qto=qto, properties={"GrossFloorArea": 120})

    psets = ifcopenshell.util.element.get_psets(space)

#Chaning Space 1 back to be correct.
space1 = model.by_type("IfcSpace")[1]
qto1 = ifcopenshell.api.run("pset.add_qto",model, product=space1, name ="Qto_SpaceBaseQuantities")
    
ifcopenshell.api.run("pset.edit_qto", model, qto=qto1, properties={"GrossFloorArea": 4.396})
print(f"Space [1] is changed into correct value again:{ifcopenshell.util.element.get_psets(space1)}")

#Windows
#Collecting the window with the global ID.
element = model.by_id("1I5_7E6Iz4rhZEaQfJMyEm")

#Just a check to see if the window is IsExternal: False
print(ifcopenshell.util.element.get_psets(element))
    
#Collecting pset_WindowCommon PropertySet for the element.
win = ifcopenshell.util.element.get_pset(element, "Pset_WindowCommon", prop="IsExternal", should_inherit=False)
win_common = ifcopenshell.util.element.get_pset(element, "Pset_WindowCommon", should_inherit=False)
#Now chaning the IsExternal from False to True
ifcopenshell.api.run("pset.edit_pset", model,
    pset=model.by_id(win_common["id"]), properties={"IsExternal": "True"})
print(win_common)

#Now checking if the window is True for IsExternal
print(ifcopenshell.util.element.get_psets(element))

model.write(r"C:\Users\Clara\Desktop\Main Folder\ifcopenshell-python-311-v0.7.0-dadcbe6-win64 (1)\model\LLYNARK31.ifc")
