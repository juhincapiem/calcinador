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
gmsh.model.geo.addPoint(0.0, 12.0, front, 1, 4)

# Lineas rectas
gmsh.model.geo.addLine(1, 2, 1)
gmsh.model.geo.addLine(2, 3, 2)
gmsh.model.geo.addLine(3, 4, 3)
gmsh.model.geo.addLine(4, 1, 4)

# Definir curvas
gmsh.model.geo.addCurveLoop([i for i in range(1, 5, 1)], 1)

# Superficie
gmsh.model.geo.addPlaneSurface([1], 1)

#En un modelo común y corriente, la sincronización se da después del addPlaneSurface
gmsh.model.geo.synchronize()

# Frontera
gmsh.model.addPhysicalGroup(1, [1], 1)
gmsh.model.setPhysicalName(1, 1, "airInlet")

gmsh.model.addPhysicalGroup(1, [2, 3, 4], 2)
gmsh.model.setPhysicalName(1, 2, "noSlip")

gmsh.model.addPhysicalGroup(2, [1], 1)
gmsh.model.setPhysicalName(1, 1, "surface")

# Crea malla de dimensión 2
gmsh.model.mesh.generate(2)

# Ver las "caras" de los elementos finitos 2D
gmsh.option.setNumber('Mesh.SurfaceFaces', 1)

# Ver los nodos de la malla  
gmsh.option.setNumber('Mesh.Points', 1)        

# Y finalmente guardar la malla
filename = 'primeraPrueba.msh'
gmsh.write(filename)

# Podemos visualizar el resultado en la interfaz gráfica de GMSH
gmsh.fltk.run()

# Tras finalizar el proceso se recomienda usar este comando
gmsh.finalize()


