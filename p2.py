import os
import fnmatch
from skip import Schematic

all_schema_files = []

def get_all_schema_files():
    for root, dirs, files in os.walk('.'):
        for file in files:
            if fnmatch.fnmatch(file, '*.kicad_sch'):
                all_schema_files.append(os.path.join(root, file))
    return all_schema_files


print(get_all_schema_files())


for each_schema_file in all_schema_files:
    sch = Schematic(each_schema_file)
    print(each_schema_file)
    for each_power_label in sch.symbol.reference_matches("#PW"):
        location_of_power_flag = each_power_label.at.value
        power_lable_name = each_power_label.Value.value
        #trim the power label name if it has a start +
        if power_lable_name.startswith('+'):
            power_lable_name = power_lable_name[1:]
        print(power_lable_name)
        # new global label
        g_label = sch.global_label.new()
        g_label.value = "VCC_"+str(power_lable_name)
        g_label.at.value = location_of_power_flag
        each_power_label.delete()
        sch.global_label.append(g_label)
    sch.overwrite()
        #print which file is being processed

print("Done")
