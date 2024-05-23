from skip import Schematic


sheetName="onp.kicad_sch"

sch = Schematic(sheetName)


for each_power_label in sch.symbol.reference_matches("#PW"):
    location_of_power_flag = each_power_label.at.value
    power_lable_name = each_power_label.Value.value
    print(power_lable_name)
    # new global label
    g_label = sch.global_label.new()
    g_label.value = "VCC_"+str(power_lable_name)
    g_label.at.value = location_of_power_flag
    sch.global_label.append(g_label)
    each_power_label.delete()
    sch.write(sheetName)
