class TaxCalculator:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(TaxCalculator, cls).__new__(cls)
        return cls._instance

    def calcular_impuestos(self, base_imponible):
        iva = base_imponible * 0.21
        iibb = base_imponible * 0.05
        contrib_munic = base_imponible * 0.012
        total_impuestos = iva + iibb + contrib_munic
        return total_impuestos

# Uso
tax_calc = TaxCalculator()
print(tax_calc.calcular_impuestos(1000))  # Output: 272.0
