from blueqat import BlueqatGlobalSetting

class HelloGate(Gate):
    lowername = "hello"
    def fallback(self, n_qubits):
        print("Hello")
        return []

BlueqatGlobalSetting.register_gate("hello", HelloGate)
BlueqatGlobalSetting.register_gate("yeah", HelloGate)
c = Circuit().hello[0].yeah[0]
c.run()
