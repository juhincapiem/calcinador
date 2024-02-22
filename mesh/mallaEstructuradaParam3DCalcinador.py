import gmsh
import sys
import os
import pandas as pd
import numpy as np


simData = pd.read_csv("meshInfo.dat")
simData.to_numpy()
simData.columns = simData.columns.str.strip()
simData.set_index('Variable',inplace=True)
print(simData)
posX = np.zeros(10)
posY = np.zeros(10)

for i in range(len(posX)):
    posX[i]  = np.float64(simData.loc['p{:.0f}x'.format(i+1)]['Value'])
    posY[i]  = np.float64(simData.loc['p{:.0f}y'.format(i+1)]['Value'])
print(posX)

front  = np.float64(simData.loc["front"]['Value'])
back  = np.float64(simData.loc["back"]['Value'])
allSurfaceXMesh  = np.int32(simData.loc["mallaX"]['Value'])   # Control mesh in X direction in all surfaces
structureYMesh  = np.int32(simData.loc["mallaS1"]['Value'])    # Control mesh in Y direction in structure |    |
roofYMesh  = np.int32(simData.loc["mallaS2"]['Value'])         # Control mesh in Y direction in rook /    \
nozzleYMesh  = np.int32(simData.loc["mallaS3"]['Value'])       # Control mesh in Y direction in nozzle \ /
fireplaceYMesh  = np.int32(simData.loc["mallaS4"]['Value'])    # Control mesh in Y direction in fireplace |  |
z  = np.int32(simData.loc["profun"]['Value'])                 # Control mesh in Z direction 


gmsh.initialize()
gmsh.option.setNumber("General.Terminal",1)
gmsh.model.add("calcinador")

for i in range(0, len(posX)):
    #Definir puntos
    gmsh.model.geo.addPoint(posX[i], posY[i], front, 1, i+1)


# Lineas rectas
gmsh.model.geo.addLine(1, 2, 1)
gmsh.model.geo.addLine(2, 3, 2)
gmsh.model.geo.addLine(3, 4, 3)
gmsh.model.geo.addLine(4, 5, 4)
gmsh.model.geo.addLine(5, 6, 5)
gmsh.model.geo.addLine(6, 1, 6)
gmsh.model.geo.addLine(3, 6, 7)
#Líneas del ducto
gmsh.model.geo.addLine(4, 7, 8)
gmsh.model.geo.addLine(7, 9, 9)
gmsh.model.geo.addLine(9, 5, 10)
gmsh.model.geo.addLine(7, 8, 11)
gmsh.model.geo.addLine(8, 10, 12)
gmsh.model.geo.addLine(10, 9, 13)

# Definir curvas
gmsh.model.geo.addCurveLoop([1, 2, 7, 6], 1)
gmsh.model.geo.addCurveLoop([3, 4, 5, -7], 2)
# Curvas del ducto
gmsh.model.geo.addCurveLoop([8, 9, 10, -4], 3)
gmsh.model.geo.addCurveLoop([11, 12, 13, -9], 4)

for tag in [6, -2]:
    gmsh.model.geo.mesh.setTransfiniteCurve(tag, structureYMesh+1)

for tag in [5, -3]:
    gmsh.model.geo.mesh.setTransfiniteCurve(tag, roofYMesh+1)

for tag in [10, -8]:
    gmsh.model.geo.mesh.setTransfiniteCurve(tag, nozzleYMesh+1)

for tag in [13, -11]:
    gmsh.model.geo.mesh.setTransfiniteCurve(tag, fireplaceYMesh+1)

for tag in [1, -7, -4, -9, -12]:
    gmsh.model.geo.mesh.setTransfiniteCurve(tag, allSurfaceXMesh+1)


# Superficie
gmsh.model.geo.addPlaneSurface([1], 1)
gmsh.model.geo.addPlaneSurface([2], 2)
gmsh.model.geo.addPlaneSurface([3], 3)
gmsh.model.geo.addPlaneSurface([4], 4)

# Definir que la superficie sea estrcuturada, al igual que las curvas
gmsh.model.geo.mesh.setTransfiniteSurface(1)
gmsh.model.geo.mesh.setTransfiniteSurface(2)
gmsh.model.geo.mesh.setTransfiniteSurface(3)
gmsh.model.geo.mesh.setTransfiniteSurface(4)

# Recombinamos para que se usen elementos cuadriláteros en vez de triangulares
gmsh.model.geo.mesh.setRecombine(2, 1)
gmsh.model.geo.mesh.setRecombine(2, 2)
gmsh.model.geo.mesh.setRecombine(2, 3)
gmsh.model.geo.mesh.setRecombine(2, 4)

# Extruimos las superficies [(superficie, tag)]
# Recombine es para hacer la malla estructurada cuadrilátera en el volumen
vol_ext1 = gmsh.model.geo.extrude([(2, 1)], 0, 0, back, numElements=[z], recombine=True)
vol_ext2 = gmsh.model.geo.extrude([(2, 2)], 0, 0, back, numElements=[z], recombine=True)
tobera = gmsh.model.geo.extrude([(2, 3)], 0, 0, back, numElements=[z], recombine=True)
ducto = gmsh.model.geo.extrude([(2, 4)], 0, 0, back, numElements=[z], recombine=True)


# Estoy tomando el tag de un diccionario
# Posición 1 para acceder al volumen creado y posición para acceder al tag
gmsh.model.geo.mesh.setTransfiniteVolume(vol_ext1[1][1])
gmsh.model.geo.mesh.setTransfiniteVolume(vol_ext2[1][1])
gmsh.model.geo.mesh.setTransfiniteVolume(tobera[1][1])
gmsh.model.geo.mesh.setTransfiniteVolume(ducto[1][1])

# Junto todos los volúmenes 
gmsh.model.addPhysicalGroup(3, [vol_ext1[1][1], vol_ext2[1][1], tobera[1][1], ducto[1][1]], 101)

# Cuando se crearon las nuevas superficies y se extruyen, se crea otro orden para renombrarlas
gmsh.model.addPhysicalGroup(2, [22], 2)
gmsh.model.setPhysicalName(2, 2, "inlet") 

gmsh.model.addPhysicalGroup(2, [92], 3)
gmsh.model.setPhysicalName(2, 3, "outlet")

gmsh.model.addPhysicalGroup(2, [26, 44, 66, 88, 96, 74, 52, 34], 1)
gmsh.model.setPhysicalName(2, 1, "walls") 

gmsh.model.addPhysicalGroup(2, [1, 2, 3, 4], 4)
gmsh.model.setPhysicalName(2, 4, "front")

gmsh.model.addPhysicalGroup(2, [35, 57, 79, 101], 5)
gmsh.model.setPhysicalName(2, 5, "back")

#----
# Cuando se hacen mallas estrcturada, la sincronización se da después del recombine
#----
gmsh.model.geo.synchronize()

# Crea malla de dimensión 3
gmsh.model.mesh.generate(3)

# Ver las "caras" de los elementos finitos 2D
gmsh.option.setNumber('Mesh.SurfaceFaces', 1)

# Ver los nodos de la malla  
gmsh.option.setNumber('Mesh.Points', 1)        

# Y finalmente guardar la malla, usando ASCII v2.2 
# Importante porque esa es la única versión que puede interpretar OF
gmsh.option.setNumber("Mesh.MshFileVersion",2.2)  
filename = 'calciner.msh'
gmsh.write(filename)

# Podemos visualizar el resultado en la interfaz gráfica de GMSH
gmsh.fltk.run()

# Tras finalizar el proceso se recomienda usar este comando
gmsh.finalize()



