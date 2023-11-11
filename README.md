# Project_no_3

Assignment 3 

All group members have contributed equally to the project, and reviewed and approved the report before submission. 

BIM Execution Plan 

When constructing a building many phases are needed for different professionals. To make a good workflow for every person a BIM Execution Plan (BEP) can be made to support the user in designing, calculating, and getting an overview of the project. For this project, the aim of the BEP is to give expectations and some guidelines for using the BIM model. This is from the design and planning to operation and construction. A BEP needs different information to implement the project. 

For this project, a building called SKYLAB needs to be built. A BIM model in IFC is made. The focus of this BEP is to be able to calculate the daylight requirements in the SKYLAB building. Here many different daylight calculations can be carried out and for this project, the focus will be on the 10% rule from BR18. 

When the BIM model is finished, and all the data is implemented, people with different perspectives and professionals can easily talk together and work further with the project.  

For the 10% daylight rule from BR18 will it be easy for e.g., the Engineer to calculate if this rule is satisfied. However, this can only be done if the right dimensions and information are in the BIM model which e.g., the architects might have a big influence on. Since the BIM model is an IFC model people will have easy access to the model even though they are from different companies. 

The 10% rule is a starting point to see if the building might agree with other daylight requirements. If the plan for the building is to achieve a sustainability certification (e.g., DGNP or svanemærket) this calculation is easy to make at the beginning of the process to see if SKYLAB has a good starting point for this type of certification. 

As mentioned before, will BR18 be used for this project as a standard. 


3A: Analyze use case 

The first edition of the SKYLAB model (used in Assignment 2) had a low Level of Development (LOD), it was too low to complete the calculation for the 10% rule correct. Therefore, the aim will be to increase the level of LOD to complete this calculation correctly. To complete the above description people with some understanding of IFC, python, and BlenderBIM are needed. 

To make sure that nothing will be lost it is important that the files have a backup if something happens to a computer. This is also for documentation for the different companies if some errors come up. 


3B: Design for a tool/workflow 

For the IFC model, some errors are observed in reaching the correct calculation of the 10% rule. Here flooring, external windows, and spaces need to be fixed as they are very important for the process. Here IfcOpenShell modifications are required and described below: 

Flooring: Add properties, names, and given areas to all flooring elements. To calculate if the daylight requirements are being held, the area of the flooring to each space is needed, like it’s saying in the BR18 §379 stk. 2 “ Tilstrækkelig tilgang af dagslys kan dokumenteres ved, at glasarealet uden skyggende forhold svarer til mindst 10 pct. af det relevante gulvareal…” In other words, this sentence states that a building meets the requirements for sufficient daylight access if the area of glass in the building, without any obstructions to the sunlight, is at least 10% of the total floor area of the building. Therefore, adding this change to the model will be essential for the calculation.  

External windows: Change the type of some external windows to external (comes out false). This will also be highly important when we need all the external windows to calculate the daylighting properly. If there are some external windows that come out as internal, some information is missing, and we don’t know if we meet the criteria or not.  

Spaces without any information: Add external windows or curtain walls to some spaces that currently lack any information. If a space in a building model lacks any information, it is important to add external windows, curtain walls or even a regular façade to make the model complete and more useful. For daylighting calculations, it is important to take into account all of the openings in a building, as these will affect how much daylight enters the building. Therefore, if some spaces are missing this information, the daylighting calculations will not be accurate. 


3D:  Value; What is the potential improvement offered by this tool? 

In the perfect world will e.g., the Engineer who needs to calculate the 10% rule takes a quick look into the 3D model before doing the calculation. Here the Engineer will get an overview of the model and easily get an expectation of what to expect from the calculation.  

Here the Engineer also sees if there are some errors, e.g., there are no external windows to the façade which has been discussed earlier. The Engineer will in the perfect world contact e.g., the Architect with e.g., the belonging coordinates or name to specify where in the 3D model the error is. The Architect will afterwards easily add the correct curtain wall and the Engineer will make the correct calculation.  

With a procedure like this, the Engineer and Architect do not need to make a meeting or have a larger mail correspondence where misunderstandings can arise. The two people can even be working in different time zones, and they have saved a lot of time.  

The societal value of this is that the different professions easily and quickly can solve the problem which leads them to more time for other problems and projects. This will reduce their work bustle and make the workflow more harmonic and sustainable. Both for themself and for their companies.  

 
