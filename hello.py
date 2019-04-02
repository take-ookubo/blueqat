from blueqat import Circuit
print(Circuit().h[0].m[:].run(shots=100))
