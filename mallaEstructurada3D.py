import gmsh
import sys
import os

gmsh.initialize()
# Visualizar lo que hace gmsh en la terminal de python
gmsh.option.setNumber("General.Terminal",1)
# Nombre del modelo
gmsh.model.add("calcinador3D")

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

# Superficie
gmsh.model.geo.addPlaneSurface([1], 1)
gmsh.model.geo.addPlaneSurface([2], 2)

gmsh.model.geo.synchronize()

# Hago extrusión
vol_ext1 = gmsh.model.geo.extrude([(2, 1)], 0, 0, back, numElements=[10], recombine=True)
vol_ext2 = gmsh.model.geo.extrude([(2, 2)], 0, 0, back, numElements=[10], recombine=True)

print()

# Creo líneas transfinias
gmsh.model.mesh.setTransfiniteCurve

gmsh.model.geo.synchronize()
gmsh.model.addPhysicalGroup(3, [vol_ext1[1][1], vol_ext2[1][1]], 101)




# Estructurar la malla
m = 10
n = 15

for tag in [vol_ext1[0][1], vol_ext1[2][1], vol_ext1[3][1], vol_ext1[4][1], vol_ext1[5][1]]:
    gmsh.model.geo.mesh.setTransfiniteSurface(tag)

for tag in [vol_ext1[2][1], vol_ext1[3][1], vol_ext2[2][1], vol_ext2[3][1]]:
    gmsh.model.geo.mesh.setTransfiniteSurface(tag, n+1)

    
#for tag in [vol_ext1[4][1], vol_ext1[5][1], vol_ext2[4][1], vol_ext2[5][1]]:
#    gmsh.model.geo.mesh.setTransfiniteSurface(tag, n+1)


gmsh.model.mesh.generate(3)

# Ver las "caras" de los elementos finitos 2D
gmsh.option.setNumber('Mesh.VolumeFaces', 1)

# Ver los nodos de la malla  
gmsh.option.setNumber('Mesh.Points', 1)        

# Y finalmente guardar la malla
filename = 'primeraPrueba.msh'
gmsh.write(filename)

# Podemos visualizar el resultado en la interfaz gráfica de GMSH
gmsh.fltk.run()

# Tras finalizar el proceso se recomienda usar este comando
gmsh.finalize()




