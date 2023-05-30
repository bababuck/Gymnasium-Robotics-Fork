num_segs = 15
rope_xml = []
cylinder_diam = 0.003
cylinder_height = 0.008
spacing = 0.015
sq_width = [0.005, 0.005]
rope_xml.append('<mujoco model="rope">')
rope_xml.append('<body name="CB0" pos="1.25 .75 0.4025">')
rope_xml.append('<joint name="object1:joint" type="free" damping="0.01"></joint>')
#rope_xml.append('<inertial pos="0 0 0.01" quat="0.707107 0 0.707107 0" mass="0.0001" diaginertia="2.52375e-09 2.52375e-09 6.38791e-09"/>')
#rope_xml.append(f'<geom name="CGH0" size="0.001 .01" pos="0 0 .01" type="cylinder"></geom>')
rope_xml.append(f'<geom name="CGH0" size="{cylinder_diam} {cylinder_height}" pos="0 0 .01" type="cylinder" rgba="0 0 1 0"></geom>')

#rope_xml.append('<inertial pos="0 0 0" quat="0.707107 0 0.707107 0" mass="0.00136136" diaginertia="2.52375e-06 2.52375e-06 6.38791e-07"/>')
#rope_xml.append('<geom name="CGH0" size="0.0025 0.005" quat="0.707107 0 0.707107 0" type="capsule" rgba="0.8 0.2 0.1 1"/>')

rope_xml.append(f'<geom name="CG0" size="0.0035 {sq_width[0]} {sq_width[1]}" quat="0.707107 0 0.707107 0" type="box" rgba="0.8 0.2 0.1 1"/>')
for i in range(1,num_segs):
    rope_xml.append(f'<body name="CB{i}" pos="{spacing} 0 0">')
#    rope_xml.append('<inertial pos="0 0 0" quat="0.707107 0 0.707107 0" mass="0.0001" diaginertia="2.52375e-09 2.52375e-09 6.38791e-09"/>')
    rope_xml.append(f'<joint name="CJ0_{i}" pos="-0.02 0 0" axis="0 1 0" group="3" damping="0.003"/>')
    rope_xml.append(f'<joint name="CJ1_{i}" pos="-0.02 0 0" axis="0 0 1" group="3" damping="0.003"/>')
#    rope_xml.append(f'<geom name="CGH{i}" size="0.001 .01" pos="0 0 .01" type="cylinder"></geom>')
    rope_xml.append(f'<geom name="CGH{i}" size="{cylinder_diam} {cylinder_height}" pos="0 0 .01" type="cylinder" rgba="0 0 1 0"></geom>')
#    rope_xml.append('<inertial pos="0 0 0" quat="0.707107 0 0.707107 0" mass="0.00136136" diaginertia="2.52375e-06 2.52375e-06 6.38791e-07"/>')
 #   rope_xml.append(f'<geom name="CGH{i}" size="0.0025 0.005" quat="0.707107 0 0.707107 0" type="capsule" rgba="0.8 0.2 0.1 1"/>')
    rope_xml.append(f'<geom name="CG{i}" size="0.0035 {sq_width[0]} {sq_width[1]}" quat="0.707107 0 0.707107 0" type="box" rgba="0.8 0.2 0.1 1"/>')

for i in range(num_segs):
    rope_xml.append('</body>')
rope_xml.append('</mujoco>')

print("\n".join(rope_xml))