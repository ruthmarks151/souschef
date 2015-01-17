def convert(value,current_unit,desired_unit):
    try:
        current = ureg.parse_expression(current_unit)
        desired = ureg.parse_expression(desired_unit)
        measurement = value * current
        return measurement.to(desired)
    except pint.unit.DimensionalityError,pint.unit.UndefinedUnitError:
        pass
