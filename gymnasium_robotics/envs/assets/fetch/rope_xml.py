rope_xml = []
rope_xml.append('<mujoco model="rope">')
rope_xml.append('<body name="CB0" pos="1.35 .75 0.4025">')
rope_xml.append('<inertial pos="0 0 0.01" quat="0.707107 0 0.707107 0" mass="0.0136136" diaginertia="2.52375e-06 2.52375e-06 6.38791e-07"/>')
rope_xml.append(f'<geom name="CG0" size="0.0025 0.0025 0.005" quat="0.707107 0 0.707107 0" type="box" rgba="0.8 0.2 0.1 1"/>')
rope_xml.append(f'<geom name="CGH0" size="0.001 .01" pos="0 0 .01" type="cylinder"></geom>')
for i in range(1,8):
    rope_xml.append(f'<body name="CB{i}" pos="0.015 0 0">')
    rope_xml.append('<inertial pos="0 0 0" quat="0.707107 0 0.707107 0" mass="0.0136136" diaginertia="2.52375e-06 2.52375e-06 6.38791e-07"/>')
    rope_xml.append(f'<joint name="CJ0_{i}" pos="-0.02 0 0" axis="0 1 0" group="3" damping="0.005"/>')
    rope_xml.append(f'<joint name="CJ1_{i}" pos="-0.02 0 0" axis="0 0 1" group="3" damping="0.005"/>')
    rope_xml.append(f'<geom name="CG{i}" size="0.0025 0.0025 0.005" quat="0.707107 0 0.707107 0" type="box" rgba="0.8 0.2 0.1 1"/>')
    rope_xml.append(f'<geom name="CGH{i}" size="0.001 .01" pos="0 0 .01" type="cylinder"></geom>')

for i in range(8):
    rope_xml.append('</body>')
rope_xml.append('</mujoco>')

print("\n".join(rope_xml))