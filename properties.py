class Celsius:

    def __init__(self,temperature):
        self.temperature=temperature

    def to_farenheit(self):
        return self.temperature * 1.8 + 32

    @property
    def temperature(self):
        print("getting temperature")
        return self._temperature

    @temperature.setter
    def temperature(self,value):
        print("setting temperature")
        if value < -273:
            raise ValueError('Temperature below -273 is not possible')
        self._temperature=value

C=Celsius(32)
print(C.to_farenheit())
C.temperature=180
C._temperature=150
print(C.temperature)
