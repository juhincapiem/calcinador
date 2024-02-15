import gmsh
import sys
import os

# Parametros del problema
t = 30
h_v = [i*2 + 2 for i in range(60)]
L = 40
p = 1

lc = 1

for i in range(len(h_v)):
    h = h_v[i]
    lf = 0.05 * h

    file_name = f"{h/L:.3f}.msh"

    gmsh.initialize()

    gmsh.model.add("872")

    # Definir puntos
    gmsh.model.geo.addPoint(0, 0, 0, lf, 1)
    gmsh.model.geo.addPoint(L, 0, 0, lc, 2)
    gmsh.model.geo.addPoint(L, h, 0, lc, 3)
    gmsh.model.geo.addPoint(0, h, 0, lf, 4)

    # Lineas rectas
    gmsh.model.geo.addLine(1, 2, 1)
    gmsh.model.geo.addLine(2, 3, 2)
    gmsh.model.geo.addLine(3, 4, 3)
    gmsh.model.geo.addLine(4, 1, 4)

   # Definir curvas
    gmsh.model.geo.addCurveLoop([i for i in range(1, 5, 1)], 1)

    # Superficie
    gmsh.model.geo.addPlaneSurface([1], 1)


    gmsh.model.geo.synchronize()

    gmsh.model.addPhysicalGroup(1, [3], 1, name = f"PRES WN={p}")
    gmsh.model.addPhysicalGroup(1, [4], 2, name = f"DISP UX=0 UY=0")

    gmsh.model.addPhysicalGroup(2, [1], 1, name = f"CATE EYOU=72 POIS=1e-10 TESP={t} TIPR=20")

    gmsh.model.mesh.generate(2)

    gmsh.option.setNumber("Mesh.MshFileVersion", 2)

    gmsh.write(f"{os.getcwd()}\\DATOS\\Proyecto 1\\Punto 2\\{file_name}")


    # if '-nopopup' not in sys.argv:
    #     gmsh.fltk.run()


    gmsh.finalize()


    # Para resolver el problema: 'PEFICA "Proyecto 1/t1"'

    # Para resolverlo en matlab
    # matlab -batch "PEFICA 'Proyecto 1/t1'"  
