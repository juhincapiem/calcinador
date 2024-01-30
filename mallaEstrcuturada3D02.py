import gmsh
import sys
import os

gmsh.initialize()
gmsh.option.setNumber("General.Terminal",1)
gmsh.model.add("calcinador")

front = 0.0
back = -2.0

#Definir puntos
gmsh.model.geo.addPoint(0.0, 4.0, front, 1, 1)
gmsh.model.geo.addPoint(20.0, 0.0, front, 1, 2)
gmsh.model.geo.addPoint(20.0, 8.0, front, 1, 3)
gmsh.model.geo.addPoint(10.0, 16.0, front, 1, 4)
gmsh.model.geo.addPoint(5.0, 16.0, front, 1, 5)
gmsh.model.geo.addPoint(0.0, 12.0, front, 1, 6)

# Lineas rectas
gmsh.model.geo.addLine(1, 2, 1)
gmsh.model.geo.addLine(2, 3, 2)
gmsh.model.geo.addLine(3, 4, 3)
gmsh.model.geo.addLine(4, 5, 4)
gmsh.model.geo.addLine(5, 6, 5)
gmsh.model.geo.addLine(6, 1, 6)
gmsh.model.geo.addLine(3, 6, 7)

# Definir curvas
gmsh.model.geo.addCurveLoop([1, 2, 7, 6], 1)
gmsh.model.geo.addCurveLoop([3, 4, 5, -7], 2)


# Estructurar la malla
m = 60
n = 40

for tag in [6, -2, 5, -3]:
    gmsh.model.geo.mesh.setTransfiniteCurve(tag, n+1)

for tag in [1, -7, -4]:
    gmsh.model.geo.mesh.setTransfiniteCurve(tag, m+1)


# Superficie
gmsh.model.geo.addPlaneSurface([1], 1)
gmsh.model.geo.addPlaneSurface([2], 2)

# Definir que la superficie sea estrcuturada, al igual que las curvas
gmsh.model.geo.mesh.setTransfiniteSurface(1)
gmsh.model.geo.mesh.setTransfiniteSurface(2)

# Recombinamos para que se usen elementos cuadriláteros en vez de triangulares
gmsh.model.geo.mesh.setRecombine(2, 1)
gmsh.model.geo.mesh.setRecombine(2, 2)

vol_ext1 = gmsh.model.geo.extrude([(2, 1)], 0, 0, back, numElements=[10], recombine=True)
vol_ext2 = gmsh.model.geo.extrude([(2, 2)], 0, 0, back, numElements=[10], recombine=True)


gmsh.model.geo.mesh.setTransfiniteVolume(vol_ext1[1][1])
gmsh.model.geo.mesh.setTransfiniteVolume(vol_ext2[1][1])

gmsh.model.addPhysicalGroup(3, [vol_ext1[1][1], vol_ext2[1][1]], 101)

gmsh.model.addPhysicalGroup(2, [20, 28, 38, 46], 1)
gmsh.model.setPhysicalName(2, 1, "noSlip") 

gmsh.model.addPhysicalGroup(2, [16], 2)
gmsh.model.setPhysicalName(2, 2, "inlet") 

gmsh.model.addPhysicalGroup(2, [42], 3)
gmsh.model.setPhysicalName(2, 3, "outlet")

gmsh.model.addPhysicalGroup(2, [1, 2], 4)
gmsh.model.setPhysicalName(2, 4, "front")

gmsh.model.addPhysicalGroup(2, [29, 51], 5)
gmsh.model.setPhysicalName(2, 5, "back")


gmsh.model.addPhysicalGroup(2, [24], 6)
gmsh.model.setPhysicalName(2, 6, "interphase")

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

# Y finalmente guardar la malla
filename = 'calcinadorPrueba01.msh'
gmsh.write(filename)

# Podemos visualizar el resultado en la interfaz gráfica de GMSH
gmsh.fltk.run()

# Tras finalizar el proceso se recomienda usar este comando
gmsh.finalize()


