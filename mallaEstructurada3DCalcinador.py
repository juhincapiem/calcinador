import gmsh
import sys
import os

gmsh.initialize()
gmsh.option.setNumber("General.Terminal",1)
gmsh.model.add("calcinador")

front = 4.0
back = -4.0

#Definir puntos
gmsh.model.geo.addPoint(0.0, 4.0, front, 1, 1)
gmsh.model.geo.addPoint(20.0, 0.0, front, 1, 2)
gmsh.model.geo.addPoint(20.0, 8.0, front, 1, 3)
gmsh.model.geo.addPoint(9.0, 16.0, front, 1, 4)
gmsh.model.geo.addPoint(6.0, 16.0, front, 1, 5)
gmsh.model.geo.addPoint(0.0, 12.0, front, 1, 6)
#Puntos del ducto
gmsh.model.geo.addPoint(10.0, 18.0, front, 1, 7)
gmsh.model.geo.addPoint(10.0, 22.0, front, 1, 8)
gmsh.model.geo.addPoint(5.0, 18.0, front, 1, 9)
gmsh.model.geo.addPoint(5.0, 22.0, front, 1, 10)

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


# Estructurar la malla
m = 60
n = 40
l = 10
d = 20

for tag in [6, -2, 5, -3, 13, -11]:
    gmsh.model.geo.mesh.setTransfiniteCurve(tag, n+1)

for tag in [13, -11]:
    gmsh.model.geo.mesh.setTransfiniteCurve(tag, d+1)

for tag in [10, -8]:
    gmsh.model.geo.mesh.setTransfiniteCurve(tag, l+1)

for tag in [1, -7, -4, -9, -12]:
    gmsh.model.geo.mesh.setTransfiniteCurve(tag, m+1)


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
vol_ext1 = gmsh.model.geo.extrude([(2, 1)], 0, 0, back, numElements=[30], recombine=True)
vol_ext2 = gmsh.model.geo.extrude([(2, 2)], 0, 0, back, numElements=[30], recombine=True)
tobera = gmsh.model.geo.extrude([(2, 3)], 0, 0, back, numElements=[30], recombine=True)
ducto = gmsh.model.geo.extrude([(2, 4)], 0, 0, back, numElements=[30], recombine=True)


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
gmsh.model.setPhysicalName(2, 1, "wall") 

gmsh.model.addPhysicalGroup(2, [1, 2, 3, 4], 4)
gmsh.model.setPhysicalName(2, 4, "front")

gmsh.model.addPhysicalGroup(2, [35, 57, 79, 101], 5)
gmsh.model.setPhysicalName(2, 5, "back")



#gmsh.model.addPhysicalGroup(2, [24], 6)
#gmsh.model.setPhysicalName(2, 6, "interphase")

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


